#!/usr/bin/env python3
"""
Flask app with Babel integration for i18n and translations.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _
from datetime import datetime
from typing import Optional, Dict
import pytz
from pytz.exceptions import UnknownTimeZoneError


class Config:
    """
    Configuration class for Flask app.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Optional[Dict]:
    """
    Get user based on login_as parameter.
    """
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    """
    Function to run before each request.
    """
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """
    Determine the best match for supported languages based on the request.
    Order of priority:
    1. Locale from URL parameters
    2. Locale from user settings
    3. Locale from request header
    4. Default locale

    Returns:
        str: The best match language.
    """
    # Locale from URL parameters
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    # Locale from user settings
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user['locale']

    # Locale from request header
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """
    Determine the best match for supported timezones based on the request.
    Order of priority:
    1. Timezone from URL parameters
    2. Timezone from user settings
    3. Default timezone

    Returns:
        str: The best match timezone.
    """
    # Timezone from URL parameters
    timezone = request.args.get('timezone')
    if timezone:
        try:
            return str(pytz.timezone(timezone))
        except UnknownTimeZoneError:
            pass

    # Timezone from user settings
    if g.user:
        user_timezone = g.user.get('timezone')
        if user_timezone:
            try:
                return str(pytz.timezone(user_timezone))
            except UnknownTimeZoneError:
                pass

    # Default timezone
    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def index() -> str:
    """
    Render the index.html template.

    Returns:
        str: Rendered HTML content of the index template.
    """
    user_timezone = pytz.timezone(get_timezone())
    current_time = datetime.now(user_timezone).strftime('%c')
    return render_template('7-index.html', current_time=current_time)


if __name__ == '__main__':
    app.run(debug=True)
