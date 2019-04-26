from includes.DatabaseFunctions import db_query


def fetchHousekeepingSlots(times):
    slots = []
    for i in range(28):
        query = "SELECT COUNT(hk_id) FROM Housekeeping WHERE time = '%s' AND room = NULL" % times[i]
        result = db_query(query).fetchone()
        slots.append(result)
    return slots


def addHousekeepingEntry(room_num, time):
    query = "SELECT hk_id FROM Housekeeping WHERE time = '%s' AND room = NULL" % time
    result = db_query(query).fetchone()
    if not result[0]:
        query = "UPDATE Housekeeping SET room = " + room_num + " WHERE hk_id = result"
        result = db_query(query).fetchone()
        return not result[0]
    else:
        return False

#def removeHousekeepingEntry(room, time):

#def clearHousekeeping():

#def initHousekeeping():