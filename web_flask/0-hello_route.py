#!/usr/bin/python3
"""
This module starts a simple Flask web application.
It listens on 0.0.0.0, port 5000, and has a single route.
"""
from flask import Flask

# Create the Flask application object
app = Flask(__name__)


# Define the route for the main page
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Displays the text 'Hello HBNB!' when the root URL is accessed.
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    # Start the application on all available IP addresses on port 5000
    app.run(host='0.0.0.0', port=5000)
