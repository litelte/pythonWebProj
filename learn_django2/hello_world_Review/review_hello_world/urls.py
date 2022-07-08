"""review_hello_world URL Configuration

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
# 再次导入re_path
from django.urls import path, re_path

# 得先导入，才能使用
from . import views

# from ..review_hw_app import views

# 这个文件是负责全局路由设置的，路由处理请求，最后响应请求，并返回内容views
# patterns是模式的意思，这里就是url模式
urlpatterns = [
    path("admin/", admin.site.urls),
    # path方法的格式：（页面，方法）
    path("", views.index),
    # 这里是re_path的写法
    # re_path(" ^$", views.index),
]
