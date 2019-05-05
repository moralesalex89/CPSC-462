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


addHousekeepingEntry(3, '04:30p')

self.clear_frames()
        ttk.Label(self.center, text="Start date").grid(column=1,row=0,columnspan=1)
        ttk.Label(self.center, text="End date").grid(column=3,row=0,columnspan=1)
        self.sDate = dateEntry(self.center,rowpos=1,colpos=1,colspan=1,text=self.sDate.prev)
        self.eDate = dateEntry(self.center,rowpos=1,colpos=3,colspan=1,text=self.eDate.prev)
        ttk.Button(self.center,text="Search", command=self.validate_dates,width=10).grid(row=3,column=1,columnspan = 3,pady=5)