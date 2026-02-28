#!/usr/bin/python3
"""
Starts a Flask web application that renders the HBNB filters page.
It listens on 0.0.0.0, port 5000.
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Closes the database connection at the end of the request.
    """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """
    Fetches all State and Amenity objects, sorts them alphabetically,
    and renders the interactive filter page.
    """
    # Fetch and sort states
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda k: k.name)
    
    # Fetch and sort amenities
    amenities = storage.all(Amenity).values()
    sorted_amenities = sorted(amenities, key=lambda k: k.name)
    
    return render_template('10-hbnb_filters.html',
                           states=sorted_states,
                           amenities=sorted_amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
