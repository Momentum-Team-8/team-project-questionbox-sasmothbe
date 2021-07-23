from django.db import models
from accounts.models import UserAccount
### CONTENT TYPE
from django.contrib.contenttypes.models import ContentType

from questions.models import Question

# Create your models here.

class Answer(models.Model):
    answer_author = models.ForeignKey(UserAccount, on_delete=models.CASCADE,
                    related_name="answers",null=True)
    answer = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE,
                               related_name="answers",null=True)

    def __str__(self):
        return f"{self.answer_author.name} {self.question.question}: {self.answer.id}"



    ### content type 
    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type
