from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie-collection.db"
app.config["check_same_thread"]= False
db = SQLAlchemy(app)
Bootstrap(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    year = db.Column(db.Date)
    description = db.Column(db.String)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String)
    img_url = db.Column(db.String)

with app.app_context():
    db.create_all()
    all_movies = db.session.query(Movie).all()

@app.route("/")
def home():
    with app.app_context():
        all_movies = db.session.query(Movie).all()
    return render_template("index.html", all_movies=all_movies)

@app.route("/add", methods=["GET", "POST"])
def add():
    if(request.method == "POST"):
        new_movie = Movie(
        title="Phone Booth",
        year=2002,
        description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
        rating=7.3,
        ranking=10,
        review="My favourite character was the caller.",
        img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
    )
        with app.app_context():
                db.session.add(new_movie)
                db.session.commit()
                
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)
