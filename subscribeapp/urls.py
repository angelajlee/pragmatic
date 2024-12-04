from django.urls import path

from subscribeapp.views import SubscribtionView

app_name = 'subscribeapp'

urlpatterns = [
    path('subscribe/', SubscribtionView.as_view(), name='subscribe'),
]