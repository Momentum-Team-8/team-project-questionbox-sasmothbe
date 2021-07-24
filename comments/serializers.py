from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    HyperlinkedIdentityField
)

from .models import Comment

class CommentSerializer(ModelSerializer):
    ### turn users to show name 
    user = SerializerMethodField()
    class Meta:
        model = Comment
        fields = [
            'id',
            'user',
            'answer',
            'content',
            'created_at',
        ]

    def get_user(self,obj):
        return str(obj.comment_user.name)