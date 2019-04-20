from includes.DatabaseConfig import db
import bcrypt


def db_query(query):
	# Basic handling of database queries
	db_cursor = db.cursor()
	db_cursor.execute(query)
	return db_cursor


def create_user(username, password, user_type, address):
	hashed_pass = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
	query = "INSERT INTO Users (name, pass, user_type, address) VALUES ('%s','%s','%d','%s')" % (username, hashed_pass.decode('utf8'), user_type, address)
	db_query(query)
	db.commit()

def verify_login(username, password):
	git 