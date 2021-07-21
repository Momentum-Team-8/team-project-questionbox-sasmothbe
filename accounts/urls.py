from django.urls import path
from .views import SignupView

urlpatterns = [
    path('signup', SignupView.as_view()),
]

## signin: http://localhost:8000/api/token/