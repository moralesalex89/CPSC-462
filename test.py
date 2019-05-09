from includes.DatabaseFunctions import *

#('room_id', 'int(11)', 'NO', 'PRI', None, 'auto_increment')
#('room_type', 'varchar(255)', 'NO', '', None, '')
#('roomStatus', "enum('Empty','Reserved')", 'NO', '', None, '')
x = db_query("describe Reservations")

for p in x:
    print (p)