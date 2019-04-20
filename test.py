from includes.DatabaseFunctions import *


create_user("test", "test", 1, "")

for x in db_query("SELECT * from Users"):
    print(x)
