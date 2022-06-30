from flask import Blueprint

php_app = Blueprint('php', __name__)


from .services import *
from .cli import *


def setup():
    db.create_all()