# all the imports
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash

# create the application instance
app = Flask(__name__) 
# load config from this file, flaskr.py
app.config.from_object(__name__)
# load default config and overrite config from an environment variable
# don't worry, crawlers, these ate not real username & password :)
app.config.update(dict(
    DATABASE=ps.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envar('FLASKR_SETTINGS', silent=True)
