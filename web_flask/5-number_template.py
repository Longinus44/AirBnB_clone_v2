#!/usr/bin/python3
"""
A simple Flask web application module.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route handler for the root URL.
    Returns a greeting message "Hello HBNB!".
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route handler for hbnb URL
    Returns "HBNB"
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
     Route handler for the /c/<text> URL.
    Returns a message "C " followed by the value of the text variable.
    Underscore _ symbols in <text> are replaced with spaces.
    """
    return f"C " + text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def route_text(text):
    """
    Route to display 'Python ' followed by the value of the text variable
      with underscores replaced by spaces.
    If no text is provided, defaults to 'is cool'.
    """
    return f"Python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def n_is_number(n):
    """
        Route to check if 'n' is a number and display 'n is a number' if true.
    """
    return f"{n} is a number"


@app.route('/number_template/<int:n>')
def template_n(n):
    """
    Route to display a HTML page only if 'n' is an integer.
    The HTML page includes an H1 tag with 'Number: n'.
    """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
