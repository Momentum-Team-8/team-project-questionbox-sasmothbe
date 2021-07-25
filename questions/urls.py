from question_box.settings import DEBUG
from django.urls import path, include
from questions import views




urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('', views.QuestionList.as_view(), name='question-list'),
    path('<int:pk>/', views.QuestionDetail.as_view(), name='question-detail'),
    path('tag/', views.TagList.as_view(), name='tag-list'),
    
]



