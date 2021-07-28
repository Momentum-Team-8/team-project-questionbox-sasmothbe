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
    IsAuthenticatedOrReadOnly,
)

#### permissions from Answers  -- start 
from answers.permissions import IsOwnerOrReadOnly
from answers.pagination import AnswerLimitOffsetPagination,AnswerPageNumberpagination
#### permissions from Answers  -- end 


from comments.models import Comment
from .serializers import CommentSerializer
                        


#### list all comments
class CommentList(ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = CommentSerializer
    ### pagination 
    pagination_class = AnswerPageNumberpagination

    ## user show the user as requested ****
    def perform_create(self, serializer):
        ## user?
        serializer.save(user=self.request.comment_user)
    
    #### restframe search
    # comments/?search=book&ordeing=title
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['content']
    
    # books/?q=book
    def get_queryset(self, *args, **kwargs):
        queryset_list = Comment.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                    Q(content__icontains=query)
            ).distinct()
        return queryset_list


### comment details 
class CommentDetail(RetrieveAPIView):
    permission_classes = (AllowAny, )
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'
### comment delete   
class CommentDelete(DestroyAPIView):
    ### only owner delete ... 
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

