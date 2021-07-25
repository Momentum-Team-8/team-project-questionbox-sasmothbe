from django.shortcuts import render
from questions.models import Question, Tag
from questions.serializers import QuestionSerializer, TagSerializer
from rest_framework import generics
from rest_framework import filters


# Create your views here.
class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = [ 'title', 'tag' ]
    

class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    

class TagList(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    
