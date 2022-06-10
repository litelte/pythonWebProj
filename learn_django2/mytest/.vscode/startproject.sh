#!/bin/bash
# 判断要创建的项目文件是否已存在
read -p "输入你想要创建的项目名：" projName
if [ -d $projName ]; then

    printf "$projName已经存在，请重新检查\n"
    exit 1

fi
# 脚本中调用conda的方式
source ~/miniconda3/bin/activate ubuntu2204VMenv
# 注意，一定要加那个点. 
django-admin startproject $projName .
