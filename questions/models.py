from django.db import models
from django.db import User
from django.conf import settings
from django.db.models.deletion import CASCADE

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Questions(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=CASCADE)
    favorited_by = models.ManyToManyField(User, related_name='favorited_by')
    created_at = models.DateField()
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
    