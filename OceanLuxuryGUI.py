from tkinter import *
from tkinter import ttk
from User import User
from UserManager import *
from CustomerUI import CustomerUI
from FrontDeskUI import FrontDeskUI
from includes.DatabaseFunctions import create_user, verify_login, get_id


class OceanLuxuryGUI:
	def __init__(self, master):
		self.defont = ("TkDefaultFont", 12)
		self.font_header = ("TkDefaultFont", 14, 'bold')
		self.activeUser = User(-1, -1, "")

		self.img_00 = PhotoImage(file='OL-Assets/OceanLuxuryBanner.png')
		self.img_01 = PhotoImage(file='OL-Assets/home.png')
		self.img_02 = PhotoImage(file='OL-Assets/aboutus.png')
		self.img_03 = PhotoImage(file='OL-Assets/booking.png')
		self.img_04 = PhotoImage(file='OL-Assets/services.png')
		self.img_05 = PhotoImage(file='OL-Assets/login.png')
		self.img_06 = PhotoImage(file='OL-Assets/signup.png')
		self.img_07 = PhotoImage(file='OL-Assets/logout.png')

		# 3 main areas of the screen
		# banner displays the Ocean Luxury logo
		# sidebar_frame displays buttons for navigation
		# main_frame is the parent frame of the other important frames
		self.banner = ttk.Label(master, text="Ocean Luxury Banner", image=self.img_00)
		self.sidebar_frame = ttk.Frame(master)
		self.main_frame = ttk.Frame(master)

		# 3 frames within main_frame
		# center_frame used as default to display
		# message_frame used to display messages/popups to user
		# backup_frame as a extra frame just in case user needs to submit a form without losing the center_frame
		self.center_frame = ttk.Frame(self.main_frame)
		self.message_frame = ttk.Frame(self.main_frame)
		self.backup_frame = ttk.Frame(self.main_frame)

		self.UI_Controller = CustomerUI(self)

		# sidebar buttons displayed on the side, used for navigation
		self.home = ttk.Button(self.sidebar_frame, text="Home", image=self.img_01)
		self.about = ttk.Button(self.sidebar_frame, text="About Us", image=self.img_02)
		self.booking = ttk.Button(self.sidebar_frame, text="Booking", image=self.img_03)
		self.services = ttk.Button(self.sidebar_frame, text="Services", image=self.img_04)
		self.login = ttk.Button(self.sidebar_frame, text="Log-in", image=self.img_05, command=self.login_press)
		self.signup = ttk.Button(self.sidebar_frame, text="Sign Up", image=self.img_06, command=self.signupUser)
		self.logout = ttk.Button(self.sidebar_frame, text="Logout", image=self.img_07, command=self.logoutUser)

		self.display_default()

	# places all tkinter objects on the screen in their default settings
	# used for initialization
	def display_default(self):
		self.banner.grid(column=0, row=0, columnspan=3, sticky=W)
		self.sidebar_frame.grid(column=0, row=1, sticky=W)
		self.main_frame.grid(column=1, row=1)
		self.center_frame.grid()
		self.message_frame.grid()
		self.message_frame.grid_remove()
		self.home.grid()
		self.about.grid()
		self.booking.grid()
		self.services.grid()
		self.set_sidebar_frame(0)

	# clear_center used to destroy all tkinter objects from the center and message frame when not needed
	def clear_center(self):
		self.center_frame.destroy()
		self.center_frame = ttk.Frame(self.main_frame)
		self.center_frame.grid()
		self.message_frame.destroy()
		self.message_frame = ttk.Frame(self.main_frame)
		self.message_frame.grid()
		self.backup_frame.destroy()
		self.backup_frame = ttk.Frame(self.main_frame)
		self.backup_frame.grid()

	# message_press function used to display messages to user over the center frame without affecting the current state
	def display_message_frame(self, msg):
		self.center_frame.grid_forget()
		self.backup_frame.grid_forget()
		self.message_frame.grid()
		self.message = ttk.Label(self.message_frame, text=msg).grid(column=0, row=0)
		self.ok_button = ttk.Button(self.message_frame, text="Ok", command=self.message_confirm).grid(column=0, row=1)

	# message_confirm used on confirmation of a message to return to the previous state of
	def message_confirm(self):
		self.message_frame.destroy()
		self.message_frame = ttk.Frame(self.main_frame)
		self.center_frame.grid()

	# layout : 0 / default = logout not displayed
	# layout : 1 = login/signup not displayed
	def set_sidebar_frame(self, layout):
		self.home.config(command=self.UI_Controller.home_press)
		self.about.config(command=self.UI_Controller.about_press)
		self.booking.config(command=self.UI_Controller.booking_press)
		self.services.config(command=self.UI_Controller.services_press)

		if layout == 1:
			self.logout.grid()
			self.login.grid_forget()
			self.signup.grid_forget()

		else:
			self.login.grid()
			self.signup.grid()
			self.logout.grid_forget()

	def get_center_frame(self):
		return self.center_frame

	def get_backup_frame(self):
		return self.backup_frame

	def get_message_frame(self):
		return self.message_frame

	def display_center_frame(self):
		self.backup_frame.grid_forget()
		self.center_frame.grid()

	def display_backup_frame(self):
		self.center_frame.grid_forget()
		self.backup_frame.grid()

	def make_form(self, frame, name, col, row,shw=None, width=20):
		ttk.Label(frame, text=name, font=self.defont).grid(column=col, row=row)
		value = ttk.Entry(frame, width=width, font=self.defont,show=shw)
		value.grid(column=col+1, row=row)
		return value

	def login_press(self):
		self.clear_center()
		username = self.make_form(self.center_frame, "Username: ", 0, 0)
		password = self.make_form(self.center_frame, "Password: ", 0, 1,shw='*')
		logBtn = ttk.Button(self.center_frame, text="Login", command=lambda: self.loginUser(username.get(), password.get()))
		logBtn.grid(column=0, row=2, columnspan=2)

	def loginUser(self, u_name, password):
		verify = verify_login(u_name, password)
		print(verify)
		usr = self.activeUser
		if verify:
			self.activeUser.login_user(u_name)

		if usr.get_userType() == 'Customer':
			self.UI_Controller = CustomerUI(self)
			self.UI_Controller.home_press()
			self.display_message_frame("Logged in as a Guest")
			self.set_sidebar_frame(1)
		elif usr.get_userType() == 'Employee':
			self.UI_Controller = FrontDeskUI(self)
			self.UI_Controller.home_press()
			self.display_message_frame("Logged in as an Employee")
			self.set_sidebar_frame(1)
		else:
			self.display_message_frame("Invalid username and/or password used, please try again!")

	def logoutUser(self):
		self.UI_Controller = CustomerUI(self)
		self.activeUser = User(-1, -1, "")
		self.set_sidebar_frame(0)
		self.UI_Controller.home_press()

	def signupValidate(self, username, password, pass_check):
		error = ""
		if username == "":
			error = error + " - No username entry\n"
		else:
			if (len(username) < 4) or (len(username) > 20):
				error = error + " - Username invalid, must be 4-20 characters\n"
		if password == "":
			error = error + " - No password entry\n"
		else:
			if password != pass_check:
				error = error + " - Passwords do not match\n"
		if error == "":
			if create_user(username, password, 0, ''):
				self.UI_Controller.home_press()
				self.display_message_frame("Your account was created successfully!")
				self.set_sidebar_frame(1)
			else:
				self.display_message_frame("Your account could not be created!")
		if error != "":
			self.display_message_frame(error)

	def signupUser(self):
		self.clear_center()
		username = self.make_form(self.center_frame, "Username: ", 0, 0)
		password = self.make_form(self.center_frame, "Password: ", 0, 1)
		pass_check = self.make_form(self.center_frame, "Re-enter Password: ", 0, 2)
		ttk.Button(self.center_frame, text="Sign-Up", command=lambda: self.signupValidate(username.get(), password.get(), pass_check.get())).grid(columnspan=2)