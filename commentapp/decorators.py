from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

from articleapp.models import Article
from commentapp.models import Comment


def comment_ownership_required(func):
    def decorated(request, *args, **kwargs):
        comment = Comment.objects.get(pk=kwargs['pk'])
        if not comment.writer == request.user:            # 작성자와 요청자가 같은지 판단
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated