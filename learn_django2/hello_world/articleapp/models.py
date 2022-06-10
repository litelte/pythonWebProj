from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


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
    # 更新字段，创建时间
    # created_time = models.DateTimeField(default=timezone.now)
    # 设置其他的时间方式
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)
    # 设置外键
    # 可以先用框架提供的内置模型：用户
    # 根据id关联，所以default=1
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1)
    # 布尔型
    is_deleted = models.BooleanField(default=False)
    # 数值类型
    readed_num = models.IntegerField(default=0)

    # 修改后台的显示效果，后期模型和模型之间的引用会用到
    # 标注对象是哪个模型，显示一个记录
    def __str__(self):
        return "<Article: %s>" % self.title
