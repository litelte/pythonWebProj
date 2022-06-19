#!/bin/bash
# 使用django创建应用
read -p "输入你想要创建的应用名：" appName
if [ -d $appName ]; then

    printf "$appName已经存在，请重新检查\n"
    exit 1

fi
source ~/miniconda3/bin/activate ubuntu2204VMenv
python manage.py startapp $appName
