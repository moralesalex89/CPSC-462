from includes.DatabaseFunctions import *

HK_PER_HOUR = 6

def fetch_times():
    times = ["08:00a", "08:30a", "09:00a", "09:30a", "10:00a", "10:30a", "11:00a", "11:30a", "12:00a", "12:30a", "01:00p", "01:30p", "02:00p", "02:30p", "03:00p", "03:30p", "04:00p", "04:30p", "05:00p"]
    return times


def fetch_housekeeping_slots():
    times = fetch_times()
    slots = []
    for time in times:
        query = "SELECT COUNT(*) FROM Housekeeping WHERE startTime = '%s' AND room_id is NULL" % time
        result = db_query(query).fetchone()
        if result is None:
            slots.append(0)
        else:
            slots.append(result[0])
    return slots


def add_housekeeping_entry(room_num, time):
    query = "SELECT hk_id FROM Housekeeping WHERE startTime = '%s' AND room_id is NULL" % time
    result = db_query(query).fetchone()
    if result is None:
        return False
    else:
        query = "UPDATE Housekeeping SET room_id = %d WHERE (hk_id = %d AND room_id is NULL)" % (room_num, result[0])
        db_query(query)
        query = "UPDATE Housekeeping SET room_id = NULL WHERE (hk_id != %d and room_id = %d)" % (result[0], room_num)
        db_query(query)
        db.commit()
        return True


def remove_housekeeping_entry(room_num):
    query = "UPDATE Housekeeping SET room_id = NULL WHERE room_id = %d" % room_num
    db_query(query)
    db.commit()


def clear_housekeeping():
    times = fetch_times()

    for time_slot in times:
        for entry_num in range(HK_PER_HOUR):
            query = "UPDATE Housekeeping (room_id) VALUES (NULL)"
            db_query(query)
            db.commit()


def get_my_entry(room_id):
    query = "SELECT startTime FROM Housekeeping WHERE room_id = %d" % room_id
    result = db_query(query).fetchone()
    if result is not None:
        return result
    else:
        return False


def get_slot_entries(time):
    query = "SELECT room_id FROM Housekeeping WHERE startTime = '%s' AND room_id is not NULL" % time
    result = db_query(query).fetchall()
    if result is not None:
        return result
    else:
        return False