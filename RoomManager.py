from includes.DatabaseFunctions import *


class RoomManager:
    def check_room_info(self, room_id):
        query = "SELECT * FROM Rooms WHERE room_id = %d" % room_id
        result = db_query(query).fetchone()
        if result is None:
            return False
        return result

    def getRooms(self):
        room_list = []
        query = "SELECT room_id FROM Rooms"
        result = db_query(query).fetchall()
        for room in result:
            room_list.append(room[0])
        return room_list

    def getOpenRooms(self):
        open_rooms = []
        query = "SELECT room_id FROM Rooms WHERE roomStatus = 1"
        result = db_query(query).fetchall()
        for room in result:
            open_rooms.append(room[0])
        return open_rooms

    def getRoomID(self, user_id):
        query = "SELECT room_id FROM Reservations WHERE user_id = '%s'" % user_id
        result = db_query(query).fetchone()
        if result is not None:
            return result[0]
        else:
            return False