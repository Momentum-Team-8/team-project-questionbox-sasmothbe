# Generated by Django 3.2.5 on 2021-07-23 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('answers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'ordering': ['accepted', 'created_at']},
        ),
    ]
