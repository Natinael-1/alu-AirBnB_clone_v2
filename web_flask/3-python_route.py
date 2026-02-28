#!/usr/bin/python3
"""
This module starts a Flask web application with four routes.
It listens on 0.0.0.0, port 5000.
"""
from flask import Flask

# Create the Flask application object
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Displays 'Hello HBNB!' when the root URL is accessed.
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Displays 'HBNB' when the /hbnb URL is accessed.
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Displays 'C ' followed by the value of the text variable.
    Replaces any underscore characters (_) with a space.
    """
    return "C {}".format(text.replace('_', ' '))


# We use two decorators here so that both /python and /python/text work
@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """
    Displays 'Python ' followed by the value of the text variable.
    If no text is provided, the default value is 'is cool'.
    Replaces any underscore characters (_) with a space.
    """
    return "Python {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    # Start the application on all available IP addresses on port 5000
    app.run(host='0.0.0.0', port=5000)
