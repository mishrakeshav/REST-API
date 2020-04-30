import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username VARCHAR(50) UNIQUE, password VARCHAR(30))"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name VARCHAR(50) UNIQUE, price real)"
cursor.execute(create_table)




connection.commit()
connection.close()