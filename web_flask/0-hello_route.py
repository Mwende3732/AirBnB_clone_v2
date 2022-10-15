#!/usr/bin/python3
"""
starts a flask web application
The application listens on localhost port 5000
"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"

  app.run(host="0.0.0.0")
if __name__ == "__main__":
  