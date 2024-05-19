#!/usr/bin/python3
from flask import Flask

"""
This Flask application creates a simple web server that listens on all interfaces (0.0.0.0)
and port 5000. It defines a route for the root URL (`/`) and displays the message "Hello HBNB!"
"""
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    This function handles requests to the root URL (`/`).

    Returns:
        str: The message "Hello HBNB!"
    """
    return f'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
