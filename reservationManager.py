from includes.DatabaseFunctions import *


class resManager:

	def checkReservations(self, startTime, endTime):
		print('s:%s\te:%s' % (startTime, endTime))
		db_cursor = db.cursor()
		query = "SELECT room_id,room_type FROM Rooms Ro WHERE Ro.room_id NOT IN (SELECT room_id FROM Reservations WHERE ((startTime >= '%s') OR (endTime >= '%s')))" % (startTime, endTime)
		db_cursor.execute(query)
		return list(db_cursor)

	def checkGuestReservation(self, guest_username):
		user_info = retrieve_user(guest_username)
		if not user_info:
			return False
		query = "SELECT * FROM Reservations WHERE user_id = %d" % user_info['id']
		result = db_query(query).fetchone()
		if result is None:
			return False
		return result

	def checkRoomInfo(self, room_id):
		query = "SELECT * FROM Rooms WHERE room_id = %d" % room_id
		result = db_query(query).fetchone()
		if result is None:
			return False
		return result

	def createReservation(self,startTime,endTime,userId,roomID):
		db_cursor = db.cursor()

		query = "INSERT INTO Reservations (startTime,EndTime,user_id,room_id) VALUES ('%s','%s','%d','%d')" % (startTime, endTime, userId, roomID)
		db_cursor.execute(query)
		db.commit()
		return True

	def cancelReservation(self):
		pass

	def updateReservation(self, room_id, room_status):
		db_cursor = db.cursor()
		query = "UPDATE Rooms SET roomStatus = '%s' WHERE room_id = %d" % (room_status, room_id)
		db_cursor.execute(query)
		db.commit()
		return True
