from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from config import config

db = SQLAlchemy()
migrate = Migrate()
cors = CORS()

def create_app(config_name='development'):
    """应用工厂函数"""
    flask_app = Flask(__name__)
    # 加载配置
    flask_app.config.from_object(config[config_name])

    # 初始化扩展
    db.init_app(flask_app)
    migrate.init_app(flask_app, db)
    cors.init_app(flask_app)

    # 注册蓝图
    from app.routes import api_bp
    flask_app.register_blueprint(api_bp)

    return flask_app