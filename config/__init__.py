from .base_config import BaseConfig

class DevelopmentConfig(BaseConfig):
    """开发环境配置"""
    DEBUG = True
    
class ProductionConfig(BaseConfig):
    """生产环境配置"""
    DEBUG = False
    
class TestingConfig(BaseConfig):
    """测试环境配置"""
    TESTING = True
    MYSQL_DATABASE = 'user_center_test'

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}