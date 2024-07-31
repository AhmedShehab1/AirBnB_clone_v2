#!/usr/bin/python3
"""
Module for Flask Framework
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Defining route to be served to user"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Defining route to be served to user"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ Defining route to be served to user"""
    text = text.replace('_', ' ')
    return f"C {text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
