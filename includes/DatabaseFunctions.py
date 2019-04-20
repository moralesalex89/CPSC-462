from includes.DatabaseConfig import db
import bcrypt


def db_query(query):
	# Basic handling of database queries
	db_cursor = db.cursor()
	db_cursor.execute(query)
	return db_cursor


def create_user(username, password, user_type, address):
	# checks to make sure username isn't already taken
	query = "SELECT COUNT(name) FROM Users WHERE name = '%s'" % username
	result = db_query(query).fetchone()
	if result[0]:
		return False
	# if username is available, continue
	hashed_pass = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
	query = "INSERT INTO Users (name, pass, user_type, address) VALUES ('%s','%s','%d','%s')" % (username, hashed_pass.decode('utf8'), user_type, address)
	db_query(query)
	db.commit()
	return True


def verify_login(username, password):
	query = "SELECT pass FROM Users WHERE name = '%s'" % username
	result = db_query(query).fetchone()
	hashed_pass = None
	if result is None:
		return False
	for x in result:
		hashed_pass = x
	verified = bcrypt.checkpw(password.encode('utf8'), hashed_pass.decode('utf8').encode('utf8'))
	return verified

