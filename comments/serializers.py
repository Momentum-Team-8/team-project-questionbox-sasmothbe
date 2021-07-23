from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField
)

from .models import Comment

class CommentSerializer(ModelSerializer):
    reply_count = SerializerMethodField()
    class Meta:
        model = Comment
        fields = [
            'id',
            'comment_user',
            'content_type',
            'object_id',
            'parent',
            'content',
            'reply_count',
            'created_at',
        ]

    def get_reply_count(self, obj):
        if obj.is_parent:
            return obj.children().count()
        return 0


### for child comments
class CommentChildSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id',
            'comment_user',
            'content',
            'created_at'
        ]


### for comment detail 
class CommentDetailSerializer(ModelSerializer):
    ### child comments
    replies = SerializerMethodField()

    reply_count = SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            'id',
            'comment_user',
            'content_type',
            'object_id',
            'content',
            'reply_count',
            'replies',
            'created_at',
        ]
    
    def get_replies(self, obj):
        if obj.is_parent:
            return CommentChildSerializer(object.children(), many=True).data
        return None


    def get_reply_count(self, obj):
        if obj.is_parent:
            return obj.children().count()
        return 0