from flask_cors import cross_origin
from modules.software.blueprints.nodejs import nodejs_app
from flask import Blueprint
from flask import jsonify
from .models import Software
from .models import db


software_app = Blueprint('software', __name__)
software_app.register_blueprint(nodejs_app, url_prefix='/software', cli_group='software')

@cross_origin()
def setup(app, **kwargs):
    db.create_all()

@software_app.route('/')
# @auth_required
def get_softwares():
    data = Software.query.all()
    softwares = jsonify([i.serialize for i in data])

    return softwares

