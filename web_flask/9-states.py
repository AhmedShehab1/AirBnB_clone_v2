#!/usr/bin/python3
"""
Module to fetch data from db
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


def get_list_of_states(id=None):
    state_list = []
    for obj in storage.all(State).values():
        state_list.append(obj)
    if id:
        for obj in state_list:
            if (obj.id) == id:
                return obj
    return state_list


@app.teardown_appcontext
def close_db(error):
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<string:id>', strict_slashes=False)
def all_states(id=None):
    return render_template('9-states.html',
                           states=get_list_of_states(id), single_id=id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
