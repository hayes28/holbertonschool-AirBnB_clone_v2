#!/usr/bin/python3
"""
Script that starts a Flask web application listening on 0.0.0.0:5000
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def state_list():
    """
    Displays an HTML formatted list of states from DBStorage
    """
    states = storage.all(State)
    return render_template("7-states_list.html", state_list=states)


@app.teardown_appcontext
def teardown(stuff):
    """
    Remove current SQLAlchemy session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
