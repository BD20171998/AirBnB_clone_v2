#!/usr/bin/python3


"""utilizing Flask for Web app frame work"""

from flask import Flask, render_template
from models import storage, State, City

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def show_states(state_id=None):
    """Dictionary of states"""

    if state_id is None:
        state_dict = storage.all(State)
        return render_template('9-states.html', state_id=state_id,
                               state_dict=state_dict)

    else:
        city_list = []
        all_cities = storage.all(City)
        all_states = storage.all(State)

        for key, value in all_cities.items():

            if value.__dict__.get('state_id') == state_id:
                    city_list.append(value)

        for key, value in all_states.items():
            if value.__dict__.get('id') == state_id:
                single_state = value

        return render_template('9-states.html', city_list=city_list,
                               single_state=single_state)


@app.teardown_appcontext
def teardown_db(self):
    '''Deletes the current session'''
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
