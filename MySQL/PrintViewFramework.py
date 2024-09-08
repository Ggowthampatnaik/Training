# Print records in a View in MySQL Database

import mysql.connector

def ConnectDatabase():
	global DbConnection, DbCursor
	DbConnection = mysql.connector.connect(
		host='138.68.140.83', 
		user='gowtham', 
		password='Gowtham@123', 
		database='dbGowtham'
	)
	DbCursor = DbConnection.cursor()

def LoadFields():
	global DbCursor, Fields
	DbCursor.execute(f"SHOW COLUMNS FROM {FrameworkView}")
	Fields = [Field[0] for Field in DbCursor.fetchall()]

def PrintView():
	global DbCursor, Fields
	DbCursor.execute(f"SELECT * FROM {FrameworkView}")
	Records = DbCursor.fetchall()
	for Record in Records:
		for FieldCounter, Field in enumerate(Fields):
			print(f"{Field}: {Record[FieldCounter]}")
		print("\n")

FrameworkView = "FrameworkView"
ConnectDatabase()
LoadFields()
PrintView()
