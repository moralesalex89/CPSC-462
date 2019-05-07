from includes.DatabaseFunctions import *

x = db_query("select * from Users")
for p in x:
	print(p)