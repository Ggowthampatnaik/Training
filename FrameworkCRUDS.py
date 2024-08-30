# Framework CRUDS Program using SQLite

import sqlite3

def AddRecord():
	global Fields, Messages
	FieldValues = ()
	for Field in Fields:
		FieldValues = FieldValues + (input(f"Enter {Field}: "), )
	PlaceHolders = ', '.join(['?'] * len(Fields))
	FieldNames = ', '.join(Fields)
	DbCursor.execute(f'INSERT INTO RecordsTable ({FieldNames}) VALUES ({PlaceHolders})', FieldValues)
	DbConnection.commit()
	print(Messages[InputKey - 1])

def PrintAllRecords():
    Records = DbCursor.execute('SELECT * FROM RecordsTable')
    print(Fields)
    for Record in Records:
        print(Record)
    print(Messages[InputKey - 1])

def SearchPrintRecord():
    SearchID = GetSearchID("Search")
    DbCursor.execute(f'SELECT * FROM RecordsTable WHERE {ID} = ?', (SearchID,))
    Record = DbCursor.fetchone()
    print(Fields)
    if Record:
        print(f"{Record}")
    else:
        print(f"{ID} not found.")
    print(Messages[InputKey - 1])

def UpdateRecord():
    SearchID = GetSearchID("Update")
    for Index, Field in enumerate(Fields[1:], start = 1):
        print(f"{Index}: {Field}")
    InputKey = int(input("Enter the number corresponding to the field you want to edit: "))
    NewValue = input(f"Enter New {Fields[InputKey]}: ")
    DbCursor.execute(f'UPDATE RecordsTable SET {Fields[InputKey]} = ? WHERE {ID} = ?', (NewValue, SearchID))
    DbConnection.commit()
    print(Messages[InputKey - 1])

def DeleteRecord():
    SearchID = GetSearchID("Delete")
    DbCursor.execute(f'DELETE FROM RecordsTable WHERE {ID} = ?', (SearchID,))
    DbConnection.commit()
    print(Messages[InputKey - 1])

def Exit():
    print(Messages[InputKey - 1])
    quit()

def LoadConfig():
    global DbCursor, Menu, Fields, Messages, Keyword
    ConfigRecords = DbCursor.execute('SELECT * FROM ConfigTable').fetchall()
    DbCursor.execute(f'PRAGMA table_info(RecordsTable)')
    Fields = [column[1] for column in DbCursor.fetchall()]
    Fields = tuple(Fields)
    for key, value in ConfigRecords:
        if key == 'Menu':
            Menu = eval(value)
        elif key == 'Keyword':
            Keyword = value
        elif key == 'Messages':
            Messages = eval(value)

def GetSearchID(Operation):
    SearchID = input(f"Enter {ID} to {Operation}: ")
    return SearchID

def ShowMenu():
    global InputKey
    Functions = [AddRecord, PrintAllRecords, SearchPrintRecord, UpdateRecord, DeleteRecord, Exit]
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

DbConnection = sqlite3.connect('Framework1.db')
DbCursor = DbConnection.cursor()
LoadConfig()
ID = Fields[0]
ShowMenu()
