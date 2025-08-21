from app.common.models.base_response import BaseResponse
from app.common.enum.error_code import ErrorCode

class ResultUtils:
    """响应工具类，用于快速创建成功/失败响应"""

    @staticmethod
    def success(data=None, message: str = "") -> BaseResponse:
        """创建成功响应"""
        return BaseResponse(0, data, message)

    @staticmethod
    def error(error_code: ErrorCode, message: str) -> BaseResponse:
        """通过错误码创建失败响应（支持自定义消息）"""
        if message:
            return BaseResponse(error_code.code, None, message)
        return BaseResponse.from_error_code(error_code)
    
    @staticmethod
    def error_with_code(code: int, message: str) -> BaseResponse:
        """通过自定义错误码和消息创建失败响应"""
        return BaseResponse(code, None, message)