from django.urls import path, include
from .views import SignupView

urlpatterns = [
    path('signup', SignupView.as_view()),
    
]

## signin: http://localhost:8000/api/token/???