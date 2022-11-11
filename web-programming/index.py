from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Welcome to your home page</p>"

@app.route("/greet")
def greet():
    return "<h1>Hello World</h1>"

@app.route("/greet/<username>")
def greet_user(username):
    return f"Hello {username}"

