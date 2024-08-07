#!/usr/bin/python3
"""
Module to fetch data from db
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


def get_states():
    return storage.all(State).values()


def get_amenities():
    return storage.all(Amenity).values()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    return render_template('10-hbnb_filters.html', states=get_states(),
                           amenities=get_amenities())


@app.teardown_appcontext
def close_db(error):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
