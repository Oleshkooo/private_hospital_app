import sqlite3
import random

global db, sql
db = sqlite3.connect('server.db')
sql = db.cursor()

sql.execute('''CREATE TABLE IF NOT EXISTS users (
	login Text,
	password Text,
	cash int

	)''')
db.commit()

def reg():
	user_login = input('login: ')
	user_password = input('Password: ')

	sql.execute(f'SELECT login FROM users WHERE login = "{user_login}" ')
	if sql.fetchone() is None:
		sql.execute(f"INSERT INTO users VALUES (?, ?, ?)" , (user_login, user_password, 0))
		db.commit()
		print('вас успішно зарегестровано')
	else:
		print('така запись вже є ')

		for value in sql.execute(f"SELECT * FROM users"):
			print(value)

def casino():
	print('вас вітає казіно ведіть свої дані щоб поучаствувати')
	user_login = input('log in: ')
	number = random.randint(1, 2)

	sql.execute(f'SELECT login FROM users WHERE login = "{user_login}" ')
	if sql.fetchone() is None:
		print('Такого користувача не існує зарегиструйтесь')
		reg()
	else:	
		if number == 1:
			sql.execute(f'UPDATE users SET cash = {1000} WHERE login = "{user_login}"')
			print('ви виграли!')
			db.commit()
		else:

			print('game over!')

def enter():
	for i in sql.execute('SELECT login, cash FROM users'):
		print(i)

def main():
	casino()
	enter()

main()		