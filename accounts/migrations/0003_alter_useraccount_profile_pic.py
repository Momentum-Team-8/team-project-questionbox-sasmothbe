# Generated by Django 3.2.5 on 2021-07-25 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_useraccount_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='profile_pic',
            field=models.ImageField(height_field=100, upload_to='', width_field=100),
        ),
    ]
