# Generated by Django 3.0.5 on 2020-04-17 16:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20200417_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_publish',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 17, 16, 5, 44, 630411), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_publish',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 17, 16, 5, 44, 630086), verbose_name='date published'),
        ),
    ]
