from django.db.models.base import Model
from rest_framework import serializers
from rest_framework.serializers import HyperlinkedIdentityField, SerializerMethodField

from .models import Answer
from comments.models import Comment

from comments.serializers import CommentSerializer


class AnswerDetailSerializer(serializers.ModelSerializer):
### turn users to show name 
    user = SerializerMethodField()
    ### comments
    comments = SerializerMethodField()
    class Meta:
        model = Answer
        fields = [
            'id',
            'user',
            'answer',
            'created_at',
            'comments',
        ]
    
    def get_user(self,obj):
        return str(obj.answer_author.name)
    

    def get_comments(self, obj):
        ### comment query set

        ### **** this place is great!!! start -- 
        c_qs = Comment.objects.filter(answer_id=obj.id) 
        comments = CommentSerializer(c_qs, many=True).data
        ### **** this place is great!!! end-- 
        return comments


## url
answer_detail_url = HyperlinkedIdentityField(
        view_name='answer_detail',
        lookup_field='pk'
    )

### delete url
answer_delete_url = HyperlinkedIdentityField(
        view_name='answer_delete',
        lookup_field='pk'
    )


class AnswerCreateSerializer(serializers.ModelSerializer):
    url= answer_detail_url 
    delete_url= answer_delete_url 
    
    class Meta:
        model = Answer
        fields = [
            'id',
            'url',
            'delete_url',
            'answer',
        ]


class AcceptAnswerSerializer(serializers.ModelSerializer):
### turn users to show name 
    user = SerializerMethodField()
    class Meta:
        model = Answer
        fields = [
            'id',
            'user'
        ]
    
    def get_user(self,obj):
        #### question author name 
        return str(obj.question.author.name)

