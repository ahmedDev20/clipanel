from flask import Blueprint
from flask.cli import AppGroup

java_app = Blueprint('java', __name__)
java_cli = AppGroup('java')
java_app.cli.add_command(java_cli)

from .services import *
from .cli import *