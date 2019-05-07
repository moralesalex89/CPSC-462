from tkinter import *
from tkinter import ttk
from User import User
from reservationManager import resManager
from InventoryManager import InventoryManager
import datetime
from HKManager import *
from RoomManager import *
from PaymentManager import *

#Creates entry field to recieve valid dates
class dateEntry:
    prev = ''

    def __init__(self,frame,rowpos,colpos,colspan,text=''):
        self.var = StringVar()
        self.var.trace('w',self.validate_length)
        self.Entry = ttk.Entry(frame,width=11,textvariable=self.var)
        self.Entry.insert(0,text)
        if text == '':
            self.Entry.insert(0,'MM/DD/YY')
        self.Entry.grid(row=rowpos,column=colpos,columnspan=colspan)
        self.Entry.bind('<FocusIn>',self.reservation_entry)
        self.Entry.bind('<FocusOut>',self.reservation_leave)
        self.prev = text

    def validate_length(self, *args):
        maxsize = 8
        temp = self.var.get()
        if len(temp) > maxsize:
            self.var.set(temp[:maxsize])
        if len(temp) < len(self.prev):
            if len(temp) == 2 or len(temp) == 5:
                self.var.set(temp[:len(self.prev)-2])
        elif len(temp) == 2 or len(temp) == 5:
            self.Entry.insert(INSERT,'/')
            self.Entry.icursor("end")
        self.prev = self.var.get()

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
        self.resMan = resManager
        self.invMan = InventoryManager
        self.img_2bed = PhotoImage(file='OL-Assets/2queen.png')
        self.img_1bed = PhotoImage(file='OL-Assets/1queen.png')
        self.img_suite = PhotoImage(file='OL-Assets/suite.png')
        # Snack Images, chose 10 snacks
        self.img_cheetos = PhotoImage(file='OL-Assets/cheetos.png')
        self.img_famous_amos = PhotoImage(file='OL-Assets/famous_amos.png')
        self.img_fritos = PhotoImage(file='OL-Assets/fritos.png')
        self.img_lays = PhotoImage(file='OL-Assets/lays.png')
        self.img_mnm = PhotoImage(file='OL-Assets/mnm.png')
        self.img_oreos = PhotoImage(file='OL-Assets/oreos.png')
        self.img_pop_tarts = PhotoImage(file='OL-Assets/pop_tarts.png')
        self.img_reeses = PhotoImage(file='OL-Assets/reeses.png')
        self.img_rice_krispies = PhotoImage(file='OL-Assets/rice_krispies.png')
        self.img_trail_mix = PhotoImage(file='OL-Assets/trail_mix.png')

    # ____________________HOME____________________
    def home_press(self):
        self.clear_frames()
        ttk.Label(self.center, text="Hello World").grid()

    # ____________________ABOUT____________________
    def about_press(self):
        self.clear_frames()
        ttk.Label(self.center, text="You are in CustomerUI").grid()

    # ____________________BOOKING____________________
    # Success Path
    # booking_press() -> validate_dates() -> room_selection() -> validate_reservation() -> pay_pop() -> reserve()

    # Displays msg if not logged in, returns
    # If reservation -> Display summary of reservation
    # else -> Two date entry fields with search button
    #   search -> self.validate_dates
    def booking_press(self):
        self.clear_frames()
        if self.activeUser.get_userID() == -1:
            ttk.Label(self.center,text="Please log in to reserve a room",font=('Arial',24)).grid()
            return
        reserve = self.activeUser.get_reservation()
        if reserve:
            msg = "Reserved: %s\nFrom:%s\nTo: %s\n" % (reserve[5],reserve[1],reserve[2])
            ttk.Label(self.center,text=msg,font=('Arial',24)).grid()
        else:
            font = ('Yu Gothic UI Semibold',12)
            ttk.Label(self.center,font=font, text="Start date").grid(column=1,row=0,columnspan=1)
            ttk.Label(self.center,font=font, text="End date").grid(column=2,row=0,columnspan=1)
            self.s_date = dateEntry(self.center,rowpos=1,colpos=1,colspan=1)
            self.e_date = dateEntry(self.center,rowpos=1,colpos=2,colspan=1)
            ttk.Button(self.center,text="Search",command=self.validate_dates,width=10).grid(row=2,column=1,columnspan=2,pady=5)

    #Validates date entry fields to check for
    # -Valid date
    # -Dates given are within one year of present date
    # -Dates given are later than present date
    # -Start date is before or equal to End date
    #If valid -> self.room_selection()
    def validate_dates(self):
        try:
            start_date = datetime.datetime.strptime(str(self.s_date.Entry.get()),'%m/%d/%y')
            end_date = datetime.datetime.strptime(str(self.e_date.Entry.get()),'%m/%d/%y')
        except:
            self.UI.display_message_frame("Date is incorrectly formatted")
            return False
        today = datetime.date.today()
        today = datetime.datetime(today.year,today.month,today.day)
        if start_date < today or start_date > end_date or end_date.year > today.year+1:
            self.UI.display_message_frame("Date is incorrectly formatted")
            return False
        available_rooms = self.resMan.check_reservations(self.resMan,start_date,end_date)
        self.room_selection(available_rooms,start_date,end_date)
    
    #Displays available room_types in series of radio buttons
    # Will assign radio button to room information by looping through available rooms
    # Has two buttons Reserve and Cancel
    #  Reserve -> self.validate_reservation()
    #  Cancel -> self.booking_press()
    def room_selection(self,available_rooms,start_date,end_date):
        self.clear_frames()
        ttk.Label(self.center, text="Start date").grid(column=2,row=0,columnspan=1)
        ttk.Label(self.center, text="End date").grid(column=3,row=0,columnspan=1)
        self.s_date = dateEntry(self.center,rowpos=1,colpos=2,colspan=1,text=self.s_date.prev)
        self.e_date = dateEntry(self.center,rowpos=1,colpos=3,colspan=1,text=self.e_date.prev)
        ttk.Button(self.center,text="Search", command=self.validate_dates,width=10).grid(row=2,column=2,columnspan=2,pady=5)
        font = ('Yu Gothic UI Semibold',12)
        self.room_select = IntVar()
        self.room_select.set(-1)
        self.single = self.double = self.suite = False
        for room in available_rooms:
            if 'single' in room:
                self.single = room
            if 'double' in room:
                self.double = room
            if 'suite' in room:
                self.suite = room
        if self.single:
            ttk.Radiobutton(self.center,variable=self.room_select,value = 1,image=self.img_1bed).grid(row=4,column=0,columnspan=4)
            ttk.Label(self.center,text="$359.20/night",font=font).grid(row=4,column=4)
        if self.double:
            ttk.Radiobutton(self.center,variable=self.room_select,value = 2,image=self.img_2bed).grid(row=5,column=0,columnspan=4)
            ttk.Label(self.center,text="$383.20/night",font=font).grid(row=5,column=4)
        if self.suite:
            ttk.Radiobutton(self.center,variable=self.room_select,value = 3,image=self.img_suite).grid(row=6,column=0,columnspan=4)
            ttk.Label(self.center,text="$849.00/night",font=font).grid(row=6,column=4)
        ttk.Button(self.center,text="Reserve",command= lambda:self.validate_reservation(start_date,end_date),width=10).grid(row=7,column=2,columnspan=1)
        ttk.Button(self.center,text="Cancel",command=self.booking_press,width=10).grid(row=7,column=3,columnspan=1)
    
    #Validates room selection from radio buttons
    # -Must have one of the room_types selected
    # On success -> self.pay_pop()
    def validate_reservation(self,start_date,end_date):
        choice = self.room_select.get()
        room_id = -1
        if choice == -1:
            self.UI.display_message_frame("No room type selected")
            return
        elif choice == 1:
            room_id = self.single[0]
            room_type = self.single[1]
            price = 359.20
        elif choice == 2:
            room_id = self.double[0]
            room_type = self.double[1]
            price = 383.20
        elif choice == 3:
            room_id = self.suite[0]
            room_type = self.suite[1]
            price = 849.00
        self.pay_pop(start_date,end_date,room_id,room_type,price)

    #Popup frame that will give summary of purchase with two buttons
    # Pay -> self.reserve()
    # Cancel -> Destroys popup
    def pay_pop(self,start_date,end_date,room_id,room_type,price):
        self.pop = Toplevel()
        self.pop.title("Pay for your reservation")
        msg = "Reserve: %s\nFrom:%s\nTo: %s\nFor: $%s/night" % (room_type,start_date,end_date,price)
        ttk.Label(self.pop,text=msg).grid(row=0,column=1)
        ttk.Button(self.pop,text="Pay",command=lambda:self.reserve(start_date,end_date,room_id)).grid(row=1,column=0,padx=20,columnspan=2)
        ttk.Button(self.pop,text="Cancel",command=self.pop.destroy).grid(row=1,column=2)
    
    #Reserves room described by pay_pop summary and calls reservationManager class
    # if Room was not available when pressed it will prompt user there was an error
    def reserve(self,start_date,end_date,room_id):
        if self.resMan.create_reservation(self.resMan,start_date,end_date,self.activeUser.get_userID(),room_id) == True:
            self.booking_press()
            self.UI.display_message_frame("Reservation made for %s - %s" % (start_date,end_date))
            self.activeUser.login_user(self.activeUser.get_username())
            self.pop.destroy()
        else:
            self.UI.display_message_frame("Room Taken")
            self.pop.destroy()
        
    # ____________________SERVICES____________________
    def services_press(self):
        self.clear_frames()
        ttk.Button(self.center, text="Food Service", command=self.food_service_press).grid()
        ttk.Button(self.center, text="Room Maintenance", command=self.room_maintenance_press).grid()

    def food_service_press(self):
        self.clear_frames()

        ttk.Label(self.center, text="Item").grid(column=3, row=0, columnspan=1)
        ttk.Label(self.center, text="Price").grid(column=5, row=0, columnspan=1)
        ttk.Label(self.center, text="Item").grid(column=11, row=0, columnspan=1)
        ttk.Label(self.center, text="Price").grid(column=13, row=0, columnspan=1)

        # snack_list is list of (name, price) tuples
        self.snack_list = self.invMan.check_stock(self.invMan)
        self.snack_list_len = len(self.snack_list)

        for snack in range(self.snack_list_len):

            # Parse the query for the name and price
            snack_name = self.snack_list[snack][0]
            snack_price = self.snack_list[snack][1]
            # print(str(snack) + " " + str(self.snack_list[snack][0]) + " " + str(self.snack_list[snack][1]))
            # print(self.snack_list[snack][0])
            # print(self.snack_list[snack][1])

            if snack < 5:
                displaycol = 1
                displayrow = snack + 1
            elif 5 <= snack <= 10:
                displaycol = 9
                displayrow = snack - 4

            # Display the correct image and button
            # 1st Column, 1 3 5 7 ----  9 11 13 15.
            if snack_name == 'Cheetos':
                ttk.Label(self.center, image=self.img_cheetos).grid(column=displaycol, row=displayrow, columnspan=1)
                ttk.Button(self.center, text="Purchase", command=lambda: self.invMan.buy_item(self=self.invMan, food_name='Cheetos'), width=10).grid(row=displayrow, column=displaycol + 6, columnspan=1, pady=5)
            elif snack_name == 'Famous Amos':
                ttk.Label(self.center, image=self.img_famous_amos).grid(column=displaycol, row=displayrow, columnspan=1)
                ttk.Button(self.center, text="Purchase",
                           command=lambda: self.invMan.buy_item(self=self.invMan, food_name='Famous Amos'), width=10).grid(
                    row=displayrow, column=displaycol + 6, columnspan=1, pady=5, padx=15)
            elif snack_name == 'Fritos':
                ttk.Label(self.center, image=self.img_fritos).grid(column=displaycol, row=displayrow, columnspan=1)
                ttk.Button(self.center, text="Purchase",
                           command=lambda: self.invMan.buy_item(self=self.invMan, food_name='Fritos'), width=10).grid(
                    row=displayrow, column=displaycol + 6, columnspan=1, pady=5, padx=15)
            elif snack_name == 'Lays':
                ttk.Label(self.center, image=self.img_lays).grid(column=displaycol, row=displayrow, columnspan=1)
                ttk.Button(self.center, text="Purchase",
                           command=lambda: self.invMan.buy_item(self=self.invMan, food_name='Lays'), width=10).grid(
                    row=displayrow, column=displaycol + 6, columnspan=1, pady=5, padx=15)
            elif snack_name == 'M&Ms':
                ttk.Label(self.center, image=self.img_mnm).grid(column=displaycol, row=displayrow, columnspan=1)
                ttk.Button(self.center, text="Purchase",
                           command=lambda: self.invMan.buy_item(self=self.invMan, food_name='M&Ms'), width=10).grid(
                    row=displayrow, column=displaycol + 6, columnspan=1, pady=5, padx=15)

            # 2nd Column, 1 3 5 7 ----  9 11 13 15.
            elif snack_name == 'Oreos':
                ttk.Label(self.center, image=self.img_oreos).grid(column=displaycol, row=displayrow, columnspan=1)
                ttk.Button(self.center, text="Purchase",
                           command=lambda: self.invMan.buy_item(self=self.invMan, food_name='Oreos'), width=10).grid(
                    row=displayrow, column=displaycol + 6, columnspan=1, pady=5)
            elif snack_name == 'Pop Tarts':
                ttk.Label(self.center, image=self.img_pop_tarts).grid(column=displaycol, row=displayrow, columnspan=1)
                ttk.Button(self.center, text="Purchase",
                           command=lambda: self.invMan.buy_item(self=self.invMan, food_name='Pop Tarts'), width=10).grid(
                    row=displayrow, column=displaycol + 6, columnspan=1, pady=5)
            elif snack_name == 'Reeses':
                ttk.Label(self.center, image=self.img_reeses).grid(column=displaycol, row=displayrow, columnspan=1)
                ttk.Button(self.center, text="Purchase",
                           command=lambda: self.invMan.buy_item(self=self.invMan, food_name='Reeses'), width=10).grid(
                    row=displayrow, column=displaycol + 6, columnspan=1, pady=5)
            elif snack_name == 'Rice Krispies':
                ttk.Label(self.center, image=self.img_rice_krispies).grid(column=displaycol, row=displayrow, columnspan=1)
                ttk.Button(self.center, text="Purchase",
                           command=lambda: self.invMan.buy_item(self=self.invMan, food_name='Rice Krispies'), width=10).grid(
                    row=displayrow, column=displaycol + 6, columnspan=1, pady=5)
            elif snack_name == 'Trail Mix':
                ttk.Label(self.center, image=self.img_trail_mix).grid(column=displaycol, row=displayrow, columnspan=1)
                ttk.Button(self.center, text="Purchase",
                           command=lambda: self.invMan.buy_item(self=self.invMan, food_name='Trail Mix'), width=10).grid(
                    row=displayrow, column=displaycol + 6, columnspan=1, pady=5)

            # Display the name and price
            ttk.Label(self.center, text=snack_name).grid(column=displaycol + 2, row=displayrow, columnspan=1)
            ttk.Label(self.center, text=snack_price).grid(column=displaycol + 4, row=displayrow, columnspan=1)



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
        len_times = len(times)

        for time_range in range(len_times):
            ttk.Label(self.center, font=self.defont, text=times[time_range]).grid(column=0, row=time_range+1)
            ttk.Label(self.center, font=self.defont, text=timeSlots[time_range]).grid(column=1, row=time_range+1)
            if timeSlots[time_range] > 0:
                open_times.append(times[time_range])

        if len(open_times) > 0:
            option = StringVar(self.center)
            ttk.Label(self.center, font=self.defont, text="Time: ").grid(column=0, row=len_times+1)
            time_options = ttk.OptionMenu(self.center, option, open_times[0], *open_times).grid(column=1, row=len_times+1)
            ttk.Button(self.center, text="Request Housekeeping", command=lambda: self.add_hk(getRoomID(self.activeUser), option.get())).grid(column=0, row=len_times+2, columnspan=2)
        else:
            ttk.Label(self.center, font=self.defont, text="All housekeeping hours are currently booked").grid(column=0, row=len_times+1, columnspan=2)

