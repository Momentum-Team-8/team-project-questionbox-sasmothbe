from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    HyperlinkedIdentityField
)

from .models import Comment

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id',
            'answer',
            'comment_user',
            'content',
            'created_at',
        ]
