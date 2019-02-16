#!/usr/bin/env python3
import sqlite3
from subprocess import call
from os import remove, path

DBNAME = 'database.db'

if path.exists(DBNAME):
    remove(DBNAME)
    call(['touch', DBNAME])
else:
    call(['touch', DBNAME])

print('Database Poblation')
# Table creation
sqlUser = 'CREATE TABLE Users (id integer primary key autoincrement, name TEXT, lastname TEXT, username TEXT, age INTEGER, password TEXT)'
sqlRooms = 'CREATE TABLE Room (id integer primary key autoincrement, name TEXT, count_users INTEGER, owner TEXT)'

try:
    print("Opened database successfully")
    conn = sqlite3.connect('database.db')
    conn.execute(sqlUser)
    conn.execute(sqlRooms)
    print("Table created successfully")
except sqlite3.Error as e:
    print("Database connection error: {}".format(e))
finally:
    conn.close()

    print('[*] Disconnected from database')
