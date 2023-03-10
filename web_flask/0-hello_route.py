#!/usr/bin/python3
"""
This script starts a Flask web application and
serves a "Hello HBNB!" message on the route /airbnb-onepage/.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/airbnb-onepage/')
def hello_hbnb():
    """
    Defines a handler for the route /airbnb-onepage/.
    Returns: "Hello HBNB!"
    """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
