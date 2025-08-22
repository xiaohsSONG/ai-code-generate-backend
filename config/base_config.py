import os
from datetime import timedelta

class BaseConfig:
    """基础配置类"""
    # Flask 基础配置
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'

    # MySql 数据库配置
    MYSQL_HOST = os.environ.get('MYSQL_HOST') or 'localhost'
    MYSQL_PORT = int(os.environ.get('MYSQL_PORT') or 3306)
    MYSQL_USER = os.environ.get('MYSQL_USER') or 'root'
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD') or '1q2w3e4r'
    MYSQL_DATABASE = os.environ.get('MYSQL_DATABASE') or 'ai_code_generate'
    MYSQL_CHARSET = os.environ.get('MYSQL_CHARSET') or 'utf8mb4'

    #SQLAlchemy配置
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}?charset={MYSQL_CHARSET}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_MAX_OVERFLOW = 20  # 最大溢出连接数
    SQLALCHEMY_POOL_TIMEOUT = 30  # 连接超时时间
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_size': 10,
        'pool_recycle': 3600,
        'pool_pre_ping': True,
        'connect_args': {
            'charset': MYSQL_CHARSET,
            'use_unicode': True
        }
    }

    # # JWT配置
    # JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'jwt-secret-key-change-in-production'
    # JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    # JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
    
    # # Redis配置
    # REDIS_URL = os.environ.get('REDIS_URL') or 'redis://localhost:6379/0'

    # 分页配置
    ITEMS_PER_PAGE = 15