from django.db.models import Q
## search
from rest_framework.filters import(
    SearchFilter,
    OrderingFilter,
)
from django.db.models import query
from rest_framework.generics import (
    ListCreateAPIView,
    ListAPIView, 
    RetrieveAPIView,
    DestroyAPIView,
    RetrieveUpdateAPIView,
    )
from rest_framework.permissions import(
    AllowAny,
    IsAdminUser,
)

##### import comments ... start --
from comments.serializers import CommentSerializer
from comments.models import Comment


##### import comments ... end --

from .models import Answer
from .serializers import AnswerDetailSerializer,AnswerCreateSerializer

from .pagination import AnswerLimitOffsetPagination,AnswerPageNumberpagination

# Create your views here.


###  list books ---- and add/create
class AnswerList(ListCreateAPIView):
    permission_classes = (AllowAny, )
    # queryset = Book.objects.all()
    serializer_class = AnswerCreateSerializer
    ### pagination 
    pagination_class = AnswerPageNumberpagination

    ## user show the user as requested ****
    def perform_create(self, serializer):
        serializer.save(user=self.request.answer_author)
    
    #### restframe search
    # answers/?search=book&ordeing=answer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['answer']
    
    # books/?q=book
    def get_queryset(self, *args, **kwargs):
        queryset_list = Answer.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                    Q(answer__icontains=query)
            ).distinct()
        return queryset_list

    


### Book details 
class AnswerDetail(RetrieveAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerDetailSerializer

    
### Book delete   
class AnswerDelete(DestroyAPIView):
    ### only admin and update and delete ... 
    queryset = Answer.objects.all()
    serializer_class = AnswerCreateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]


### Book update  
### retrive update view gives us pre filled details ... 
class BookUpdate(RetrieveUpdateAPIView):
    ### only admin and update and delete ... 
    queryset = Answer.objects.all()
    serializer_class = AnswerCreateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]


