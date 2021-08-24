from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from articleapp.models import Article
from likeapp.models import LikeRecord


@method_decorator(login_required, 'get')
class LikeArticleView(RedirectView):
    def get(self, request, *args, **kwargs):
        user = request.user
        article = Article.objects.get(pk=kwargs['article_pk'])

        like_record = LikeRecord.objects.filter(user=user,
                                                article=article)
        # 좋아요가 눌러져있다면
        if like_record.exists():
            messages.add_message(request, messages.ERROR, '이미 눌려있습니다.')
            return HttpResponseRedirect(reverse('articleapp:detail',
                                                kwargs={'pk': kwargs['article_pk']}))

        # 좋아요 누르고 db에 바로 저장
        LikeRecord(user=user, article=article).save()
        article.like += 1
        article.save()
        messages.add_message(request, messages.SUCCESS, '좋아요!')
        return super().get(request, *args, **kwargs)

    # 리다이렉 할때 어디로 갈지
    def get_redirect_url(self, *args, **kwargs):
        return reverse('articleapp:detail', kwargs={'pk': kwargs['article_pk']})
