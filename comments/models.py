from __future__ import unicode_literals

from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.db import models

from accounts.models import UserAccount


class CommentManager(models.Manager):
    def all(self):
        qs = super(CommentManager, self).filter(parent=None)
        return qs

    def filter_by_instance(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.id
        qs = super(CommentManager, self).filter(content_type=content_type, object_id= obj_id).filter(parent=None)
        return qs

class Comment(models.Model):
    comment_user = models.ForeignKey(UserAccount, on_delete=models.CASCADE,
                    related_name="comments",null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    parent      = models.ForeignKey("self", null=True, blank=True)
    content     = models.TextField()
    created_at  = models.DateTimeField(auto_now_add=True)
    objects = CommentManager()

    class Meta:
        ordering = ['-created_at']


    def __unicode__(self):  
        return str(self.comment_user.name)

    def __str__(self):
        return str(self.comment_user.name)

    def get_absolute_url(self):
        return reverse("comments:thread", kwargs={"id": self.id})

    def get_delete_url(self):
        return reverse("comments:delete", kwargs={"id": self.id})
        
    def children(self): #replies
        return Comment.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True

