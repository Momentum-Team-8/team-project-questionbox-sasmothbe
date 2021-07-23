from __future__ import unicode_literals

from django.conf import settings
from django.urls import reverse
from django.db import models

from accounts.models import UserAccount
from answers.models import Answer


class Comment(models.Model):
    ### answer
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE,
                    related_name="comments",null=True)
    comment_user = models.ForeignKey(UserAccount, on_delete=models.CASCADE,
                    related_name="comments",null=True)
    content     = models.TextField()
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']


    def __unicode__(self):  
        return str(self.comment_user.name)

    def __str__(self):
        ### self.question.title
        return f"{self.comment_user.name} answer id:{self.answer} comment id:{self.id}"

    def get_absolute_url(self):
        return reverse("comments:thread", kwargs={"id": self.id})

    def get_delete_url(self):
        return reverse("comments:delete", kwargs={"id": self.id})
        




