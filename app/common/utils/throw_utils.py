from app.common.exceptions.business_exception import BusinessException
from app.common.enum.error_code import ErrorCode

def throw_if(condition: bool, exception: Exception) -> None:
    """如果条件为真，则抛出业务异常"""
    if condition:
        raise exception

def throw_if_error_code(condition: bool,error_code: ErrorCode) -> None:
    if condition:
        raise BusinessException.from_error_code(error_code)

def throw_if_error_message(condition: bool, error_code: ErrorCode, message: str) -> None:
    """如果条件为真，则抛出错误码对应的业务异常"""
    if condition:
        raise BusinessException.from_error_code(error_code, message)