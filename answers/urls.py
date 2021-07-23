from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from .views import (
    AnswerList,
    AnswerDetail,
    AnswerDelete,
    AnswerUpdate
)

urlpatterns = [
    path('', AnswerList.as_view(), name='answer_list'),
    path('<int:pk>/', AnswerDetail.as_view(), name='answer_detail'),
    path('<int:pk>/edit/', AnswerUpdate.as_view(), name='answer_update'),
    path('<int:pk>/delete/', AnswerDelete.as_view(), name='answer_delete'),
]