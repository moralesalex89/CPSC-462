from includes.DatabaseConfig import DBInfo
import mysql.connector

dbLogin = DBInfo()

# Used to prevent db login info from leaking onto Github
db = mysql.connector.connect(
	host=dbLogin.dbHost,
	user=dbLogin.dbUser,
	passwd=dbLogin.dbPass,
	database=dbLogin.dbDatabase
)


def db_query(query):
	# Basic handling of database queries
	db_cursor = db.cursor()
	db_cursor.execute(query)
