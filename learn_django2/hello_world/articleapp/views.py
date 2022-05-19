from multiprocessing import context
from urllib import response

from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render, render_to_response

from .models import Article

# Create your views here.
""" 自定义处理方法 """


def article_detail(request, article_id):
    # 创建article对象
    """try:
        article = Article.objects.get(id=article_id)
        context = {}
        context["article_obj"] = article
        # return render(request, "article_detail.html", context)
        # 简化版的：django3已经把render_to_response废弃，建议用render即可
        return render_to_response("article_detail.html", context)
    except Article.DoesNotExist:
        # return HttpResponse("您访问的文章内容不存在")
        # return Http404() 这个无法运行，应该是作为错误抛出去
        # 应该是用这个，raise Http404抛出异常
        raise Http404"""

    # else:
    # return HttpResponse("文章标题: %s </br>文章内容: %s" % (article.title, article.content))
    # 文章列表内容有限，用户输入超过文章已有数目的数字，网页就会提示报错，解决方法，使用try-except
    """ 重构代码 """
    # pk是主键的缩写，还可以用id
    article = get_object_or_404(Article, pk=article_id)
    context = {}
    context["article_obj"] = article
    return render(request, "article_detail.html", context)


def article_list(request):
    articles = Article.objects.all()
    context = {}
    context["articles"] = articles
    return render(request, "article_list.html", context)
