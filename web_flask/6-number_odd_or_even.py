#!/usr/bin/python3
"""Script that start a flask web app"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Return string when route is called"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Return string when route is called"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """Return C followed by text"""
    return "C " + text.replace('_', ' ')


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_cool(text="is cool"):
    """Return Python, followed by text"""
    return "Python " + text.replace('_', ' ')


@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    """Display n is a number only if it's an integer"""
    return "{:d} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Display HTML page if n is an ineteger"""
    return render_template("5-number.html", n=n)


@app.route("/number_old_or_even/<int:n>", strict_slashes=False)
def number_old_or_even(n):
    """Dispays HTML page if number is an integer"""
    return render_template("6-number_old_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
