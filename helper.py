# -*- coding: utf-8 -*-
from datetime import datetime
import sqlite3

#Checking for new users
def was_here(user_id):
	found = False
	cnn = sqlite3.connect('database/users.db')#Connect to users.db database
	c = cnn.cursor()
    #Create database if not exists
	c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    user_id TEXT NOT NULL, first_name TEXT NOT NULL, last_name TEXT NOT NULL, username TEXT NOT NULL, Date DATETIME NOT NULL)''')
	users = c.execute("SELECT * FROM users")
    #Check is user_id in users informations
	for user in users:
		chat_id = user[1]
		if user_id == chat_id:
			found = True
			break
	cnn.close()
	return found

#Write new user to database
def write(user_id, first_name, last_name, user_name):
	now = str(datetime.now())[:-7]#Get current time until second as string
	cnn = sqlite3.connect("database/users.db")#Connect to database
	cnn.execute("PRAGMA ENCODING = 'utf8';")#Set encoding uft-8
	cnn.text_factory = str
	c = cnn.cursor()
	c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, user_id TEXT NOT NULL, username TEXT NOT NULL, Date DATETIME NOT NULL)''')
	insert = "INSERT INTO `users`(`user_id`, `first_name`, `last_name`, `username`, `Date`) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}');\
		".format(user_id, first_name, last_name, user_name, now)
	c.execute(insert)
	cnn.commit()
	cnn.close()