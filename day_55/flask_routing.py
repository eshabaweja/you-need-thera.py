from flask import Flask

app = Flask(__name__)

# my decorators
def make_bold(func):
    def wrapper_bold():
        return f"<b>{func()}</b>"
    return wrapper_bold

def make_emphasis(func):
    def wrapper_emphasis():
        return f"<em>{func()}</em>"
    return wrapper_emphasis

def make_underlined(func):
    def wrapper_underlined():
        return f"<u>{func()}</u>"
    return wrapper_underlined


# you can simply write html in the return statement
@app.route("/")
def hello_world():
    return '<h1 style="color:blue">Hello, World!</h1>\
        <p>this is a paragraph</p> \
        <img src="https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif" width="200px">'

@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye_world():
    return "Bye asf"

# https://flask.palletsprojects.com/en/2.1.x/quickstart/#routing
# You can add variable sections to a URL by marking sections with <variable_name>. 
# Debug mode: off

@app.route("/<name>")
def var_name(name):
    return f"Would ya look at that, {name}!"