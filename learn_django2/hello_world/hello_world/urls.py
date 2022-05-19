"""hello_world URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path

from . import views

# 这是django的特性
# from articleapp.views import article_detail, article_list


# url行为模式
urlpatterns = [
    # 后台管理专用的网址
    path("admin/", admin.site.urls),
    path("", views.index),
    re_path(" $", views.index),
    # 对应views.py的处理方法
    # 引用应用文件夹种的urls路径
    path("articleapp/", include("articleapp.urls")),
]
# 如果使用re_path，就要使用正则表达式$，这是django1.0的写法
# 运行客户端后，客户端会打开path的网页，然后发送请求到urls文件
# urls下来会处理请求，在这里的话，就是使用后面的方法，views.index
# 就是使用views库中的index方法
