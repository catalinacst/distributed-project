from flask import session, jsonify
from flask_socketio import emit, join_room, leave_room
from .. import socketio
from .routes  import roomlist, user_list


@socketio.on('joined', namespace='/chat')
def joined(message):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    name = session.get('name')
    if name in user_list : 
        pass
    else : 
        user_list.append(session.get('name'))
    join_room(room)
    emit('status', {'msg': session.get('name') + ' has entered the room.'}, room=room)


@socketio.on('text', namespace='/chat')
def text(message):
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
    room = session.get('room')
    emit('message', {'msg': session.get('name') + ':' + message['msg']}, room=room)


@socketio.on('left', namespace='/chat')
def left(message):
    """Sent by clients when they leave a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    leave_room(room)
    emit('status', {'msg': session.get('name') + ' has left the room.'}, room=room)

@socketio.on('cmd', namespace='/chat')
def cmd_handler(message):
    """
    Handle all the commands sent by the client
    """
    available_commands = {
        "#Cr" : "Crear Sala con el nombre de la Sala.", 
        "#gR" : "Entrar a una Sala especifica.", 
        "#eR" : "Salir de la sala, estando en default no hace nada.", 
        "#lR" : "Lista los nombre de todas las sales disponibles y numero de participantes.",
        "#dR" : "Eliminar la sala nombreSala, solo se puede eliminar la sala si se es dueño.", 
        "#show users" : "Muestra el lista de usuarios en el chat.", 
        "#\private" : "Envia mensaje privado a otra persona.", 
        "#exit" : " Abandona el servidor.", 
        "#help" : "Muestra esta ayuda contextual."
    }

    cmd = message["cmd"]
    name = session.get('name')
    room = session.get('room')
    print(room)
    if cmd == "#exit":
        leave_room(room)
        emit('status', {'msg': session.get('name') + ' has left the room.'}, room=room) 
        for i in user_list: 
            user_list.remove(name)
        emit('leave',{})

    elif cmd == "#show users":
        for i in user_list :        #debug
            print(i)
        emit('show_users', {'msg':user_list}, room=room)
    
    elif cmd == "#lR":
        for i in roomlist :        #debug
            print(i)
        emit('show_channels', {'msg':roomlist}, room=room)
    elif cmd == "#help":
        emit('help', {'msg': available_commands})
    elif cmd == "#Cr":
        pass
    else : 
        emit('status',{'msg':'Comando Invalido, Revisa tu sintaxis, #help para mas ayuda'})

    print('Estamos recibiendo msgs del cliente {}'.format(cmd))

