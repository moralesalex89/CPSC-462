from tkinter import *
from tkinter import ttk
from User import User
from HKManager import *
from RoomManager import *
from PaymentManager import *

class FrontDeskUI:
    def __init__(self, UI_Controller):
        self.UI = UI_Controller
        self.defont = UI_Controller.defont
        self.center = UI_Controller.get_center_frame()
        self.backup = UI_Controller.get_backup_frame()
        self.message = UI_Controller.get_message_frame()
        self.activeUser = UI_Controller.activeUser

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

    def reset_maintenance_press(self):
        self.clear_frames()
        ttk.Label(self.center, font=self.defont, text="WARNING").grid()
        ttk.Label(self.center, font=self.defont, text="Housekeeping entries are only to be cleared after all requests are cleared for the day").grid()
        ttk.Label(self.center, font=self.defont, text="Please re-enter your password to confirm a housekeeping reset").grid()
        password = ttk.Entry(self.center, font=self.defont)
        password.grid()
        ttk.Button(self.center, text="Clear Housekeeping", command=lambda: self.clear_hk(password.get())).grid()

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

#   __________ACCOUNT__________

    def account_press(self):
        self.clear_frames()
        ttk.Button(self.center, text="Account Information", command=lambda: self.account_info()).grid()
        ttk.Button(self.center, text="Review Transactions", command=lambda: self.display_transactions()).grid()

    def account_info(self):
        self.clear_frames()
        #Can someone who used the User class more than me do this one please
        #Employees maybe will not need to edit CC info like Guests but should be able to change their password

    def dispute_transaction(self, p_id):
        headers = ["Payment ID", "User ID", "Charge", "Info"]
        self.UI.display_headers(headers, 0)
        result = search_transaction(p_id)
        if result is None:
            self.UI.display_message_frame("Transaction not found in search")
            self.display_transactions()
        else:
            entry = ['%s' % result[0], '%s' % result[1], '%s' % result[2], '%s' % result[3]]
            self.UI.display_headers(entry, 1)

        if clear_transaction(p_id):
            self.UI.display_message_frame("Transaction cleared successfully")
        else:
            self.UI.display_message_frame("Transaction clear failed")
        self.display_transactions()

    def display_transactions(self):
        self.clear_frames()
        p_id = self.UI.make_form(self.center, "Payment ID: ")
        ttk.Button(text="Clear Entry", command=self.dispute_transaction(p_id.get()))

    # ____________________OTHER____________________
    def clear_frames(self):
        self.UI.clear_center()
        self.center = self.UI.get_center_frame()
        self.backup = self.UI.get_backup_frame()
        self.message = self.UI.get_message_frame()