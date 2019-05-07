from includes.DatabaseFunctions import *


def add_payment(user_id, charge, info):
    query = "INSERT INTO Payments (user_id, charge, info) VALUES(%d, %f, '%s')" % (user_id, charge, info)
    db_query(query)
    db.commit()


def get_payment_list(user_id):
    query = "SELECT * FROM Payments WHERE user_id = %d" % user_id
    result = db_query(query).fetchall()
    return result


def search_transaction(payment_id):
    query = "SELECT * FROM Payments WHERE payment_id = %d" % payment_id
    result = db_query().fetchone()
    return result


def clear_transaction(payment_id):
    query = "UPDATE Payments SET charge = 0 WHERE payment_id = %d" % payment_id
    result = db_query(query).fetchone()
    db.commit()
    return result[0] is not None
