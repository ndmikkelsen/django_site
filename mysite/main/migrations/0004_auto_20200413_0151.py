# Generated by Django 3.0 on 2020-04-13 01:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200413_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_publish',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 13, 1, 51, 10, 195004, tzinfo=utc), verbose_name='date published'),
        ),
    ]
