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
        state_dict.append({'id': obj.id, 'name': obj.name})
    return state_dict


@app.route('/states_list', strict_slashes=False)
def states():
    return render_template('7-states_list.html', states=get_list_of_states())


@app.teardown_appcontext
def db_close(error):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
