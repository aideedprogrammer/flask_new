from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import proj.config
from flask_cors import CORS
import datetime

app = Flask(__name__, instance_relative_config=True)

CORS(app)

config_name = os.getenv('FLASK_CONFIGURATION', 'default')
app.config.from_object(config.config_setting[config_name])  # object-based default configuration
app.config.from_pyfile('flask.cfg', silent=True)  # instance-folders configuration


db = SQLAlchemy(app)
from proj import model

# db.drop_all()
db.create_all()

from proj.views.user import bp_user
app.register_blueprint(bp_user, url_prefix='/user')
