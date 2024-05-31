#!/usr/bin/env python3
'''
This is a basic Flask application with its internationalization support.
'''

import pytz
from typing import Union, Dict
from flask_babel import Babel, format_datetime
from flask import Flask, render_template, request, g

class Config:
    '''
    This class represents the configuration for Flask Babel.
    '''

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)

# A dictionary of users with their details such as name, locale, and timezone.
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user() -> Union[Dict, None]:
    '''
    This function retrieves a user based on a user id from the URL parameter 'login_as'.
    
    Returns:
        dict or None: The user details if the user id exists, None otherwise.
    '''
    login_id = request.args.get('login_as', '')
    if login_id:
        return users.get(int(login_id), None)
    return None

@app.before_request
def before_request() -> None:
    '''
    This function is executed before each request to the application. It retrieves the user details and stores them in the global object 'g'.
    '''
    user = get_user()
    g.user = user

@babel.localeselector
def get_locale() -> str:
    '''
    This function retrieves the locale from the URL parameter, user details, or request headers if they're in the supported languages. 
    If not, it retrieves the default locale from the application configuration.
    
    Returns:
        str: The locale from the URL parameter, user details, or request headers, or the default locale from the application configuration.
    '''
    queries = request.query_string.decode('utf-8').split('&')
    query_table = dict(map(
        lambda x: (x if '=' in x else '{}='.format(x)).split('='),
        queries,
    ))
    locale = query_table.get('locale', '')
    if locale in app.config["LANGUAGES"]:
        return locale
    user_details = getattr(g, 'user', None)
    if user_details and user_details['locale'] in app.config["LANGUAGES"]:
        return user_details['locale']
    header_locale = request.headers.get('locale', '')
    if header_locale in app.config["LANGUAGES"]:
        return header_locale
    return app.config['BABEL_DEFAULT_LOCALE']

@babel.timezoneselector
def get_timezone() -> str:
    '''
    This function retrieves the time zone from the URL parameter or user details if they're valid. 
    If not, it returns the default time zone from the application configuration.
    
    Returns:
        str: The time zone from the URL parameter or user details, or the default time zone from the application configuration.
    '''
    timezone = request.args.get('timezone', '').strip()
    if not timezone and g.user:
        timezone = g.user['timezone']
    try:
        return pytz.timezone(timezone).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']

@app.route('/')
def get_index() -> str:
    '''
    This function defines the default route for the application and returns the homepage.
    
    Returns:
        html: The homepage of the application.
    '''
    g.time = format_datetime()
    return render_template('index.html')

if __name__ == '__main__':
    # This line ensures the application runs in debug mode when the script is run directly.
    app.run()

