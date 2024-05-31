#!/usr/bin/env python3
'''
This is Task 0 which involves creating a basic Flask application.
'''

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    '''
    This function defines the default route for the application.
    '''
    return render_template("0-index.html",)

if __name__ == "__main__":
    # This line ensures the application runs in debug mode when the script is run directly.
    app.run(debug=True)

