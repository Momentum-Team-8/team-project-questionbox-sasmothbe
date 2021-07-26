from django.conf.urls import url
from django.contrib import admin

from .views import (
    CommentList,
    CommentDelete,
    CommentDetail,

    )

urlpatterns = [
    url('', CommentList.as_view(), name='list'),
    url('<int:answer_id>/<int:pk>/', CommentDetail.as_view(), name='thread'),
    url('<int:pk>/delete/', CommentDelete.as_view(), name='delete'),
]