# ____________________ACCOUNT____________________
    def account_press(self):
        self.clear_frames()
        ttk.Button(self.center, text="Account Information", command=lambda: self.account_info()).grid()
        ttk.Button(self.center, text="Review Transactions", command=lambda: self.display_transactions()).grid()

    def account_info(self):
        self.clear_frames()
        #Can someone who used the User class more than me do this one please

    def display_transactions(self, result=None, page=0):
        self.clear_frames()
        if result is None:
            result = get_payment_list(self.activeUser.get_userID())
        if page >= 10:
            ttk.Button(self.center, text="<<", command=lambda: self.display_transactions(result, 0, page-10))
        if (len(result) - page) >= 10:
            ttk.Button(self.center, text=">>", command=lambda: self.display_transactions(result, 0, page+10))
        headers = ["Payment ID", "Charge", "Info"]
        self.UI.display_headers(headers, 0)
        for index in range(min(10, len(result) - page)):
            entry = ['%s' % result[index+page][0], '%s' % result[index+page][2], '%s' % result[index+page][3]]
            self.UI.display_headers(entry, index)

    # ____________________OTHER____________________
    def clear_frames(self):
        self.UI.clear_center()
        self.center = self.UI.get_center_frame()
        self.backup = self.UI.get_backup_frame()
        self.message = self.UI.get_message_frame()
