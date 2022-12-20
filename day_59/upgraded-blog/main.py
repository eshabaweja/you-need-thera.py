from flask import Flask, render_template

app = Flask(__name__)

# Home page rendered
@app.route("/")
def home():
    return render_template('index.html')






########### notes ###########

""" https://stackoverflow.com/questions/29882642/how-to-run-a-flask-application """

# if __name__ == "__main__":
#     app.run(debug=True)

# or 

# in terminal:
# >>> export FLASK_APP=main
# >>> export FLASK_ENV=development
# >>> flask run

