from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

from articleapp.models import Article


def article_ownership_required(func):
    def decorated(request, *args, **kwargs):
        article = Article.objects.get(pk=kwargs['pk'])
        if not article.writer == request.user:            # 작성자와 요청자가 같은지 판단
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated