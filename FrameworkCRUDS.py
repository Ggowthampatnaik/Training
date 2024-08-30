# Framework CRUDS Program using SQLite

import sqlite3

def AddBook():
	global Fields, Messages
	FieldValues = ()
	for Field in Fields:
		FieldValues = FieldValues + (input(f"Enter {Field}: "), )
	PlaceHolders = ', '.join(['?'] * len(Fields))
	FieldNames = ', '.join(Fields)
	DbCursor.execute(f'INSERT INTO Records ({FieldNames}) VALUES ({PlaceHolders})', FieldValues)
	DbConnection.commit()
	print(Messages[InputKey - 1])

def PrintAllData():
    Records = DbCursor.execute('SELECT * FROM Records')
    print(Fields)
    for Record in Records:
        print(Record)
    print(Messages[InputKey - 1])

def SearchPrintData():
    SearchID = GetSearchID("Search")
    DbCursor.execute(f'SELECT * FROM Records WHERE {Fields[0]} = ?', (SearchID,))
    Record = DbCursor.fetchone()
    print(Fields)
    if Record:
        print(f"{Record}")
    else:
        print(f"{Fields[0]} not found.")
    print(Messages[InputKey - 1])

def UpdateBook():
    SearchID = GetSearchID("Update")
    for index, Field in enumerate(Fields):
        print(f"{index}: {Field}")
    InputKey = int(input("Enter the number corresponding to the field you want to edit: "))
    NewValue = input(f"Enter New {Fields[InputKey]}: ")
    DbCursor.execute(f'UPDATE Records SET {Fields[InputKey]} = ? WHERE {Fields[0]} = ?', (NewValue, SearchID))
    DbConnection.commit()
    print(Messages[InputKey - 1])

def DeleteBook():
    SearchID = GetSearchID("Delete")
    DbCursor.execute(f'DELETE FROM Records WHERE {Fields[0]} = ?', (SearchID,))
    DbConnection.commit()
    print(Messages[InputKey - 1])

def Exit():
    print(Messages[InputKey - 1])
    quit()

def LoadConfig():
    global DbCursor, Menu, Fields, Messages, Keyword
    ConfigRecords = DbCursor.execute('SELECT * FROM CongifFile').fetchall()
    DbCursor.execute(f'PRAGMA table_info(Records)')
    Fields = [column[1] for column in DbCursor.fetchall()]
    Fields = tuple(Fields)
    for key, value in ConfigRecords:
        if key == 'Menu':
            Menu = eval(value)
        elif key == 'Keyword':
            Keyword = value
        elif key == 'Messeges':
            Messages = eval(value)

def GetSearchID(Operation):
    SearchID = input(f"Enter {Fields[0]} to {Operation}: ")
    return SearchID

def ShowMenu():
    global InputKey
    Functions = [AddBook, PrintAllData, SearchPrintData, UpdateBook, DeleteBook, Exit]
    while True:
        for MenuItem in Menu:
            print(MenuItem)
        try:
            InputKey = int(input("Enter Key: "))
            if 1 <= InputKey <= len(Functions):
                Functions[InputKey - 1]()
            else:
                print("Invalid selection, please choose a valid option.")
        except ValueError:
            print("Invalid input, please enter a number.")

Menu = None
Fields = None 
Messages = None 
Keyword = None 
InputKey = None
SearchID = None

DbConnection = sqlite3.connect('Framework.db')
DbCursor = DbConnection.cursor()
LoadConfig()
ID = Fields[0]
ShowMenu()
