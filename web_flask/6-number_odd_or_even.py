#!/usr/bin/python3
"""
This module starts a Flask web application with seven routes.
It listens on 0.0.0.0, port 5000.
"""
from flask import Flask, render_template

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
    """Displays 'Python ' followed by the text variable."""
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """Displays 'n is a number' only if n is an integer."""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Displays an HTML page with the number."""
    return render_template('5-number.html', n=n)


# The new route for Task 6
@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Displays an HTML page only if n is an integer.
    The HTML page determines if the number is odd or even.
    """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    # Start the application on all available IP addresses on port 5000
    app.run(host='0.0.0.0', port=5000)
