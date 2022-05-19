from django.urls import path

# from articleapp.views import article_detail, article_list
# 引用当前目录
from . import views

""" 该文件被项目种urls.py引用 """
urlpatterns = [
    # localhost:8000/article/1
    path("<int:article_id>", views.article_detail, name="article_detail"),
    # localhost:8000/article/
    path("", views.article_list, name="article_list"),
]
