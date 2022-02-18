#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Strong Developer'
SITENAME = 'Pelican Theme'
SITESUBTITLE = "A great blog about old stuff"
SITEURL = 'https://themeexample.com'
#RELATIVE_URLS = True

LOAD_CONTENT_CACHE = True

PATH = 'content'

TIMEZONE = "America/Bogota"

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

CONTACTS = [
    ("Twitter", "twitter", "https://twitter.com/theanalogfox"),
    ("Facebook", "facebook-f", "https://facebook.com/theanalogfox"),
    ("Instagram", "instagram", "https://www.instagram.com/theanalogfox/"),
    ("Email", "envelope", "info@theanalogfox.com"),
]

DEFAULT_PAGINATION = 3

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DEFAULT_DATE = 'fs'
# DIRECT_TEMPLATES = ['index', 'tags']

READERS = {'html':None}

TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''

#SLUGIFY_SOURCE = 'Summary'

ARTICLE_PATHS = ['pages']
ARTICLE_SAVE_AS = '{date}/{slug}.html'
ARTICLE_URL = '{date}/{slug}.html'

THEME = 'future-imperfect'

THEME_STATIC_DIR = 'theme/future-imperfect'

STATIC_PATHS = ['images', 'files']