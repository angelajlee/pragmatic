from accountapp.urls import app_name
from django.urls import path

from commentapp.migrations.views import CommentCreateView

app_name = 'commentapp'

urlpatterns = [
    path('create/', CommentCreateView.as_view(), name='create'),
]