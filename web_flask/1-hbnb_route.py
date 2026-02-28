#!/usr/bin/python3
"""
This module starts a Flask web application with two routes.
It listens on 0.0.0.0, port 5000.
"""
from flask import Flask

# Create the Flask application object
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Displays 'Hello HBNB!' when the root URL (/) is accessed.
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Displays 'HBNB' when the /hbnb URL is accessed.
    """
    return "HBNB"


if __name__ == "__main__":
    # Start the application on all available IP addresses on port 5000
    app.run(host='0.0.0.0', port=5000)
