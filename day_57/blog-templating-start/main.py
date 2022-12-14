from flask import Flask, render_template, url_for
import requests

app = Flask(__name__)

all_blogs = requests.get(url="https://api.npoint.io/9a16ff6ad3d962b83ec2").json()
# print(all_blogs)


@app.route("/")
def home():
    return render_template("index.html", all_blogs=all_blogs)


# url_for is defined as a function that enables developers to build and generate URLs on a Flask application


@app.route("/post/<int:blog_id>")
def post(blog_id):
    return render_template("post.html", blog_id=blog_id, all_blogs=all_blogs)


if __name__ == "__main__":
    app.run(debug=True)
