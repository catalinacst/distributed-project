# Realtime using Flask and Socketio

This application is an experimental prototype for the last project, this has been
coded thinking in create a realtime chat web application.This will expose endpoints 
that are going to be consume by the mobile application. We're going to have a cli 
version too.

# Running

You will need to install a virtual enviroment, activate it and install the requirements. 

```sh 
user@machine$ python3 -m venv venv 
user@machine$ source venv/bin/activate
(venv)user@machine$ git clone https://github.com/h3ct0rjs/distributed-project dp
(venv)user@machine$ cd dp/web-prototype
(venv)user@machine dp/web-prototype $ pip install -r requirements.txt
(venv)user@machine dp/web-prototype $ python main.py
```


If you are unable to startup the process ensure that you use the database creation script
```sh
(venv)user@machine dp/web-prototype $ python database.py
```


