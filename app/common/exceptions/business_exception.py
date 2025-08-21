from app.common.enum.error_code import ErrorCode

class BusinessException(Exception):
    """业务异常类，用于包装业务逻辑中的错误"""
    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message
        super().__init__(message)

    @classmethod
    def from_error_code(cls, error_code: ErrorCode, message:str):
        """根据错误码创建业务异常"""
        if message is None:
            message = error_code.message
        return cls(error_code.code, message)