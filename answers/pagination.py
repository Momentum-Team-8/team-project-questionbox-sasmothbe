from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
)

class AnswerLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 10


### pagepagination 
class AnswerPageNumberpagination(PageNumberPagination):
    page_size = 2