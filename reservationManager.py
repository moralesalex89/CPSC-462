from includes.DatabaseFunctions import *


class resManager:
	def check_reservations(self ,startTime,endTime):
		db_cursor = db.cursor()
		query = "SELECT room_id,room_type FROM Rooms Ro WHERE Ro.room_id NOT IN (SELECT room_id FROM Reservations WHERE ((startTime <= '%s') AND (endTime >= '%s')))" %(startTime,endTime)
		db_cursor.execute(query)
		return list(db_cursor)

	def check_guest_reservation(self, guest_username):
		user_info = retrieve_user(guest_username)
		if not user_info:
			return False
		query = "SELECT * FROM Reservations WHERE user_id = %d" % user_info['id']
		result = db_query(query).fetchone()
		if result is None:
			return False
		return result

	def create_reservation(self,startTime,endTime,userId,roomID):
		db_cursor = db.cursor()
		query = "INSERT INTO Reservations (startTime,EndTime,user_id,room_id) VALUES ('%s','%s','%d','%d')" % (startTime,endTime,userId,roomID)
		db_cursor.execute(query)
		db.commit()
		return True

	def cancel_reservation(self):
		pass

	def update_reservation(self,room_status,room_id):
		db_cursor = db.cursor()
		query = "UPDATE Rooms SET roomStatus = '%s' WHERE room_id = %d" % (room_status, room_id)
		db_cursor.execute(query)
		db.commit()
		return True