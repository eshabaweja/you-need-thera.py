from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# app creation and db initialize
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///book-collection.db"
app.config["check_same_thread"]= False
db = SQLAlchemy(app)

# The model will generate a table name by converting the CamelCase class name to snake_case.
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    author = db.Column(db.String)
    rating = db.Column(db.Float, nullable=False)

with app.app_context():
    db.create_all()
    # all_books = db.session.execute(db.select(Book)).scalars()
    all_books = db.session.query(Book).all()

@app.route('/')
def home():
    with app.app_context():
        all_books = db.session.query(Book).all()

    return render_template('index.html',all_books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if(request.method == "POST"):
        # all_books.append({
        # "title": request.form["bookname"],
        # "author": request.form["bookauthor"],
        # "rating": request.form["bookrating"]})
        new_book=Book(name=request.form["bookname"], author=request.form["bookauthor"],rating=request.form["bookrating"])

        with app.app_context():
            db.session.add(new_book)
            db.session.commit()
            
        # print(all_books)
    return render_template('add.html')
# print(dir(all_books))
# The dir() function, as shown above, prints all of the attributes of a Python object. 

if __name__ == "__main__":
    app.run(debug=True)