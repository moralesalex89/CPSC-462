from includes.DatabaseConfig import db


def db_query(query):
	# Basic handling of database queries
	db_cursor = db.cursor()
	db_cursor.execute(query)
