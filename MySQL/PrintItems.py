# Print Items in MySQL Database using Python

import mysql.connector

def ConnectDatabase():
  global DbConnection, DbCursor
  DbConnection = mysql.connector.connect(host='138.68.140.83', user='gowtham', password='Gowtham@123', database='dbGowtham')
  DbCursor = DbConnection.cursor()

def LoadFields():
	global DbCursor, Fields
	DbCursor.execute(f"SHOW COLUMNS FROM {ItemTable}")
	Fields = [FieldName[0] for FieldName in DbCursor.fetchall()]

def PrintItems():
	global DbCursor
	DbCursor.execute(f"SELECT * FROM {ItemTable}")
	Items = DbCursor.fetchall()
	for Item in Items:
		for FieldCounter, Field in enumerate(Fields):
			print(f"{Field}: {Item[FieldCounter]}")
		print("\n")

ItemTable = "Item"
ConnectDatabase()
LoadFields()
PrintItems()
