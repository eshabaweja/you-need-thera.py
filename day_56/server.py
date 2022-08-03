from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
# def home():
#     return "hello world"

# rendering an html page
# def home():
#     return render_template("index.html")

# rendering my card
def home():
    return render_template("my_card.html")

if __name__== "__main__":
    app.run()