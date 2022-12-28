import sqlite3

db=sqlite3.connect("books-collection.db")
cursor=db.cursor()
# So a cursor is also known as the mouse or pointer. 
# Our database can contain many tables.
# All actions in SQLite databases are expressed as SQL (Structured Query Language) commands.

# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit()

# Luckily, there are much better ways of working with SQLite in Python projects, we can use a tool called SQLAlchemy (an ORM) to write Python code instead of all these error-prone SQL commands. That's what we'll do in the next lesson!

# SQLAlchemy is defined as an ORM Object Relational Mapping library. 
# This means that it's able to map the relationships in the database into Objects. Fields become Object properties. Tables can be defined as separate Classes and each row of data is a new Object.