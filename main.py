from tkinter import *
from tkinter import ttk
from CustomerUI import CustomerUI
from OceanLuxuryGUI import OceanLuxuryGUI
from includes.DatabaseFunctions import db_query
from HKManager import *

def main():
    root = Tk()
    app = OceanLuxuryGUI(root)
    root.mainloop()


if __name__ == "__main__": main()