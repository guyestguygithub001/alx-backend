#!/usr/bin/env python3
'''
This is Task 4 which involves creating a Flask application that forces the locale with a URL parameter and retrieves user details.
'''

from typing import Dict, Union
from flask import Flask, render_template, request, g
from flask_babel import Babel

class Config:
    '''
    This class defines the configuration for the Flask application, including the supported languages, default settings, and debug mode.
    '''

    DEBUG = True
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user() -> Union[Dict, None]:
    """
    This function retrieves a user based on a user id from the URL parameter 'login_as'.
    
    Returns:
        dict or None: The user details if the user id exists, None otherwise.
    """
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None

@app.before_request
def before_request() -> None:
    """
    This function is executed before each request to the application. It retrieves the user details and stores them in the global object 'g'.
    """
    g.user = get_user()

@babel.localeselector
def get_locale() -> str:
    """
    This function retrieves the locale from the URL parameter if it's in the supported languages. 
    If not, it retrieves the best matching language from the request's accepted languages.
    
    Returns:
        str: The locale from the URL parameter or the best matching language from the request's accepted languages.
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index() -> str:
    '''
    This function defines the default route for the application and returns the homepage.
    
    Returns:
        html: The homepage of the application.
    '''
    return render_template("5-index.html")

# If you uncomment the following line and comment the @babel.localeselector,
# you will encounter an error: AttributeError: 'Babel' object has no attribute 'localeselector'
# babel.init_app(app, locale_selector=get_locale)

if __name__ == "__main__":
    # This line ensures the application runs in debug mode when the script is run directly.
    app.run()

