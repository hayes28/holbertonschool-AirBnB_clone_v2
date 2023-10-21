#!/usr/bin/python3
"""
Write a script that starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ displays Hello HBNB """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ displays HBNB """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cis(text):
    """ displays C followed by the value of the text variable """
    return f'C {text.replace("_", " ")}'


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pyis(text="is cool"):
    """ displays Python followed by the value of the text variable """
    return f'Python {text.replace("_", " ")}'


@app.route('/number/<int:n>', strict_slashes=False)
def num(n: int):
    """ displays n is a number only if n is an integer """
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
