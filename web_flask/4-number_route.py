#!/usr/bin/python3


"""utilizing Flask for Web app frame work"""
from flask import Flask, escape

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def home():
    """method that defines '/' route for Flask web application"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """method that defines '/hbnb' route"""
    return "HBNB"


@app.route('/c/<text>')
def show_text(text):
    """method that defines '/c/' route that uses a variable"""
    return 'C %s' % escape(text)


@app.route('/python/')
@app.route('/python/<text>')
def show_text2(text="is cool"):
    """method that defines '/python/' route that uses a variable"""
    return 'Python %s' % escape(text)


@app.route('/number/<int:n>')
def show_text3(n):
    """method that defines '/number/' route that uses a variable"""
    if isinstance(n, int):
        return '%d is a number' % n

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
