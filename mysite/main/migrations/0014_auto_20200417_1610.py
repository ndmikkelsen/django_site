# Generated by Django 3.0.5 on 2020-04-17 16:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20200417_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_publish',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 17, 16, 10, 49, 511088), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_publish',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 17, 16, 10, 49, 510731), verbose_name='date published'),
        ),
    ]
