from flask import Flask, render_template
import requests

app = Flask(__name__)
api_fetch = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391").json()

# Home page rendered
@app.route("/")
@app.route("/index.html")
def home():
    return render_template('index.html',api_fetch=api_fetch)

# About page rendered
@app.route("/about.html")
def about():
    return render_template('about.html')

# Contact page rendered
@app.route("/contact.html")
def contact():
    return render_template("contact.html")





########### notes ###########

""" https://stackoverflow.com/questions/29882642/how-to-run-a-flask-application """

# if __name__ == "__main__":
#     app.run(debug=True)

# or 

# in terminal:
# >>> export FLASK_APP=main
# >>> export FLASK_ENV=development
# >>> flask run

