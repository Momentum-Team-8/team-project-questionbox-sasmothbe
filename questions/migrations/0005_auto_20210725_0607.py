# Generated by Django 3.2.5 on 2021-07-25 06:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0004_merge_0002_auto_20210723_0209_0003_auto_20210723_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='favorited_by',
            field=models.ManyToManyField(blank=True, related_name='favorite', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='questions', to='questions.Tag'),
        ),
    ]