#!/bin/bash
source ~/miniconda3/bin/activate ubuntu2204VMenv
# 这是第一步，更新数据库中的已迁移数据
printf "迁移数据库前记得去项目文件夹中的settings.py文件中注册模型哦！\n"
python manage.py makemigrations
printf "更新要迁移的数据后，记得再运行一遍mgr命令，就可以将迁移的数据同步到数据库了\n"
