from tkinter import *
from tkinter import ttk


class User:
    def __init__(self, u_id, u_type, u_name):
        self.userID = u_id
        self.userType = u_type
        self.username = u_name

    def get_userID(self):
        return self.userID

    def get_userType(self):
        return self.userType

    def get_username(self):
        return self.username
