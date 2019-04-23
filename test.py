from includes.DatabaseFunctions import db_query,create_reservation,check_reservations
var = check_reservations('2019-05-22','2019-05-23')
#create_reservation('2019-05-22','2019-05-23',11,6)
#var = db_query("SELECT * FROM Reservations")
print(var)
for x in var:
    print(x)
    for y in x:
        pass
        #print(y)

#var2 = db_query("describe Rooms")
#print(var2)