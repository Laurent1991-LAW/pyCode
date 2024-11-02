#!/bin/bash

# 定义虚拟环境和脚本路径
VENV_DIR=".venv"
SCRIPT_PATH="image-processor.py"

# 检查虚拟环境是否存在
if [ ! -d "$VENV_DIR" ]; then
  echo "Virtual environment directory '$VENV_DIR' does not exist. Please create it first."
  exit 1
fi

# 激活虚拟环境
source "$VENV_DIR/bin/activate"

# 检查脚本是否存在
if [ ! -f "$SCRIPT_PATH" ]; then
  echo "Script file '$SCRIPT_PATH' does not exist."
  deactivate
  exit 1
fi

# 运行脚本
python "$SCRIPT_PATH"

# 退出虚拟环境
deactivate