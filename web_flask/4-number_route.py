#!/usr/bin/python3
"""
This module starts a Flask web application with five routes.
It listens on 0.0.0.0, port 5000.
"""
from flask import Flask

# Create the Flask application object
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'HBNB'"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Displays 'C ' followed by the text variable."""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """Displays 'Python ' followed by the text variable (default is cool)."""
    return "Python {}".format(text.replace('_', ' '))


# Notice the <int:n> here. This is the "bouncer" forcing it to be an integer.
@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """Displays 'n is a number' only if n is an integer."""
    return "{} is a number".format(n)


if __name__ == "__main__":
    # Start the application on all available IP addresses on port 5000
    app.run(host='0.0.0.0', port=5000)
