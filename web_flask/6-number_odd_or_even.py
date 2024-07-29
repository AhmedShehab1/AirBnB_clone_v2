#!/usr/bin/python3

from flask import Flask, render_template

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


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False, defaults={'text': 'is_cool'})
def python(text):
    """ Defining route to be served to user"""
    text = text.replace('_', ' ')
    return f'Python {text}'


@app.route('/number/<int:n>', strict_slashes=False)
def only_if_int(n):
    """ Defining route to be served to user"""
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n):
    """ Defining route to be served to user"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_odd(n):
    """ Defining route to be served to user"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")