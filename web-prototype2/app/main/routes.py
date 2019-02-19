from flask import session, redirect, url_for, render_template, request, jsonify
import sqlite3
from . import main
from .forms import LoginForm, RegistrationForm, LoginForm_exp
from flask_wtf import FlaskForm as BaseForm
roomlist = []
user_list = []


roomlist.append('public')      # we create the default room
@main.route('/', methods=['GET', 'POST'])
def index():
    """Login form to enter a room."""
    form = LoginForm_exp()
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username  = form.username.data 
        password = form.password.data
        try:
            with sqlite3.connect("database.db") as conn:
                cur = conn.cursor()
                cur.execute("SELECT * FROM Users WHERE  username = ? and password=?",(username,password))
                rows = cur.fetchall()
                if len(rows) == 0:
                    result = '[!!] Failed to Register, Username is registered, use another one'
                    return redirect(url_for('.index'))
                else : 
                    session['name'] = username
                    session['room'] = 'public'
                    print('{} {}'.format(username, password))
                    return redirect(url_for('.chat'))
        except sqlite3.Error as e:
            print("Database connection error: {}".format(e))
            conn.rollback()
            result = "There was an error when trying to save to database: {}".format(
                e)
            print(result)
    else :
        return jsonify({'msg':'HTTP Verb invalid'})
   

@main.route('/registro', methods=['GET', 'POST'])
def registrar():
    form = RegistrationForm()
    if request.method == 'GET':
        return render_template('signup.html', form=form)
    elif request.method == 'POST':
        print('Datos From Formulario:::')
        try:
            first_name = form.first_name.data
            lastname = form.last_name.data
            username = form.username.data
            password = form.password.data
            age = form.age.data
            gender = form.gender.data
            print('{}{}{}{}{}{}'.format(first_name,
                                        lastname, username, password, age, gender))
            with sqlite3.connect("database.db") as conn:
                cur = conn.cursor()
                cur.execute("SELECT * FROM Users WHERE  username = ?",(username,))
                rows = cur.fetchall()
                if len(rows) == 0:
                    sql = "INSERT INTO Users (name,lastname,username,age,password,gender) VALUES(?,?,?,?,?,?)"
                    cur.execute(sql, (first_name, lastname,
                                  username,age, password, gender))
                    conn.commit()
                    result = '[Ok] Registro agregado a la base de datos'
                    print(result)
                else : 
                    result = '[!!] Failed to Register, Username is registered, use another one'
        except sqlite3.Error as e:
            print("Database connection error: {}".format(e))
            conn.rollback()
            result = "There was an error when trying to save to database: {}".format(
                e)
            print(result)
        finally:
            return render_template('results.html', result=result)
    else:
        return jsonify({'msg':'method not allowed'})

@main.route('/ingresar', methods=['GET', 'POST'])
def verificar(dato):
    for a in roomlist:
        if(a == dato):
            return True
    return False

@main.route('/chat')
def chat():
    """Chat room. The user's name and room must be stored in
    the session."""
    name = session.get('name', '')
    room = session.get('room', '')
    if name == '' or room == '' or len(user_list) == 0:
        return redirect(url_for('.index'))
    return render_template('chat.html', user_list=user_list, roomlist=roomlist)
