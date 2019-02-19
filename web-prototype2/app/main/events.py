from flask import session, jsonify
from flask_socketio import emit, join_room, leave_room
from .. import socketio
from .routes import roomlist, user_list


@socketio.on('joined', namespace='/chat')
def joined(message):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    name = session.get('name')
    if name in user_list:
        pass
    else:
        user_list.append(session.get('name'))
    join_room(room)
    emit('status', {'msg': session.get('name') +
                    ' has entered the room.'}, room=room)


@socketio.on('text', namespace='/chat')
def text(message):
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
    room = session.get('room')
    emit('message', {'msg': session.get('name') +
                     ':' + message['msg']}, room=room)


@socketio.on('left', namespace='/chat')
def left(message):
    """Sent by clients when they leave a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    leave_room(room)
    emit('status', {'msg': session.get('name') +
                    ' has left the room.'}, room=room)


@socketio.on('cmd', namespace='/chat')
def cmd_handler(message):
    """
    Handle all the commands sent by the client
    """
    available_commands = {
        "#Cr": "Create a new chatroom.",
        "#gR": "Enter specific chatroom.",
        "#eR": "Exit from specific chatroom.",
        "#lR": "List of current chatrooms.",
        "#dR": "delete specific Room .",
        "#show users": "Show current connected users.",
        "#\private": "Send a private message.",
        "#exit": "Finish the chat session.",
        "#help": "Show the help menu with the current available options."
    }

    cmd = message["cmd"]
    name = session.get('name')
    room = session.get('room')
    if cmd == "#exit":
        leave_room(room)
        emit('status', {'msg': session.get('name') +
                        ' has left the room.'}, room=room)
        for i in user_list:
            user_list.remove(name)
        emit('leave', {})

    elif cmd == "#show users":
        for i in user_list:  # debug
            print(i)
        emit('show_users', {'msg': user_list}, room=room)

    elif cmd == "#lR":
        for i in roomlist:  # debug
            print(i)
        emit('show_channels', {'msg': roomlist}, room=room)

    elif cmd == "#help":
        emit('help', {'msg': available_commands})

    elif cmd.split(' ')[0] == "#Cr":
        roomarg = cmd.split(' ')[1]
        roomlist.append(roomarg)
        print(roomlist)
        emit('commands',{'msg': roomarg +' chat room was created'})

    elif cmd.split(' ')[0] == "#dR":
        roomarg = cmd.split(' ')[1]
        if not (roomarg == 'public' or roomarg == 'publico'):
            if roomarg in roomlist :
                emit('commands',{'msg': roomarg +' was deleted from the chan list'})
                roomlist.remove(roomarg)
            else : 
                emit('commands',{'msg': roomarg +' Unable to delete the channel, it doesn\' exist'})
        else :
            print(roomlist)
            emit('commands',{'msg': roomarg +' Impossible to delete default channel'})
    else:
        emit('status', {
             'msg': 'Invalid command, use  #help to get more information.'})