#!/usr/bin/python3
""" Starts new Flask web application """

from flask import Flask, render_template
from models import storage

app = Flask(__name__)



@app.route("/states", strict_slashes=False)
def states():
    """Display a HTML page with a list of all State objects
    present in DBStorage sorted by name (A->Z)"""
    states = storage.all(State)
    sorted_states_list = sorted(states.values(), key=lambda state: state.name)
    return render_template('9-states.html',
                           states=sorted_states_list, display_all=True)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Display a HTML page with information about a specific State
    based on its id"""
    states = storage.all(State)
    state = states.get("State.{}".format(id))
    return render_template('9-states.html', state=state, display_all=False)


@app.teardown_appcontext
def close_storage(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
