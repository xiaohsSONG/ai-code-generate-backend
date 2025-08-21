from app import db
from flask import Blueprint,jsonify
from flask_restful import Api
from sqlalchemy import inspect
import pymysql
from config.base_config import BaseConfig

api_bp = Blueprint('api', __name__, url_prefix='/rec/static')
api = Api(api_bp)

@api_bp.route('/health', methods=['GET'])
def health_check(): 
    """健康检查端点 - 检查数据库连接状态"""
    health_status = {
        'status': 'healthy',
        'timestamp': None,
        'database': {
            'mysql': {'status': 'unknown', 'message': ''},
            'sqlalchemy': {'status': 'unknown', 'message': ''}
        }
    }
    
    try:
        from datetime import datetime
        health_status['timestamp'] = datetime.now().isoformat()
        
        # 检查MySQL连接
        try:
            mysql_conn = pymysql.connect(
                host=BaseConfig.MYSQL_HOST,
                port=BaseConfig.MYSQL_PORT,
                user=BaseConfig.MYSQL_USER,
                password=BaseConfig.MYSQL_PASSWORD,
                database=BaseConfig.MYSQL_DATABASE,
                charset=BaseConfig.MYSQL_CHARSET
            )
            
            # 检查users表
            with mysql_conn.cursor() as cursor:
                cursor.execute("SHOW TABLES LIKE 'users'")
                users_table_exists = cursor.fetchone() is not None
            
            mysql_conn.close()
            
            health_status['database']['mysql'] = {
                'status': 'healthy',
                'message': f'MySQL连接成功，users表{"存在" if users_table_exists else "不存在"}',
                'host': BaseConfig.MYSQL_HOST,
                'port': BaseConfig.MYSQL_PORT,
                'database': BaseConfig.MYSQL_DATABASE,
                'users_table': users_table_exists
            }
            
        except Exception as e:
            health_status['database']['mysql'] = {
                'status': 'unhealthy',
                'message': f'MySQL连接失败: {str(e)}'
            }
            health_status['status'] = 'unhealthy'
        
        # 检查SQLAlchemy连接
        try:
            with db.engine.connect() as connection:
                result = connection.execute(db.text("SELECT 1"))
                result.fetchone()
            
            # 检查表是否存在
            inspector = inspect(db.engine)
            users_table_exists = inspector.has_table('users')
            
            health_status['database']['sqlalchemy'] = {
                'status': 'healthy',
                'message': f'SQLAlchemy连接成功，users表{"存在" if users_table_exists else "不存在"}',
                'users_table': users_table_exists
            }
            
        except Exception as e:
            health_status['database']['sqlalchemy'] = {
                'status': 'unhealthy',
                'message': f'SQLAlchemy连接失败: {str(e)}'
            }
            health_status['status'] = 'unhealthy'
            
    except Exception as e:
        health_status['status'] = 'error'
        health_status['error'] = str(e)
    
    return jsonify(health_status)