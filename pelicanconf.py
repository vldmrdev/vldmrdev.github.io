AUTHOR = 'vldmrdev'
SITENAME = 'Blog[under construction]'
SITEURL = "https://vldmrdev.github.io"

PATH = "content"

TIMEZONE = 'Europe/Moscow'

DEFAULT_LANG = 'en'

ARTICLE_PATHS = ["ru", "en"]

THEME = "theme"

DELETE_OUTPUT_DIRECTORY = True

CSS_FILE = "terminal.css"

PLUGINS = ["i18n_subsites"]

JINJA_ENVIRONMENT = {
    "extensions": ["jinja2.ext.i18n"],
}

I18N_SUBSITES = {
    "ru": {
        "SITENAME": "[under construction]",
    },
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 7

# Uncomment following line if you want document-relative URLs when developing
# TODO: for localhost only! back to False!!!
RELATIVE_URLS = True
