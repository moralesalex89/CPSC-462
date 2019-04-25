from includes.DatabaseConfig import db
class resManager:
    def checkReservations(startTime,endTime):
        db_cursor = db.cursor()
        query = "SELECT room_id,room_type FROM Rooms Ro WHERE Ro.room_id NOT IN (SELECT room_id FROM Reservations WHERE ((startTime >= '%s') OR (endTime >= '%s')))" %(startTime,endTime)
        db_cursor.execute(query)
        return list(db_cursor)

    def createReservation(startTime,endTime,userId,roomID):
        db_cursor = db.cursor()
        check = check_reservations(startTime,endTime)
        if check == None:
            return False
        query = "INSERT INTO Reservations (startTime,EndTime,user_id,room_id) VALUES ('%s','%s','%d','%d')" % (startTime,endTime,userId,roomID)
        db_cursor.execute(query)
        db.commit()
        return True

    def cancelReservation():
        pass

    def updateReservation():
        pass