#!/usr/bin/python3
"""
starts a flask web application
rt Flask
from flask import render_template

app = """
from models import storage
from flask impoFlask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
"""
    Displays a HTML page with a list of all stdef cities_by_states():
    ates and related cities
    """
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """
    Remove current SQLAlchemy session
    """
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
