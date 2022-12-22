from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def show_form():
    return render_template('index.html')

# trigger a method when it receives a POST request:
@app.route('/login', methods=['POST'])
def login():
    if request.method=='POST':
        #  Flask has a method called request which allows us to 
        # tap into the parameters of the request that was made to our server.
        # To access form data, you can use the form attribute. 
        username = request.form['username']
        password = request.form['password']

        return f"<h1>Logged in bruh</h1><p>{username}</p><p>{password}</p>"