from flask import Blueprint
from flask_restful import Api
from app.resources.account.user_resource import RegisterResource,LoginResource


api_bp = Blueprint('api', __name__, url_prefix='/rec/static')
api = Api(api_bp)

api.add_resource(RegisterResource, '/register')
api.add_resource(LoginResource, '/login')
