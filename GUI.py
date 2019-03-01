from tkinter import *
from tkinter import ttk

class OceanLuxuryHome:
    def __init__(self, master):
        self.banner = ttk.Label(master, text="Ocean Luxury Banner")
        self.button_frame = ttk.Frame(master, relief=RAISED)
        self.parent_frame = ttk.Frame(master, relief=SUNKEN)
        self.center_frame = ttk.Frame(self.parent_frame)
        self.banner.grid(column=0, row=0, columnspan=2, sticky=W)
        self.button_frame.grid(column=0, row=1, sticky=W)
        self.parent_frame.grid(column=1, row=1)
        self.center_frame.grid()
        self.banner_img = PhotoImage(file='OL-Assets/OceanLuxuryBanner.png')
        self.banner.config(image=self.banner_img)

        self.hb_img = PhotoImage(file='OL-Assets/home.png')
        self.aub_img = PhotoImage(file='OL-Assets/aboutus.png')
        self.lb_img = PhotoImage(file='OL-Assets/login.png')
        self.sub_img = PhotoImage(file='OL-Assets/signup.png')
        self.bb_img = PhotoImage(file='OL-Assets/booking.png')
        self.sb_img = PhotoImage(file='OL-Assets/services.png')

        self.home = ttk.Button(self.button_frame, text="Home", command=self.home_press, image=self.hb_img, width=400)
        self.aboutus = ttk.Button(self.button_frame, text="Home", command=self.aboutus_press, image=self.aub_img)
        self.login = ttk.Button(self.button_frame, text="Log-in", command=self.login_press, image=self.lb_img)
        self.signup = ttk.Button(self.button_frame, text="Sign Up", command=self.signup_press, image=self.sub_img)
        self.booking = ttk.Button(self.button_frame, text="Booking", command=self.booking_press, image=self.bb_img)
        self.services = ttk.Button(self.button_frame, text="Services", command=self.service_press, image=self.sb_img)
        self.home.grid(column=0, row=1)
        self.aboutus.grid(column=0, row=4)
        self.login.grid(column=0, row=5)
        self.signup.grid(column=0, row=6)
        self.booking.grid(column=0, row=2)
        self.services.grid(column=0, row=3)

        self.home_press()

    def clear_center(self):
        self.center_frame.destroy()
        self.center_frame = ttk.Frame(self.parent_frame)
        self.center_frame.grid()

    def home_press(self):
        self.clear_center()
        self.home_banner = ttk.Label(self.center_frame, text="Welcome to Ocean Luxury").grid(column=0, row=0)
        print('Home pressed')

    def aboutus_press(self):
        self.clear_center()
        self.info = ttk.Label(self.center_frame, text="About US\n...").grid(column=0, row=0)
        print('About Us pressed')

    def login_press(self):
        self.clear_center()
        self.username = ttk.Label(self.center_frame, text="Username ").grid(column=0, row=0)
        self.password = ttk.Label(self.center_frame, text="Password ").grid(column=0, row=1)
        self.un_entry = ttk.Entry(self.center_frame).grid(column=1, row=0)
        self.pw_entry = ttk.Entry(self.center_frame).grid(column=1, row=1)
        self.login_confirm = ttk.Button(self.center_frame, text="Log-in").grid(column=0, row=2, columnspan=2)
        print('Log-in pressed')

    def signup_press(self):
        self.clear_center()
        self.username = ttk.Label(self.center_frame, text="Username ").grid(column=0, row=0)
        self.password = ttk.Label(self.center_frame, text="Password ").grid(column=0, row=1)
        self.fname = ttk.Label(self.center_frame, text="First Name ").grid(column=0, row=2)
        self.lname = ttk.Label(self.center_frame, text="Last Name ").grid(column=0, row=3)
        self.un_entry = ttk.Entry(self.center_frame).grid(column=1, row=0)
        self.pw_entry = ttk.Entry(self.center_frame).grid(column=1, row=1)
        self.fn_entry = ttk.Entry(self.center_frame).grid(column=1, row=2)
        self.ln_entry = ttk.Entry(self.center_frame).grid(column=1, row=3)
        self.login_confirm = ttk.Button(self.center_frame, text="Register").grid(column=0, row=4, columnspan=2)
        print('Sign Up pressed')

    def booking_press(self):
        self.clear_center()
        self.date = ttk.Label(self.center_frame, text="Date ").grid(column=0, row=0)
        self.un_entry = ttk.Entry(self.center_frame, width=2).grid(column=1, row=0)
        self.date = ttk.Label(self.center_frame, text="/").grid(column=2, row=0)
        self.un_entry = ttk.Entry(self.center_frame, width=2).grid(column=3, row=0)
        self.date = ttk.Label(self.center_frame, text="/").grid(column=4, row=0)
        self.un_entry = ttk.Entry(self.center_frame, width=2).grid(column=5, row=0)
        self.search = ttk.Button(self.center_frame, text="Search").grid(column=0, row=4, columnspan=6)
        print('Booking pressed')

    def service_press(self):
        self.clear_center()
        self.food = ttk.Button(self.center_frame, text="Food Kiosk").grid(column=0, row=0, ipadx=30, ipady=70)
        self.room_service = ttk.Button(self.center_frame, text="Room Service").grid(column=1, row=0, ipadx=30, ipady=70)
        print('Services pressed')


def main():
    root = Tk()
    app = OceanLuxuryHome(root)
    root.mainloop()


if __name__ == "__main__": main()
