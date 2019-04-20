from tkinter import *
from tkinter import ttk
from User import User
import datetime


class date_entry:
    def __init__(self,frame,rowpos,colpos,colspan):
        self.var = StringVar()
        self.var.trace('w',self.validate_length)
        self.Entry = ttk.Entry(frame,width=11,textvariable=self.var)
        self.Entry.insert(0,'MM/DD/YY')
        self.Entry.grid(row=rowpos,column=colpos,columnspan=colspan)
        self.Entry.bind('<FocusIn>',self.reservation_entry)
        self.Entry.bind('<FocusOut>',self.reservation_leave)
    def validate_length(self, *args):
        temp = self.var.get()
        if len(temp) > 8:
            self.var.set(temp[:10])
        
    def reservation_entry(self, event):
        if self.Entry.get() == 'MM/DD/YY':
            self.Entry.delete(0,"end")
            self.Entry.insert(0,'')
    def reservation_leave(self,event):
        if self.Entry.get() == '':
            self.Entry.delete(0,"end")
            self.Entry.insert(0,'MM/DD/YY')

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
        self.sDate = date_entry(self.center,1,0,3)
        self.eDate = date_entry(self.center,1,4,3)
        ttk.Label(self.center, text="Start date").grid(column=0,row=0,columnspan=3)
        ttk.Label(self.center, text="End date").grid(padx=30,column=4,row=0,columnspan=3)
        ttk.Button(self.center,text="Search", command=self.validate_dates).grid(row=3,column=2,columnspan = 3,pady=15)

    # ____________________SERVICES____________________
    def services_press(self):
        self.clear_frames()
        ttk.Button(self.center, text="Food Service", command=self.food_service_press).grid()
        ttk.Button(self.center, text="Room Maintenance", command=self.room_maintenance_press).grid()
        

    def food_service_press(self):
        self.clear_frames()

    def room_maintenance_press(self):
        self.clear_frames()

    # ____________________OTHER____________________
    def clear_frames(self):
        self.UI.clear_center()
        self.center = self.UI.get_center_frame()
        self.backup = self.UI.get_backup_frame()
        self.message = self.UI.get_message_frame()
    
    #Validates date entry fields to check for
    # -Valid date
    # -Dates given are within one year of present date
    # -Dates given are later than present date
    def validate_dates(self):
        print("Verifying dates")
        try:
            startDate = datetime.datetime.strptime(str(self.sDate.Entry.get()),'%m/%d/%y')
            endDate = datetime.datetime.strptime(str(self.eDate.Entry.get()),'%m/%d/%y')
        except:
            self.UI.display_message_frame("Date is incorrectly formatted")
            return False
        today = datetime.date.today()
        today = datetime.datetime(today.year,today.month,today.day)
        print("Present:\t"+ str(today))
        print("Start:\t"+ str(startDate))
        print("End:\t"+ str(endDate))
        if startDate < today or startDate > endDate or endDate.year > today.year+1:
            self.UI.display_message_frame("Date is incorrectly formatted")
            return False