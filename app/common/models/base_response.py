from typing import Generic, TypeVar
from app.common.enum.error_code import ErrorCode


class BaseResponse():
    """基础响应类，统一 API 响应格式"""

    def __init__(self, code: int, data, message: str = ""):
        self.code = code
        self.data = data
        self.message = message

    @classmethod
    def from_error_code(cls, error_code: ErrorCode):
        """从错误码创建响应"""
        return cls(error_code.code, None, error_code.message)

    def to_dict(self) -> dict:
        """转换为字典，用于接口返回"""
        return {
            "code": self.code,
            "data": self.data,
            "message": self.message
        }