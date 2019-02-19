from flask import Flask, render_template, request, redirect
from flask_socketio import SocketIO
import sqlite3
import sys
DATABASE = 'database.db'
conn = None
try:
    conn = sqlite3.connect(DATABASE)
    print('[-] Connected to the  Sqlite Database')

except sqlite3.Error as e:
    print("Database connection error: {}".format(e))
    sys.exit(0)

finally:
    conn.close()
    print('[*] Disconnected from database')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'soyunallavesecreta'
socketio = SocketIO(app)    # start the connection with the flask server.

# Events


@socketio.on('message')
def handle_messages(msg):
    print('received {}'.format(msg))


@app.route('/')
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        # there is a user trying to do a loging in my app
        username = request.form['inputUser']
        password = request.form['inputPass']
        print('{} : {}'.format(username, password))
    return('/xxxx')



@app.route('/chat')
def chatView():
    return render_template('chat.html')


@app.route('/registro', methods=['POST', 'GET'])
def regView():
    if request.method == 'POST':
        # Nombres,apellidos,login, password, edad y género.
        try:
            name = request.form['inputName']
            lastname = request.form['inputLastname']
            username = request.form['inputUser']
            age = request.form['inputAge']
            password = request.form['inputPass']
            print('{}{}{}{}'.format(name, username, lastname, age))
            with sqlite3.connect("database.db") as conn:
                cur = conn.cursor()
                sql = "INSERT INTO Users (name,lastname,username,age,password) VALUES(?,?,?,?,?)"
                cur.execute(sql, (name, lastname, username, age, password))
                conn.commit()
                result = '[Ok] Registro agregado a la base de datos'
                print(result)
        except sqlite3.Error as e:
            print("Database connection error: {}".format(e))
            conn.rollback()
            result = "There was an error when trying to save to database: {}".format(
                e)
            print(result)
        finally:
            return render_template('results.html', result=result)
    elif request.method == 'GET':
        return render_template('registro.html')
    else:
        redirect('/')


if __name__ == "__main__":
    socketio.run(app, debug=True)
