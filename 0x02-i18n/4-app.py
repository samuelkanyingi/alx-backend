#!/usr/bin/env python3
"""
Flask app with Babel integration for i18n and translations.
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _


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


@babel.localeselector
def get_locale() -> str:
    """
    Determine the best match for supported languages based on the request.
    If a locale parameter is present in the request its value is a supported
    locale, use it; otherwise, use the default behavior.

    Returns:
        str: The best match language.
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """
    Render the index.html template.

    Returns:
        str: Rendered HTML content of the index template.
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)
