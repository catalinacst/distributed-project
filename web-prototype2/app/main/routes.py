from flask import session, redirect, url_for, render_template, request
from . import main
from .forms import LoginForm
from flask_wtf import FlaskForm as BaseForm
roomlist = []
user_list = []


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
    return render_template('index.html', form=form, lista=roomlist)


@main.route('/registrar', methods=['GET', 'POST'])
def registrar():
    form = LoginForm()
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
        return redirect(url_for('.chat'))
    elif request.method == 'GET':
        form.name.data = session.get('name', '')
        form.room.data = session.get('room', '')
    return render_template('registrar.html', form=form, lista=roomlist)


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
    return render_template('chat.html', name=name, room=room)