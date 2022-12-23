from flask import Flask, render_template, request
import requests

app = Flask(__name__)
api_fetch = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391").json()

# Home page rendered
@app.route("/")
@app.route("/index")
def home():
    return render_template('index.html',api_fetch=api_fetch)

# About page rendered
@app.route("/about")
def about():
    return render_template('about.html')

# Contact page rendered AND Contact form submission
@app.route("/contact", methods=["GET","POST"])
def contact():
    if request.method=="GET":
        return render_template("contact.html", msg_sent = False)

    elif(request.method=="POST"):
        message = request.form["message"]
        return render_template("contact.html", msg_sent = True)

# Posts rendered dynamically
""" You can add variable sections to a URL by marking sections with <variable_name>. 
Your function then receives the <variable_name> as a keyword argument. 
Optionally, you can use a converter to specify the type of the argument 
like <converter:variable_name>. """
@app.route("/post/<int:post_id>")
def post(post_id):
    return render_template("post.html", posts = api_fetch, post_index = post_id-1)


########### notes ###########

""" https://stackoverflow.com/questions/29882642/how-to-run-a-flask-application """

# if __name__ == "__main__":
#     app.run(debug=True)

# or 

# in terminal:
# >>> export FLASK_APP=main
# >>> export FLASK_ENV=development
# >>> flask run

