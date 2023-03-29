#!/usr/bin/python3
"""
You must use storage for fetching data
from the storage engine (FileStorage or DBStorage) =>
from models import storage and storage.all(...)
"""
from models import storage
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_states():
    """
    /states_list: display a HTML page: (inside the tag BODY)
    H1 tag: “States”
    UL tag: with the list of all State objects present in DBStorage
    sorted by name (A->Z) tipLI tag: description of one State: <state.id>:
    <B><state.name></B>
    """
    states = storage.all('State')
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """
    After each request you must remove the current SQLAlchemy Session:
    Declare a method to handle @app.teardown_appcontext
    Call in this method storage.close()
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
