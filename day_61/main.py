from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, validators
from flask_wtf.csrf import CSRFProtect

# Blueprint of Form
class LoginForm(FlaskForm):
    email = StringField(label='Email Address', validators=[validators.Length(max=30), validators.Email(message="Invalid email bruh")])
    password = PasswordField(label='Password', validators=[validators.Length(min=8,max=30), validators.DataRequired()])
    submit = SubmitField(label="Log In")
    
# instance of Flask app
app = Flask(__name__)
app.config['SECRET_KEY']='BigCronchMangoDB'
csrf = CSRFProtect(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    my_form = LoginForm()
    if my_form.validate_on_submit():
        if my_form.email.data == "admin@email.com" and my_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")

    # print(f"yaaaar {my_form.errors}")
    return render_template('login.html', my_form = my_form, errors = my_form.errors)


if __name__ == '__main__':
    app.run(debug=True)