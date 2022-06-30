from flask import Blueprint
from flask.cli import AppGroup

python_app = Blueprint('python', __name__)
python_cli = AppGroup('python')
python_app.cli.add_command(python_cli)


from .services import *
from .cli import *