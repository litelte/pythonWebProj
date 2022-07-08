from django.db import models

# Create your models here.
# 这里就可以创建自己的模型

# 继承了models中的Model对象
class Article(models.Model):
    """创建一个文章类的模型"""

    # charField是文本型字符型数据的字段
    # 标题
    title = models.CharField(max_length=30)
    # 内容
    content = models.TextField()
    # 创建好模型，记得配置下
