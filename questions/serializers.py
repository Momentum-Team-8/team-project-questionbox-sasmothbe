from answers.models import Answer
from questions. models import Question, Tag
from answers. models import Answer
from answers.serializers import AnswerListNoLinkSerializer
from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField

class QuestionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
            'title',
            'body',
            'favorited_by',
            'tags',
        ]

        extra_kwargs ={
            "author": {'read_only': True }
        }



class QuestionListSerializer(serializers.ModelSerializer):
    user = SerializerMethodField()
    count_favorite = SerializerMethodField()

    class Meta:
        model = Question
        fields = [
            'id',
            'user',
            'title',
            'body',
            'created_at',
            'favorited_by',
            'count_favorite',
            'tags',
        ]

    def get_user(self,obj):
        return str(obj.author.name)

    def get_count_favorite(self,obj):
        return obj.favorited_by.count()


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'


class QuestionDetailSerializer(serializers.ModelSerializer):
### turn users to show name 
    user = SerializerMethodField()
    ### answers
    answers = SerializerMethodField()
    total_answers = SerializerMethodField()
    class Meta:
        model = Question
        fields = [
            'id',
            'user',
            'created_at',
            'title',
            'body',
            'created_at',
            'favorited_by',
            'tags',
            'total_answers',
            'answers',

        ]
    
    def get_user(self,obj):
        return str(obj.author.name)
    

    def get_answers(self, obj):
        ### query set
        q_qs = Answer.objects.filter(question_id=obj.id) 
        answers = AnswerListNoLinkSerializer(q_qs, many=True).data
        return answers

    def get_total_answers(self, obj):
        q_qs = Answer.objects.filter(question_id=obj.id) 
        return q_qs.count()