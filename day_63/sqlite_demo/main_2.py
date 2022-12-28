from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
# initialize the app with the extension
db.init_app(app)

# The model will generate a table name by converting the CamelCase class name to snake_case.
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    author = db.Column(db.String)
    rating = db.Column(db.Float, nullable=False)


new_book=Book(name="34+35", author="Ariana",rating=6.9)

with app.app_context():
    db.create_all()
    db.session.add(new_book)
    db.session.commit()
    all_books = session.query(Book).all()

# Things to figure out when working with any new database technology
# is how to CRUD data records.

# Create
# Read
# Update
# Delete