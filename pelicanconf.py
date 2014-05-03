#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'gsoc'
SITENAME = u''
SITEURL = ''
AVATAR_IMG = ''

TIMEZONE = 'US/Central'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None

TAG_FEED_ATOM = "feeds/tag_%s.atom.xml"

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

PLUGIN_PATH = '/Users/marcus/Downloads/pelican-plugins'
PLUGINS = ['assets']

THEME = "theme"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
