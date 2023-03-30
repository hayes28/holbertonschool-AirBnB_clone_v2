#!/usr/bin/python3
""" Starts new Flask web application """

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


def StartFlask():
    """ Starts Flask web application """
    app.run(host='0.0.0.0', port=5000)


@app.route('/states', strict_slashes=False)
def states_list():
    """ Displays a List of States """
    states = storage.all('State')
    return render_template('9-states.html', states=states.values(), id=None)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """ Displays a List of States """
    states = storage.all('State')
    state = states.get('State.' + id)
    return render_template('9-states.html', states=state, my_id=id)


@app.teardown_appcontext
def teardown_db(exception):
    """ Remove current SQLAlchemy Session """
    storage.close()


if __name__ == "__main__":
    StartFlask()
