from tkinter import *
from tkinter import ttk
from OceanLuxuryGUI import OceanLuxuryGUI


class CustomerUI:
    def __init__(self, master):
        GUI = OceanLuxuryGUI(master)
        master.mainloop()

        self.user_name = ""
        self.user_id = ""
