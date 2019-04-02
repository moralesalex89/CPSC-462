from tkinter import *
from tkinter import ttk
from User import User


class CustomerUI:
    def __init__(self, UI_Controller):
        self.UI = UI_Controller
        self.center = UI_Controller.get_center_frame()
        self.backup = UI_Controller.get_backup_frame()
        self.message = UI_Controller.get_message_frame()
        self.activeUser = UI_Controller.activeUser

    # ____________________HOME____________________
    def home_press(self):
        self.clear_frames()
        self.Label = ttk.Label(self.center, text="Hello World").grid()

    # ____________________ABOUT____________________
    def about_press(self):
        self.clear_frames()
        self.Label = ttk.Label(self.center, text="Hello World1").grid()

    # ____________________BOOKING____________________
    def booking_press(self):
        self.clear_frames()
        ttk.Label(self.center, text="Date : ").grid()
        self.month = ttk.Entry(self.center, )


    # ____________________SERVICES____________________
    def services_press(self):
        self.clear_frames()
        if self.activeUser.userType == -1:
            self.UI.display_message_frame("You must be logged in to use this feature")

        else:
            ttk.Button(self.center, text="Food Service", command=self.food_service_press).grid()
            ttk.Button(self.center, text="Room Maintenance", command=self.room_maintenance_press).grid()

    def food_service_press(self):
        return 1

    def room_maintenance_press(self):
        return 1

    # ____________________OTHER____________________
    def clear_frames(self):
        self.UI.clear_center()
        self.center = self.UI.get_center_frame()
        self.backup = self.UI.get_backup_frame()
        self.message = self.UI.get_message_frame()

    def backup_login(self):
        self.UI.display_backup_frame()
        self.priviledge = 0
        ttk.Label(self.backup, text="Username")
        ttk.Entry(self.backup)
        ttk.Label(self.backup, text="Password")

        ttk.Radiobutton(self.backup, text="Guest", variable=self.priviledge, value=0).grid()
        ttk.Radiobutton(self.backup, text="Employee", variable=self.priviledge, value=1).grid()
