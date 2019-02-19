import sqlite3

#Checking for new users
def was_here(user_id):
	found = False
	cnn = sqlite3.connect('database/users.db')#Connect to users.db database
	c = cnn.cursor()
    #Create database if not exists
	c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    user_id TEXT NOT NULL, username TEXT NOT NULL, Date DATETIME NOT NULL)''')
	users = c.execute("SELECT * FROM users")
	cnn.close()
    #Check is user_id in users informations
	for user in users:
		chat_id = user[1]
		if user_id == chat_id:
			found = True
			break
	return found