#!/usr/bin/python3
""" Starts new Flask web application """

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


app.url_map.strict_slashes = False


@app.route("/states")
@app.route("/states/<id>")
def states_id_route(id=None):
    """
    Displays an HTML formatted of cities with a given State id
    """
    states = storage.all(State)
    return render_template("9-states.html", state_list=states, id=id)


@app.teardown_appcontext
def teardown(stuff):
    """
    Remove current SQLAlchemy session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
