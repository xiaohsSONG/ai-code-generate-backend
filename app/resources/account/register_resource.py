from app import db
from app.models.user import UserModel
from flask_restful import Resource, reqparse,request
from flask import Response
from app.common.utils.result_utils import ResultUtils
from app.resources import CommonResource

import app.common.utils.throw_utils
throw_if = app.common.utils.throw_utils.throw_if
throw_if_error_code = app.common.utils.throw_utils.throw_if_error_code

class RegisterResource(CommonResource):
    def post(self):
        