from flask import Flask
import random

# The first argument is the name of the application’s module or package.
app = Flask(__name__)
# print(__name__)
# print(random.__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/bye")
def say_bye():
    return "Bye"

if __name__ == "__main__":
    app.run()
# you can use the app.run() method
# or
# by setting the environment variable
# export FLASK_APP=hello.py
# and doing flask run
from flask import Flask

app = Flask(__name__)

