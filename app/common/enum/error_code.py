from enum import Enum

class ErrorCode(Enum):
    SUCCESS = (0,"OK")
    PARAMS_ERROR = (40000, "请求参数错误")
    NOT_LOGIN_ERROR = (40100, "未登录")
    NO_AUTH_ERROR = (40101, "无权限")
    NOT_FOUND_ERROR = (40400, "请求数据不存在")
    FORBIDDEN_ERROR = (40300, "禁止访问")
    SYSTEM_ERROR = (50000, "系统内部异常")
    OPERATION_ERROR = (50001, "操作失败")
    
    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message

    @property
    def code(self) -> int:
        return self._code
    
    @code.setter
    def code(self, code: int):
        self._code = code

    @property
    def message(self) -> str:
        return self._message
    
    @message.setter
    def message(self, message: str):
        self._message = message