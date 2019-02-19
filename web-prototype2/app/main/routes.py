from flask import session, redirect, url_for, render_template, request, jsonify
import sqlite3
from . import main
from .forms import LoginForm, RegistrationForm
from flask_wtf import FlaskForm as BaseForm
roomlist = []
user_list = []

roomlist.append('publico')      # we create the default room

@main.route('/', methods=['GET', 'POST'])
def index():
    """Login form to enter a room."""
    form = LoginForm()
    archivo = open("archivo.txt", "a")  # replace with database
    a = "Usuario: " + str(form.name.data) + "  Sala: " + \
        str(form.room.data) + " \n"
    archivo.write(str((a)))
    archivo.close()
    if form.validate_on_submit():
        if not (roomlist):
            roomlist.append(form.room.data)
        else:
            if(verificar(form.room.data)):
                print("ya esta")
            else:
                roomlist.append(form.room.data)
        session['name'] = form.name.data
        session['room'] = form.room.data
        #session['age'] = form.age.data
        return redirect(url_for('.chat'))

    elif request.method == 'GET':
        form.name.data = session.get('name', '')
        form.room.data = session.get('room', '')
    return render_template('index.html', form=form, roomlist=roomlist)

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
                sql = "INSERT INTO Users (name,lastname,username,age,password,gender) VALUES(?,?,?,?,?,?)"
                cur.execute(sql, (first_name, lastname,
                                  username,age, password, gender))
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
    if name == '' or room == '':
        return redirect(url_for('.index'))
    return render_template('chat.html', user_list=user_list, roomlist=roomlist)
