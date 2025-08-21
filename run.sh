#!/bin/bash

# 激活虚拟环境
source .venv/bin/activate

# 设置环境变量
export FLASK_ENV=development
export FLASK_APP=run.py

# 启动应用
python run.py