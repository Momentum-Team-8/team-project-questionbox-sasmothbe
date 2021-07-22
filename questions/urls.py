from django.urls import path
from questions. views import QuestionDetail, QuestionList


urlpatterns = [
    path('questions', QuestionList.as_view()),
    path('questions/<int:pk>/', QuestionDetail.as_view()),
]
