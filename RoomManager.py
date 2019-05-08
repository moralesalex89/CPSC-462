from includes.DatabaseFunctions import *

def getRooms():
    room_list = []
    query = "SELECT room_id FROM Rooms"
    result = db_query(query).fetchall()
    for room in result:
        room_list.append(room[0])
    return room_list


def getOpenRooms():
    open_rooms = []
    query = "SELECT room_id FROM Rooms WHERE roomStatus = 1"
    result = db_query(query).fetchall()
    for room in result:
        open_rooms.append(room[0])
    return open_rooms


def getRoomID(user_id):
    query = "SELECT room_id FROM Reservations WHERE user_id = '%s'" % user_id
    result = db_query(query).fetchone()
    if result is not None:
        return result[0]
    else:
        return False