#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """ 10. States and State """
    states = storage.all('State')
    return render_template("9-states.html", states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """ 10. States and State """
    for state in storage.all('State').values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown_db(exc):
    """ 10. States and State """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
