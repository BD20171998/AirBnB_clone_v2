#!/usr/bin/python3


"""utilizing Flask for Web app frame work"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def home():
    """method that defines '/' route for Flask web application"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """method that defines '/hbnb' route for Flask web application"""
    return "HBNB"


@app.route('/c/<text>')
def show_text(text):
    """method that defines '/c/' route for Flask app that uses a variable"""
    return "C {}".format(text.replace('_', ' '))

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
