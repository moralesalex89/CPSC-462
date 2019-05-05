from includes.DatabaseFunctions import *


def add_payment(user_id, charge, info):
    query = "INSERT INTO Payment (user_id, charge, info) VALUES(%d, %f, '%s')" % (user_id, charge, info)
    db_query(query)
    db.commit()


def get_payment_list(user_id):
    query = "SELECT * FROM Payment WHERE user_id = %d" % user_id
    result = db_query(query).fetchall()
    return result
