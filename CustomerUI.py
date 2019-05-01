from tkinter import *
from tkinter import ttk
from User import User
from HKManager import *


class CustomerUI:
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
        self.Label = ttk.Label(self.center, text="Hello World").grid()

    # ____________________ABOUT____________________
    def about_press(self):
        self.clear_frames()
        ttk.Label(self.center, text="You are in CustomerUI").grid()

    # ____________________BOOKING____________________
    def booking_press(self):
        self.clear_frames()

    # ____________________SERVICES____________________
    def services_press(self):
        self.clear_frames()
        ttk.Button(self.center, text="Food Service", command=self.food_service_press).grid()
        ttk.Button(self.center, text="Room Maintenance", command=self.room_maintenance_press).grid()

    def food_service_press(self):
        self.clear_frames()

    def room_maintenance_press(self):
        self.clear_frames()
        ttk.Label(self.center, text="Time").grid(column=0, row=0)
        ttk.Label(self.center, text="Open Slots").grid(column=1, row=0, columnspan=2)
        times = fetchTimes()
        timeSlots = fetchHousekeepingSlots()
        open_times = []

        for time_range in range(len(times)):
            ttk.Label(self.center, text=times[time_range]).grid(column=0, row=time_range+1)
            ttk.Label(self.center, text=timeSlots[time_range]).grid(column=1, row=time_range+1)
            if timeSlots[time_range] > 0:
                open_times.append(times[time_range])

        if len(open_times) > 0:
            option = StringVar(self.center)
            time_options = ttk.OptionMenu(self.center, option, open_times[0], *open_times).grid(column=0, row=len(times)+1, columnspan=3)
            ttk.Button(self.center, text="Request Housekeeping").grid(column=0, row=len(times)+2, columnspan=3)
        else:
            ttk.Label(self.center, text="All housekeeping hours are currently booked").grid(column=0, row=len(times)+1, columnspan=3)


    # ____________________OTHER____________________
    def clear_frames(self):
        self.UI.clear_center()
        self.center = self.UI.get_center_frame()
        self.backup = self.UI.get_backup_frame()
        self.message = self.UI.get_message_frame()