from flask import Flask, render_template
import random
from datetime import date
import requests

AGIFY = "https://api.agify.io/?name="
GENDERIZE = "https://api.genderize.io/?name="
YOUR_NAME="Esha"

app = Flask(__name__)

# home route
@app.route("/")
def hello():
    random_num = random.randint(1,10)
    return render_template("index.html",num=random_num,today_date=date.today().strftime("%Y"), your_name=YOUR_NAME)

# using APIs with Jinja
@app.route("/guess/<name>")
def guess(name):
    age = requests.get(url=AGIFY+name).json()["age"]
    gender = requests.get(url=GENDERIZE+name).json()["gender"]
    return render_template("guess.html", name=name,gender=gender,age=age)

# different markup for keywords

if __name__ == "__main__":
    app.run(debug=True)