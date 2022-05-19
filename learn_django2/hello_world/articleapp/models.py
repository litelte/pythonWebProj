from turtle import title

from django.db import models


# Create your models here.
# 创建一个文章类，继承了模型库
class Article(models.Model):
    # 字符型的字段
    """
    一个模型，通常来说，对应多个字段
    """
    # 标题字段
    title = models.CharField(max_length=30)
    # 文本字段
    content = models.TextField()
