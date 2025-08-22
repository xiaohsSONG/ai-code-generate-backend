from passlib.hash import bcrypt
from .random_string import random_string

class CommonUtils:

    @staticmethod
    def generate_salt():
        return random_string(22)
    
    @staticmethod
    def generate_password_hash(salt, password):
        return bcrypt.using(ide)
    @staticmethod
    def get_safe_user(user):
        if not user:
            return None
        return {
            "id": user.id,
            "userAccount": user.userAccount,
            "userName": user.userName,
            "userAvatar": user.avatarUrl,
            "userProfile": user.profile,
            "userRole": user.userRole,
            "createTime": user.createTime,
        }