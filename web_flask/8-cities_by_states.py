#!/usr/bin/python3
"""
Module to fetch data from db
"""

from models import storage
from flask import Flask, render_template
from models.state import State

app = Flask(__name__)


def get_list_of_states():
    state_dict = []
    for obj in storage.all(State).values():
        state_dict.append(obj)
    return state_dict


def get_list_of_cities():
    state_city_dictionary = {}
    for state in get_list_of_states():
        cities_list = []
        for city in state.cities:
            cities_list.append(city)
        state_city_dictionary.update({state: cities_list})
    return state_city_dictionary


@app.route('/cities_by_states', strict_slashes=False)
def states_and_cities():
    return render_template('8-cities_by_states.html',
                           state_cities=get_list_of_cities())


@app.teardown_appcontext
def db_close(error):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
