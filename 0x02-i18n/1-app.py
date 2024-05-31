#!/usr/bin/env python3
'''
This is Task 0 which involves creating a basic Flask application with internationalization support.
'''
from flask_babel import Babel
from flask import Flask, render_template

class Config:
    '''
    This class defines the configuration for the Flask application, including the supported languages and default settings.
    '''

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False

babel = Babel(app)

@app.route('/')
def index():
    '''
    This function defines the default route for the application.
    '''
    return render_template("1-index.html",)

if __name__ == "__main__":
    # This line ensures the application runs in debug mode when the script is run directly.
    app.run(debug=True)

