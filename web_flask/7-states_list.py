#!/usr/bin/python3
"""
Script that starts a Flask web application listening on 0.0.0.0:5000
Use storage for fetching data from the storage engine File or DB storage
from models import storage and storage.all(...)
After each request, remove current SQLAlchemy Session:
    Declare method to handle @app.teardown_appcontext
    Call in this method: storage.close()
Route /states_list: display a HTML page
    H1 tag: "States"
    UL tag: list of all State objects present in DBStorage sorted by name
        LI tag: Description of one State: <state.id>: <<B><state.name></B>
Must use option strict_slashes=False
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(stuff):
    """
    Remove current SQLAlchemy session
    """
    storage.close()


@app.route("/states_list")
def state_list():
    """
    Displays an HTML formatted list of states from DBStorage
    """
    states = storage.all(State)
    return render_template("7-states_list.html", state_list=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
