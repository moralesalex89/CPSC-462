from tkinter import *
from tkinter import ttk
from includes.DatabaseFunctions import get_id, get_reservation


class User:
    def __init__(self, u_id, u_type, u_name):
        self.userID = u_id
        self.userType = u_type
        self.username = u_name
    
    def login_user(self,u_name,u_type,u_id):
        self.userID = u_id
        self.userType = u_type
        self.username = u_name
        try:
            self.reservation = get_reservation(u_id)
        except:
            self.reservation = False

    def get_userID(self):
        return self.userID

    def get_userType(self):
        return self.userType

    def get_username(self):
        return self.username

    def get_reservation(self):
        return self.reservation
