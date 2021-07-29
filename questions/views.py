from rest_framework.permissions import AllowAny, IsAuthenticated
from questions.permissions import QuestionIsOwnerOrReadOnly
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

from rest_framework.parsers import JSONParser, FileUploadParser
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied, ParseError
from rest_framework.decorators import action
from rest_framework.generics import (
    get_object_or_404
)

# Create your views here.
        

### create quesstion 
class QuestionCreate(generics.CreateAPIView):
    queryset = Question.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = QuestionCreateSerializer

    

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class QuestionList(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionListSerializer
    permission_classes = (AllowAny, )
    
    


## search parts 
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = [ 'title', 'tag' ]
    

class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionDetailSerializer
    permission_classes = [QuestionIsOwnerOrReadOnly]


class TagList(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer



