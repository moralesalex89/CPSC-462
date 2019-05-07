from includes.DatabaseConfig import db


class InventoryManager:

    def checkStock(self):
        db_cursor = db.cursor()
        query = "SELECT name, cost FROM Food_Inventory WHERE stock > 0"
        db_cursor.execute(query)

        result = list(db_cursor.fetchall())
        return result

    def buyItem(self, food_name):
        db_cursor = db.cursor()
        query = "UPDATE Food_Inventory SET  stock = stock - 1 WHERE name = %s"
        db_cursor.execute(query, food_name)
        db.commit()
        return True

    # Fill up the database with food to initialize it
    def stockItems(self):

        db_cursor = db.cursor()
        query1 = "INSERT IGNORE INTO Food_Inventory (food_id, name, cost, stock) VALUES (01, 'Cheetos', 1.50, 100)"
        query2 = "INSERT IGNORE INTO Food_Inventory (food_id, name, cost, stock) VALUES (02, 'Famous Amos', 1.25, 100)"
        query3 = "INSERT IGNORE INTO Food_Inventory (food_id, name, cost, stock) VALUES (03, 'Fritos', 1.00, 100)"
        query4 = "INSERT IGNORE INTO Food_Inventory (food_id, name, cost, stock) VALUES (04, 'Lays', 1.50, 100)"
        query5 = "INSERT IGNORE INTO Food_Inventory (food_id, name, cost, stock) VALUES (05, 'M&Ms', 1.00, 100)"
        query6 = "INSERT IGNORE INTO Food_Inventory (food_id, name, cost, stock) VALUES (06, 'Oreos', 1.25, 100)"
        query7 = "INSERT IGNORE INTO Food_Inventory (food_id, name, cost, stock) VALUES (07, 'Pop Tarts', 2.00, 100)"
        query8 = "INSERT IGNORE INTO Food_Inventory (food_id, name, cost, stock) VALUES (08, 'Reeses', 1.00, 100)"
        query9 = "INSERT IGNORE INTO Food_Inventory (food_id, name, cost, stock) " \
                 "VALUES (08, 'Rice Krispies', 1.00, 100)"
        query10 = "INSERT IGNORE INTO Food_Inventory (food_id, name, cost, stock) VALUES (08, 'Trail Mix', 1.25, 100)"

        db_cursor.execute(query1)
        db.commit()
        db_cursor.execute(query2)
        db.commit()
        db_cursor.execute(query3)
        db.commit()
        db_cursor.execute(query4)
        db.commit()
        db_cursor.execute(query5)
        db.commit()
        db_cursor.execute(query6)
        db.commit()
        db_cursor.execute(query7)
        db.commit()
        db_cursor.execute(query8)
        db.commit()
        db_cursor.execute(query9)
        db.commit()
        db_cursor.execute(query10)
        db.commit()

        print("Updated Food Inventory")
        return True
