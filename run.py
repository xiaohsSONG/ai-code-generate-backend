from app import create_app
import sys
sys.dont_write_bytecode = True

def main():
    # 创建应用实例（这里会自动执行数据库连接检查）
    app = create_app()
    # 启动应用
    app.run(debug=True, host='0.0.0.0', port=5000)

if __name__ == '__main__':
    main()