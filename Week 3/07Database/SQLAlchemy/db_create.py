from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine, update, delete, select
# The following line creates engine to connect to database. It also creates the database if it doesn't exist
engine = create_engine('sqlite:///07Database/SQLAlchemy/database.db', echo = True) 
meta = MetaData()

# The follwing snippet describes the structure of the table in the database
students = Table(
   'details', meta, 
   Column('name', String, primary_key = True), 
   Column('colour', String), 
   Column('opinion', String), 
)

meta.create_all(engine) # Creates engine metadata
conn = engine.connect() # Connects to database

# This is a snippet for insertion
# result = conn.execute(students.insert(), [{'name' : 'Synergy', 'colour' : 'Blue', 'opinion' : 'Yes'},
#                                           {'name' : 'Daisy', 'colour' : 'Green', 'opinion' : 'Kind-of'}, 
#                                           {'name' : 'Alan', 'colour' : 'Yellow', 'opinion' : 'No'}])

# This is a snippet for Updating entries
# s = update(students).where(students.c.name=='Alan').values(colour = 'Red', opinion = 'Kind-of')

# This is the snippet for deletion
# s = delete(students).where(students.c.name=='Alan')

# This is how you execute a statement. Uncomment any one line above and see the results.
result = conn.execute(s)

# The following snippet is for displaying the table after all operations are done.
st = students.select()
result = conn.execute(st).fetchall()
for row in result:
   print(row)
