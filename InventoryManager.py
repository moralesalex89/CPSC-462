from includes.DatabaseConfig import db
from tkinter import messagebox
from PaymentManager import *


class InventoryManager:

	def check_stock(self):
		db_cursor = db.cursor()
		query = "SELECT name, cost, stock FROM Food_Inventory WHERE stock > 0"
		db_cursor.execute(query)

		result = db_cursor.fetchall()
		return result

	def buy_item(self, food_name, user_id, cost, note):

		db_cursor = db.cursor()
		query = "UPDATE Food_Inventory SET stock = stock - 1 WHERE name = '%s'" % food_name
		db_cursor.execute(query)
		db.commit()

		add_payment(user_id, cost, note)


		print(food_name + " snack purchased!")
		return True

	# Fill up the database with food to initialize it
	def stock_items(self):

		db_cursor = db.cursor()
		query1 = "INSERT IGNORE INTO Food_Inventory (food_id, name, cost, stock) VALUES (01, 'Cheetos', 1.50, 100)"
		query2 = "INSERT IGNORE INTO Food_Inventory (food_id, name, cost, stock) VALUES (02, 'Famous Amos', 1.25, 100)"
		query3 = "INSERT IGNORE INTO Food_Inventory (food_id, name, cost, stock) VALUES (03, 'Fritos', 1.00, 100)"
		query4 = "INSERT IGNORE INTO Food_Inventory (food_id, name, cost, stock) VALUES (04, 'Lays', 1.50, 100)"
		query5 = "INSERT IGNORE INTO Food_Inventory (food_id, name, cost, stock) VALUES (05, 'M&Ms', 1.00, 100)"
		query6 = "INSERT IGNORE INTO Food_Inventory (food_id, name, cost, stock) VALUES (06, 'Oreos', 1.25, 100)"
		query7 = "INSERT IGNORE INTO Food_Inventory (food_id, name, cost, stock) VALUES (07, 'Pop Tarts', 2.00, 100)"
		query8 = "INSERT IGNORE INTO Food_Inventory (food_id, name, cost, stock) VALUES (08, 'Reeses', 1.00, 100)"
		query9 = "INSERT IGNORE INTO Food_Inventory (food_id, name, cost, stock) VALUES (09, 'Rice Krispies', 1.00, 100)"
		query10 = "INSERT IGNORE INTO Food_Inventory (food_id, name, cost, stock) VALUES (10, 'Trail Mix', 1.25, 100)"

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

		print("Initialized Food Inventory")
		return True

	def restock_items(self):
		db_cursor = db.cursor()
		query = "UPDATE Food_Inventory SET stock = 100 WHERE stock < 100"
		db_cursor.execute(query)
		db.commit()
		return True

	def view_inventory(self):
		inventory = self.check_stock()
		inventory_str = ""

		for item in inventory:
			inventory_str += "%s %d\n" % (item[0], item[2])

		messagebox.showinfo("Current Food in Inventory", inventory_str)
		return True







