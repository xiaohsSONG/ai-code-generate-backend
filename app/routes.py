from flask import Blueprint
from flask_restful import Api
from app.resources.account.register_resource import RegisterResource

api_bp = Blueprint('api', __name__, url_prefix='/rec/static')
api = Api(api_bp)

api.add_resource(RegisterResource, '/register')