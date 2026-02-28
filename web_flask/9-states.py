#!/usr/bin/python3
"""
Starts a Flask web application that displays states and their cities.
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


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_and_state(id=None):
    """
    If no ID is provided, displays a list of all states.
    If an ID is provided, displays the specific state and its cities.
    If the ID is not found, displays 'Not found!'.
    """
    # Fetch all states from the database
    states_dict = storage.all(State)
    
    if id is not None:
        # User gave an ID! Let's format the key to look for it (e.g., "State.123")
        target_key = "State." + id
        
        # Check if the state exists in our dictionary
        if target_key in states_dict:
            target_state = states_dict[target_key]
            # Pass the specific state to the template
            return render_template('9-states.html', state=target_state, id=id)
        else:
            # State not found
            return render_template('9-states.html', state=None, id=id)
            
    else:
        # User did not give an ID. Show the main list, sorted alphabetically.
        sorted_states = sorted(states_dict.values(), key=lambda s: s.name)
        return render_template('9-states.html', states=sorted_states, id=id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
