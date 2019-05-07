from tkinter import *
from tkinter import ttk
from includes.DatabaseFunctions import get_reservation, retrieve_user


class User:
	def __init__(self, u_id, u_type, u_name):
		self.userID = u_id
		self.userType = u_type
		self.username = u_name

	def login_user(self, u_name):
		user_info = retrieve_user(u_name)
		self.userID = user_info['id']
		self.userType = user_info['user_type']
		self.username = u_name
		print(user_info['user_type'])
		try:
			self.reservation = get_reservation(self.userID)
		except:
			self.reservation = False

	def get_userID(self):
		return self.userID

	def get_userType(self):
		return self.userType

	def get_username(self):
		return self.username

	def get_reservation(self):
		return self.reservation
