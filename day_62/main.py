from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import (
    StringField,
    SubmitField,
    URLField,
    TimeField,
    SelectField,
    validators,
)
from wtforms.validators import DataRequired
import csv

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap(app)
csrf = CSRFProtect(app=app)


class CafeForm(FlaskForm):
    cafe = StringField("Cafe name", validators=[DataRequired()])
    location = URLField("Cafe Location on Google Maps (URL)", validators=[validators.URL()])
    opening = TimeField("Opening Time", validators=[DataRequired()])
    closing = TimeField("Closing Time", validators=[DataRequired()])
    coffee_rating = SelectField(
        validators=[DataRequired()],
        choices=["✘", "☕️", "☕️☕️", "☕️☕️☕️", "☕️☕️☕️☕️", "☕️☕️☕️☕️☕️"],
    )
    wifi_rating = SelectField(
        validators=[DataRequired()], choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"]
    )
    power_rating = SelectField(
        validators=[DataRequired()], choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"]
    )

    submit = SubmitField("Submit")


# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
        # print(form.cafe.data)
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
        with open("cafe-data.csv", "a", newline="") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=",")
            cafe_attrs = []
            for cafe_attr in form:
                cafe_attrs.append(cafe_attr.data)
            csv_writer.writerow(cafe_attrs[:-2])
            
    return render_template("add.html", form=form)


@app.route("/cafes")
def cafes():
    with open("cafe-data.csv", newline="") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=",")
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template("cafes.html", cafes=list_of_rows)


if __name__ == "__main__":
    app.run(debug=True)
