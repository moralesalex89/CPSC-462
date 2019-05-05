from tkinter import *
from tkinter import ttk
from User import User
from reservationManager import resManager
from includes.DatabaseFunctions import *


class FrontDeskUI:
	def __init__(self, UI_Controller):
		self.UI = UI_Controller
		self.go_back = []
		self.defont = UI_Controller.defont
		self.font_header = UI_Controller.font_header
		self.center = UI_Controller.get_center_frame()
		self.backup = UI_Controller.get_backup_frame()
		self.message = UI_Controller.get_message_frame()
		self.activeUser = UI_Controller.activeUser
		self.resManager = resManager()

	# ____________________HOME____________________
	def home_press(self):
		self.clear_frames()
		self.Label = ttk.Label(self.center, text="Welcome Employee").grid()

	# ____________________ABOUT____________________
	def about_press(self):
		self.clear_frames()
		ttk.Label(self.center, text="You are in FrontDeskUI").grid()

	# ____________________BOOKING____________________
	def booking_press(self):
		self.clear_frames()

	# ____________________SERVICES____________________
	def services_press(self):
		self.clear_frames()
		ttk.Button(self.center, text="Food Service", command=self.food_service_press).grid()
		ttk.Button(self.center, text="Room Maintenance", command=self.room_maintenance_press).grid()
		ttk.Button(self.center, text="Guest Services", command=self.guest_service_press).grid()

	def food_service_press(self):
		self.clear_frames()

	def room_maintenance_press(self):
		self.clear_frames()

	def guest_service_press(self):
		self.clear_frames()
		ttk.Button(self.center, text="Check-in Guest", command=self.check_in_press).grid(column=0, row=0)
		ttk.Button(self.center, text="Check-out Guest", command=self.check_out_press).grid(column=1, row=0)

	def check_in_press(self):
		self.clear_frames()
		ttk.Label(self.center, text="Please enter guest information below to search guest reservations:").grid(column=0, columnspan=2, row=0, pady=10)
		ttk.Label(self.center, text="Guest Username: ").grid(column=0, row=1)
		guest_username = ttk.Entry(self.center, font=self.defont)
		guest_username.grid(column=1, row=1)
		guest_username.bind('<Return>', lambda event: self.check_in_search_press(guest_username.get()))
		search_button = ttk.Button(self.center, width=50, text="Search", command=lambda: self.check_in_search_press(guest_username.get())).grid(column=0, row=2, columnspan=2, pady=5)
		back_button = ttk.Button(self.center, text="Go Back", command=self.guest_service_press).grid(column=0, row=3, columnspan=2, pady=2)

	def check_in_search_press(self, username):
		reservation_info = self.resManager.checkGuestReservation(username)
		if reservation_info is False:
			self.UI.display_message_frame("No reservations found for %s" % username)
			return False
		room_info = self.resManager.checkRoomInfo(reservation_info[4])
		self.clear_frames()
		ttk.Label(self.center, text="Reservation Found", font=self.font_header).grid(column=0, row=0, padx=0, pady=10, columnspan=2)
		ttk.Label(self.center, text="Check-in Date: ").grid(column=0, row=1)
		ttk.Label(self.center, text=reservation_info[1]).grid(column=1, row=1)
		ttk.Label(self.center, text="Check-out Date: ").grid(column=0, row=2)
		ttk.Label(self.center, text=reservation_info[2]).grid(column=1, row=2)
		ttk.Label(self.center, text="Room Number: ").grid(column=0, row=3)
		ttk.Label(self.center, text="Room #%d" % reservation_info[4]).grid(column=1, row=3)
		ttk.Label(self.center, text="Room Type: ").grid(column=0, row=4)
		ttk.Label(self.center, text=room_info[1].capitalize()).grid(column=1, row=4)
		ttk.Label(self.center, text="Room Status: ").grid(column=0, row=5)
		ttk.Label(self.center, text=room_info[2]).grid(column=1, row=5)
		if room_info[2] == 'Empty':
			ttk.Button(self.center, text="Check-in Guest", command=lambda: self.check_in_guest(reservation_info)).grid(column=0, row=6, columnspan=2, pady=10)
		back_button = ttk.Button(self.center, text="Go Back", command=self.check_in_press).grid(column=0, row=7, columnspan=2, pady=2)

	def check_in_guest(self, reservation_info):
		self.resManager.updateReservation(reservation_info[4], 'Reserved')
		self.check_in_search_press(retrieve_user_by_id(reservation_info[3])['username'])
		self.UI.display_message_frame("Guest has been successfully checked in!")

	def check_out_press(self):
		self.clear_frames()
		ttk.Label(self.center, text="Please enter guest information below to search guest reservations:").grid(column=0, columnspan=2, row=0, pady=10)
		ttk.Label(self.center, text="Guest Username: ").grid(column=0, row=1)
		guest_username = ttk.Entry(self.center, font=self.defont)
		guest_username.grid(column=1, row=1)
		guest_username.bind('<Return>', lambda event: self.check_in_search_press(guest_username.get()))
		search_button = ttk.Button(self.center, width=50, text="Search", command=lambda: self.check_out_search_press(guest_username.get())).grid(column=0, row=2, columnspan=2, pady=5)
		back_button = ttk.Button(self.center, text="Go Back", command=self.guest_service_press).grid(column=0, row=3, columnspan=2, pady=2)

	def check_out_search_press(self, username):
		reservation_info = self.resManager.checkGuestReservation(username)
		if reservation_info is False:
			self.UI.display_message_frame("No reservations found for %s" % username)
			return False
		room_info = self.resManager.checkRoomInfo(reservation_info[4])
		self.clear_frames()
		ttk.Label(self.center, text="Reservation Found", font=self.font_header).grid(column=0, row=0, padx=0, pady=10, columnspan=2)
		ttk.Label(self.center, text="Check-in Date: ").grid(column=0, row=1)
		ttk.Label(self.center, text=reservation_info[1]).grid(column=1, row=1)
		ttk.Label(self.center, text="Check-out Date: ").grid(column=0, row=2)
		ttk.Label(self.center, text=reservation_info[2]).grid(column=1, row=2)
		ttk.Label(self.center, text="Room Number: ").grid(column=0, row=3)
		ttk.Label(self.center, text="Room #%d" % reservation_info[4]).grid(column=1, row=3)
		ttk.Label(self.center, text="Room Type: ").grid(column=0, row=4)
		ttk.Label(self.center, text=room_info[1].capitalize()).grid(column=1, row=4)
		ttk.Label(self.center, text="Room Status: ").grid(column=0, row=5)
		ttk.Label(self.center, text=room_info[2]).grid(column=1, row=5)
		if room_info[2] == 'Reserved':
			ttk.Button(self.center, text="Check-out Guest", command=lambda: self.check_out_guest(reservation_info)).grid(column=0, row=6, columnspan=2, pady=10)
		back_button = ttk.Button(self.center, text="Go Back", command=self.check_out_press).grid(column=0, row=7, columnspan=2, pady=2)

	def check_out_guest(self, reservation_info):
		self.resManager.updateReservation(reservation_info[4], 'Empty')
		self.check_out_search_press(retrieve_user_by_id(reservation_info[3])['username'])
		self.UI.display_message_frame("Guest has been successfully checked out")

	# ____________________OTHER____________________
	def clear_frames(self):
		self.UI.clear_center()
		self.center = self.UI.get_center_frame()
		self.backup = self.UI.get_backup_frame()
		self.message = self.UI.get_message_frame()