# Generated by Django 3.0 on 2020-04-13 01:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200413_0151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutorialseries',
            name='tutorial_category',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='tutorial_series',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='tutorial_slug',
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_publish',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 13, 1, 55, 41, 403365), verbose_name='date published'),
        ),
        migrations.DeleteModel(
            name='TutorialCategory',
        ),
        migrations.DeleteModel(
            name='TutorialSeries',
        ),
    ]
