from flask import Flask, request

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    """Return simple "Welcome" Greeting."""

    html = "<html><body><h1>Welcome</h1></body></html>"
    return html


@app.route('/welcome/home')
def welcome_home():
    """Return simple "Welcome home" Greeting."""

    html = "<html><body><h1>Welcome home</h1></body></html>"
    return html

@app.route('/welcome/back')
def welcome_back():
    """Return simple "Welcome back" Greeting."""

    html = "<html><body><h1>Welcome back</h1></body></html>"
    return html