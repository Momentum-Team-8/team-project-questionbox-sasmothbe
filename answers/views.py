from django.core.checks import messages
from django.db.models import Q
## search
from rest_framework.filters import(
    SearchFilter,
    OrderingFilter,
)
from django.db.models import query
from rest_framework.generics import (
    ListAPIView, 
    RetrieveAPIView,
    DestroyAPIView,
    RetrieveUpdateAPIView,
    UpdateAPIView,
    CreateAPIView,
    get_object_or_404
    )
from rest_framework.permissions import(
    AllowAny,
    IsAuthenticatedOrReadOnly,
    IsAuthenticated
)

##### import comments ... start --
from comments.serializers import CommentSerializer
from comments.models import Comment
##### import comments ... end --

from answers.permissions import IsOwnerOrReadOnly

from .models import Answer
from questions.models import Question
from .serializers import (
    AnswerDetailSerializer,
    AnswerCreateSerializer,
    AnswerListSerializer,
    AcceptAnswerSerializer,
    UpdateAnswerSerializer
)

from .pagination import AnswerLimitOffsetPagination,AnswerPageNumberpagination

# Create your views here.


#### Anser create
class AnswerCreate(CreateAPIView):
    queryset = Answer.objects.all()
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticated]
    serializer_class = AnswerCreateSerializer

    def perform_create(self, serializer):
        ### I think here should work !! 
        ## answer_author=Answer.user_author
        serializer.save(answer_author=self.request.user)


###  ** list answers ---- and add/create
class AnswerList(ListAPIView):
    queryset = Answer.objects.all()
    permission_classes = (AllowAny,)
    # queryset = Book.objects.all()
    serializer_class = AnswerListSerializer
    ### pagination 
    pagination_class = AnswerPageNumberpagination

    ## user show the user as requested ****
    def perform_create(self, serializer):
        serializer.save(user=self.request.answer_author)
    
    #### restframe search
    # answers/?search=think
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['answer',]
    
    # answers/?q=answer
    def get_queryset(self, *args, **kwargs):
        queryset_list = Answer.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                    Q(answer__icontains=query)
            ).distinct()
        return queryset_list


### ** Answer details 
class AnswerDetail(RetrieveAPIView):
    permission_classes = (AllowAny, )
    queryset = Answer.objects.all()
    serializer_class = AnswerDetailSerializer

    
### ** Answer delete   
class AnswerDelete(DestroyAPIView):
    ### only author can update and delete ... 
    queryset = Answer.objects.all()
    serializer_class = AnswerCreateSerializer
    permission_classes = [IsOwnerOrReadOnly,IsAuthenticatedOrReadOnly]


### ** Answer update  
### retrive update view gives us pre filled details ... 

### question author can update accept; answer author can update other fields;
class AnswerUpdate(RetrieveUpdateAPIView):
    ### only admin and update and delete ... 
    queryset = Answer.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'pk'

    ### need instance qustion id 
    def get_serializer_class(self):
        ####************* get the instance og the class ... 
        instance = self.get_object()
        ####*************
        if self.request.user == instance.question.author:
            return AcceptAnswerSerializer
        
        if self.request.user == instance.answer_author:
            return UpdateAnswerSerializer




