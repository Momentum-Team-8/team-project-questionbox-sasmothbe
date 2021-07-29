from django.db import models
from accounts .models import UserAccount
from django.conf import settings
from django.db.models.deletion import CASCADE
from datetime import date


# Create your models here.


class Tag(models.Model):
    insert = models.CharField(max_length=32)

    def __str__(self):
        return self.insert


class Question(models.Model):
    title = models.CharField(max_length=100, null= True)
    body = models.TextField(blank=True)
    author = models.ForeignKey(UserAccount, on_delete=CASCADE)
    image = models.ImageField(upload_to="images", null=True, blank=True,)
    favorited_by = models.ManyToManyField(UserAccount, blank=True,  related_name='favorite')
    created_at = models.DateField(default=date.today)
    tags = models.ManyToManyField(Tag, related_name='questions', blank=True)


    def __str__(self):
        return self.title

