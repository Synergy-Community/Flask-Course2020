import sqlite3

# Connects to the database
connection = sqlite3.connect(r'07Database\SQLite\database.db') 
#Pylint does not trust sqlite3, so you might be shown an error here. Ignore it.
print("Database opened")

# Creates a table in the database
# connection.execute('CREATE TABLE details (name TEXT, colour TEXT, opinion TEXT)')
# print('Table created')

# This snippet prints all the rowws from the table
cursor = connection.cursor()
cursor.execute('select * from details')
all_rows = cursor.fetchall()
name_list = []
for row in all_rows:
    print(row)

# Closes the connection to the database. This is very important
connection.close()
