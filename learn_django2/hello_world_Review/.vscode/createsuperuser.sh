#!/bin/bash
# 创建django管理员用户
source ~/miniconda3/bin/activate ubuntu2204VMenv
python manage.py createsuperuser
