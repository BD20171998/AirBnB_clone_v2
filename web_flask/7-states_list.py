#!/usr/bin/python3


"""utilizing Flask for Web app frame work"""

from flask import Flask, render_template
from models import storage, State
from flask import escape

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def show_states():
    '''Dictionary: of States'''
    state_dict = storage.all(State)
    return render_template('7-states_list.html', state_dict=state_dict)


@app.teardown_appcontext
def teardown_db(self):
    '''Deletes the current session'''
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
