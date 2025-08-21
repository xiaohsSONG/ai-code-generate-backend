from app.common.enum.error_code import ErrorCode
import app.common.utils.throw_utils
from app.common.enum.error_code import ErrorCode
from app.common.exceptions.business_exception import BusinessException
from app import db
from app.common.utils.common_utils import CommonUtils
from app.common.utils.result_utils import ResultUtils
from app.resources import CommonResource
from app.models.user import UserModel

throw_if = app.common.utils.throw_utils.throw_if
throw_if_error_code = app.common.utils.throw_utils.throw_if_error_code

class RegisterResource(CommonResource):
    def post(self):
        args = self.get_parser_args([
            dict(key='userAccount', required=True, type=str, help='userAccount'),
            dict(key='userPassword', required=True, type=str, help='userAccount'),
            dict(key='checkPassword', required=True, type=str, help='userAccount'),
        ])

        throw_if_error_code(args is None, ErrorCode.PARAMS_ERROR)
        user_account = args['userAccount']
        user_password = args['userPassword']
        check_password = args['checkPassword']
        #1、参数校验
        if not all([user_account, user_password, check_password]):
            raise BusinessException.from_error_code(ErrorCode.PARAMS_ERROR,"参数为空")
        if len(user_account) < 4:
            raise  BusinessException.from_error_code(ErrorCode.PARAMS_ERROR,"用户账号过短")
        if len(user_password) < 8 or len(check_password) < 8:
            raise BusinessException.from_error_code(ErrorCode.PARAMS_ERROR, "用户密码过短")
        if user_password != check_password:
            raise BusinessException.from_error_code(ErrorCode.PARAMS_ERROR, "两次输入的密码不一致")
        #2、检查是否重复
        existing_user  = UserModel.query.filter_by(userAccount=user_account).first()
        if existing_user:
            raise BusinessException.from_error_code(ErrorCode.PARAMS_ERROR, "该账号已被注册")
        #3、密码加密
        hashed_password = CommonUtils.get_encrypt_password(user_password)
        #4、将数据插入数据库
        new_user = UserModel(user_account, hashed_password)
        try:
            db.session.add(new_user)
            db.session.commit()
            ret = {"userId": new_user.id}
        except Exception as e:
            db.session.rollback()  # 出错时回滚
            raise BusinessException.from_error_code(ErrorCode.SYSTEM_ERROR, "注册失败：" + str(e))
        return ResultUtils.success(ret)