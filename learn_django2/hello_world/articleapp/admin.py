from django.contrib import admin

from .models import Article


# Register your models here.
# 使用装饰器注册模型
@admin.register(Article)
# 创建一个类
class ArticleAdmin(admin.ModelAdmin):
    """模型的定制类，用于分辨模型的具体参数"""

    list_display = (
        "id",
        "title",
        "content",
        "created_time",
        "last_updated_time",
        "author",
        "is_deleted",
    )
    # 对模型进行排序
    # ordering = ("id",)
    # 倒序排序就加负号
    ordering = ("-id",)
    # 元组后面必须有逗号


# 注册模型，上面是另外一种方法，使用装饰器
# admin.site.register(Article, ArticleAdmin)
