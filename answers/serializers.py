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
            "accepted",
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

class AnswerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = [
            #'id',
            'question', 
            'answer',
        ]

        #### user is read only!! ***** this part is nice!!!
        extra_kwargs ={
            "answer_author": {'read_only': True }
        }
        


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


class AnswerListSerializer(serializers.ModelSerializer):
    url= answer_detail_url 
    delete_url= answer_delete_url 
    user = SerializerMethodField()
    question_name = SerializerMethodField()
    
    class Meta:
        model = Answer
        fields = [
            'id',
            'user',
            'question', 
            'question_name',
            'url',
            'delete_url',
            'answer',
            'created_at',
            "accepted",
        ]

    def get_user(self,obj):
        return str(obj.answer_author.name)
    
    def get_question_name(self,obj):
        return str(obj.question.title)


class AnswerListNoLinkSerializer(serializers.ModelSerializer):
    user = SerializerMethodField()
    question_name = SerializerMethodField()
    
    class Meta:
        model = Answer
        fields = [
            'id',
            'user',
            'question', 
            'question_name',
            'answer',
            'created_at',
            "accepted",
        ]

    def get_user(self,obj):
        return str(obj.answer_author.name)
    
    def get_question_name(self,obj):
        return str(obj.question.title)


class AcceptAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = [
            "accepted"
        ]
    ### read_only_field = ("xx")

class UpdateAnswerSerializer(serializers.ModelSerializer):
### turn users to show name 
    class Meta:
        model = Answer
        fields = [
            "answer"
        ]

        extra_kwargs ={
            "answer": {'read_only': True }
        }
    