from django.shortcuts import render
from questions.models import Question, Tag
from questions.serializers import (
    QuestionCreateSerializer,
    TagSerializer,
    QuestionListSerializer,
    QuestionDetailSerializer
)
from rest_framework import generics
from rest_framework import filters


# Create your views here.

### create quesstion 
class QuestionCreate(generics.CreateAPIView):
    queryset = Question.objects.all()
    # permission_classes = [IsAuthenticated]
    serializer_class = QuestionCreateSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



class QuestionList(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionListSerializer


## search parts 
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = [ 'title', 'tag' ]

class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionDetailSerializer

class TagList(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
