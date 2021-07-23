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
        view_name='detail',
        lookup_field='pk'
    )

### delete url
book_delete_url = HyperlinkedIdentityField(
        view_name='delete',
        lookup_field='pk'
    )
class BookCreateSerializer(serializers.ModelSerializer):
    url= book_detail_url 
    delete_url= book_delete_url 
    
    class Meta:
        model = Book
        fields = [
            'url',
            'delete_url',
            'title',
            'slug',
            'author',
            'description',
            'featured',
            'publication_date',
        
        ]