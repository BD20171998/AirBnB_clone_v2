#!/usr/bin/python3


"""utilizing Flask for Web app frame work"""

from flask import Flask, render_template
from models import storage, State
from flask import escape

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def show_cities():
    '''Dictionary: of Cities'''
    city_dict = storage.all(State)
    return render_template('8-cities_by_states.html', city_dict=city_dict)


@app.teardown_appcontext
def teardown_db(self):
    '''Deletes the current session'''
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
