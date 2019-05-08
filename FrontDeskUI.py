from tkinter import *
from tkinter import ttk
from User import User
from HKManager import *
from RoomManager import *
from reservationManager import resManager
from InventoryManager import InventoryManager
from includes.DatabaseFunctions import *
from PaymentManager import *

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
        self.invManager = InventoryManager()

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
        ttk.Button(self.center, text="Room Maintenance", command=self.room_maintenance_press).grid()
        ttk.Button(self.center, text="Reset Maintenance Schedule", command=self.reset_maintenance_press).grid()
        ttk.Button(self.center, text="Guest Services", command=self.guest_service_press).grid()
        ttk.Button(self.center, text="Food Services", command=lambda: self.food_service_press()).grid()

    def reset_maintenance_press(self):
        self.clear_frames()
        ttk.Label(self.center, font=self.defont, text="WARNING").grid()
        ttk.Label(self.center, font=self.defont, text="Housekeeping entries are only to be cleared after all requests are cleared for the day").grid()
        ttk.Label(self.center, font=self.defont, text="Please re-enter your password to confirm a housekeeping reset").grid()
        password = ttk.Entry(self.center, font=self.defont)
        password.grid()
        ttk.Button(self.center, text="Clear Housekeeping", command=lambda: self.clear_hk(password.get())).grid()

    def food_service_press(self):
        self.clear_frames()
        ttk.Button(self.center, text="Restock Food Inventory", command=lambda: self.invManager.restock_items()).grid()
        ttk.Button(self.center, text="View Food Inventory", command=lambda: self.invManager.view_inventory()).grid()

    def clear_hk(self, password):
        #if password is correct, filler code used here for testing
        if password == "correct":
            clearHousekeeping()
        self.room_maintenance_press()
        self.UI.display_message_frame("Housekeeping entries successfully cleared!")

    def add_hk(self, room_num, time):
        if addHousekeepingEntry(int(room_num), time):
            self.room_maintenance_press()
            self.UI.display_message_frame("Housekeeping scheduled successfully")
        else:
            self.room_maintenance_press()
            self.UI.display_message_frame("Housekeeping scheduling failed")

    def room_maintenance_press(self):
        self.clear_frames()
        ttk.Label(self.center, font=self.defont, text="Time").grid(column=0, row=0)
        ttk.Label(self.center, font=self.defont, text="Open Slots").grid(column=1, row=0)
        times = fetchTimes()
        timeSlots = fetchHousekeepingSlots()
        open_times = []
        open_rooms = getOpenRooms()
        len_times = len(times)

        for time_range in range(len_times):
            ttk.Label(self.center, font=self.defont, text=times[time_range]).grid(column=0, row=time_range+1)
            ttk.Label(self.center, font=self.defont, text=timeSlots[time_range]).grid(column=1, row=time_range+1)
            if timeSlots[time_range] > 0:
                open_times.append(times[time_range])

        if len(open_times) > 0:
            option = StringVar(self.center)
            room_num = StringVar(self.center)
            ttk.Label(self.center, font = self.defont, text="Room: ").grid(column=0, row=len_times+1)
            ttk.OptionMenu(self.center, room_num, open_rooms[0], *open_rooms).grid(column=1, row = len_times+1)
            ttk.Label(self.center, font=self.defont, text="Time: ").grid(column=0, row=len_times+2)
            ttk.OptionMenu(self.center, option, open_times[0], *open_times).grid(column=1, row=len_times+2)
            ttk.Button(self.center, text="Schedule Housekeeping", command=lambda: self.add_hk(room_num.get(), option.get())).grid(column=0, row=len_times+3, columnspan=2)
        else:
            ttk.Label(self.center, font=self.defont, text="All housekeeping hours are currently booked").grid(column=0, row=len_times+1, columnspan=2)

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

    #__________ACCOUNT__________
    def account_press(self):
        self.clear_frames()
        ttk.Button(self.center, text="Account Information", command=lambda: self.account_info()).grid()
        ttk.Button(self.center, text="Review Transactions", command=lambda: self.display_transactions()).grid()

    def account_info(self):
        self.clear_frames()
        ttk.Label(self.center, text="Username: %s" % self.activeUser.get_username()).grid(column=0, row=0)
        ttk.Button(self.center, text="Change Password", command=lambda: self.change_password_press()).grid(column=0, row=1, columnspan=2)
        ttk.Button(self.center, text="Go Back", command=lambda: self.account_press()).grid()

    def change_password_press(self):
        self.clear_frames()
        password = self.UI.make_form(self.center, "Enter New Password: ", 0, 1)
        pass_check = self.UI.make_form(self.center, "Re-enter New Password: ", 0, 2)
        ttk.Button(self.center, text="Change Password", command=lambda: self.pass_change_validate(password.get(), pass_check.get())).grid(columnspan=2)
        ttk.Button(self.center, text="Go Back", command=lambda: self.account_info()).grid(columnspan=2)

    def pass_change_validate(self, password, pass_check):
        error = ""
        if password == "":
            error = error + " - No password entry\n"
        else:
            if password != pass_check:
                error = error + " - Passwords do not match\n"
        if error is "":
            update_user_password(self.activeUser.get_userID(), password)
            self.UI.logoutUser()
            self.UI.display_message_frame("Password has been changed successfully!\nYou will now be logged out.")
        if error != "":
            self.UI.display_message_frame(error)

    def dispute_transaction(self, p_id):
        self.clear_frames()
        headers = ["Payment ID", "User ID", "Charge", "Info"]
        self.UI.display_headers(headers, 0)

        try:
            int(p_id)
        except ValueError:
            self.display_transactions()
            self.UI.display_message_frame("Invalid entry")
            return

        pid = int(p_id)
        result = search_transaction(pid)

        if result is None:
            self.display_transactions()
            self.UI.display_message_frame("Transaction not found in search")
            return

        else:
            entry = ['%s' % result[0], '%s' % result[1], '$%s' % result[2], '%s' % result[3]]
            self.UI.display_headers(entry, 1)
            ttk.Button(self.center, text="Clear Entry", command=lambda: self.clear_trans(pid)).grid(columnspan=4)

    def clear_trans(self, p_id):
        self.clear_frames()
        clear_transaction(p_id)
        self.display_transactions()
        self.UI.display_message_frame("Transaction cleared successfully")

    def display_transactions(self):
        self.clear_frames()
        p_id = self.UI.make_form(self.center, "Payment ID: ", 0, 0)
        ttk.Button(self.center, text="Search", command=lambda: self.dispute_transaction(p_id.get())).grid(column=0, row=1, columnspan=3)

    # ____________________OTHER____________________
    def clear_frames(self):
        self.UI.clear_center()
        self.center = self.UI.get_center_frame()
        self.backup = self.UI.get_backup_frame()
        self.message = self.UI.get_message_frame()