#!/usr/bin/python3
"""
Starts a Flask web application that displays a list of all State objects
and their corresponding City objects.
It listens on 0.0.0.0, port 5000.
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """
    After each request, this method closes the current SQLAlchemy Session.
    """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    Fetches all State objects from storage, sorts them alphabetically,
    and renders them along with their cities in an HTML template.
    """
    # Grab all State objects from the storage engine
    states = storage.all(State).values()
    
    # Sort the states alphabetically by their 'name' attribute
    sorted_states = sorted(states, key=lambda k: k.name)
    
    # Pass the sorted list to the template
    return render_template('8-cities_by_states.html', states=sorted_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
