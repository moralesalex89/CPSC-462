from includes.DatabaseFunctions import *

print(create_user("test2", "test", 1, ""))


verify_login("test", "test")
verify_login("test2", "test")
verify_login("test", "test2")

if verify_login("test", "test"):
	print("Login verified")
else:
	print("Username and/or password is incorrect")

if verify_login("test2", "test"):
	print("Login verified")
else:
	print("Username and/or password is incorrect")

if verify_login("test", "test2"):
	print("Login verified")
else:
	print("Username and/or password is incorrect")