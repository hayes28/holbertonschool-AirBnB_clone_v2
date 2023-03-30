#!/usr/bin/python3
"""
Start a Flask web application
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


def StartFlask():
    """
    Start Flask web app
    """
    app.run(host='0.0.0.0', port=5000)


@app.route('/', strict_slashes=False)
def show_pages():
    """
    Show all pages
    """
    states = storage.all('State')
    amenities = storage.all('Amenity')
    return render_template('10-hbnb_filters.html', states=states.values(),
                           amenities=amenities.values())


@app.teardown_appcontext
def teardown_db(exc):
    """
    Close storage
    """
    storage.close()


if __name__ == "__main__":
    StartFlask()
