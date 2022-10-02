from flask import Flask,render_template
from datetime import date

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html",num=69,today_date=date.today().strftime("%Y"), your_name="YOUR_NAME")

############
if __name__ == "__main__":
    app.run(debug=True)