from enum import Enum
from typing import Optional


class UserRoleEnum(Enum):
    """用户角色枚举类，定义系统支持的用户角色"""
    USER = ("用户", "user")
    ADMIN = ("管理员", "admin")

    def __init__(self, text: str, val: str):
        self.text = text
        self.val = val

    @classmethod
    def get_enum_by_value(cls, value: str) -> Optional["UserRoleEnum"]:
        """根据 value 获取对应的枚举实例"""
        if not value:
            return None
        # 遍历所有枚举值，匹配 value
        for enum_item in cls.__members__.values():
            if enum_item.value == value:
                return enum_item
        return None

