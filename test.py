from includes.DatabaseFunctions import *

x = input("Name:")
id = get_id(x)
reservation = get_reservation(id)
print(reservation)