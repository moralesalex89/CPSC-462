from includes.DatabaseConfig import db
import bcrypt


def db_query(query):
	# Basic handling of database queries
	db_cursor = db.cursor(buffered=True)
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

#@return - list of reservation details obtained from a user_id
def get_reservation(user_id):
	query = "SELECT * FROM Reservations WHERE user_id = '%d'" % user_id
	result = list(db_query(query).fetchone())
	query = "SELECT room_type FROM Rooms WHERE room_id = '%d'" % result[4]
	result2 = db_query(query).fetchone()
	result.append(result2[0])
	return result

def get_id(username):
	query = "SELECT user_id FROM Users WHERE name = '%s'" % username
	result = db_query(query).fetchone()
	return result[0]
	
def verify_login(username, password):
	query = "SELECT pass FROM Users WHERE name = '%s'" % username
	result = db_query(query).fetchone()
	hashed_pass = None
	if result is None:
		return False
	for x in result:
		hashed_pass = x
	verified = bcrypt.checkpw(password.encode('utf8'), hashed_pass.encode('utf8'))
	return verified
