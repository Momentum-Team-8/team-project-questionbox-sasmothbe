from rest_framework import serializers
from rest_framework.serializers import HyperlinkedIdentityField, SerializerMethodField

from .models import Answer


class AnswerDetailSerializer(serializers.ModelSerializer):
### turn users to show name 
    user = SerializerMethodField()
    class Meta:
        model = Answer
        fields = [
            'user',
            'answer',
            'created_at',
            'accepted',
        ]
    
    def get_user(self,obj):
        return str(obj.answer_author.name)

## url
answer_detail_url = HyperlinkedIdentityField(
        view_name='answer_detail',
        lookup_field='pk'
    )

### delete url
answer_delete_url = HyperlinkedIdentityField(
        view_name='answer_update',
        lookup_field='pk'
    )
class AnswerCreateSerializer(serializers.ModelSerializer):
    url= answer_detail_url 
    delete_url= answer_delete_url 
    
    class Meta:
        model = Answer
        fields = [
            'url',
            'delete_url',
            'accepted',
            'answer',
        ]