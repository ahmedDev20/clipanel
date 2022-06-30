from flask import Blueprint
from flask.cli import AppGroup

nodejs_app = Blueprint('nodejs', __name__)
nodejs_cli = AppGroup('nodejs')
nodejs_app.cli.add_command(nodejs_cli)


from .services import *
from .cli import *


