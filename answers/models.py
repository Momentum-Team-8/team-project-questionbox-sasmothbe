from django.db import models
from accounts.models import UserAccount
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
        return f"{self.answer_author.name} {self.question.title}: {self.id}"

    class Meta:
        ordering = ["accepted", "created_at"]

