#!/bin/bash
source ~/miniconda3/bin/activate ubuntu2204VMenv
# 将数据迁移到数据库
python manage.py migrate
printf "没报错的话，数据已经迁移到数据库中了！\n"
