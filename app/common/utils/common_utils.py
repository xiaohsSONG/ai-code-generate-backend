import bcrypt

class CommonUtils:
    @staticmethod
    def get_encrypt_password(password):
        # 固定盐值（建议实际项目中从环境变量读取，而非硬编码）
        # bcrypt 要求盐值为字节类型
        SALT = 'salt'.encode('utf-8')
        # 1. 将明文密码转换为字节类型
        password_bytes = password.encode('utf-8')
        # 2. 使用 bcrypt 进行哈希加密（自动处理盐值混合，生成不可逆哈希）
        hashed_bytes = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
        # 3. 将加密后的字节转换为字符串返回（便于存储到数据库）
        return hashed_bytes.decode('utf-8')