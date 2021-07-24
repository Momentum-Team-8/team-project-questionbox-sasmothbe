from django.shortcuts import render
from questions.models import Question, Tag
from questions.serializers import QuestionSerializer
from rest_framework import generics
from rest_framework import filters


# Create your views here.
class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = [ 'title' ]

class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
