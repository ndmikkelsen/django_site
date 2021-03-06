# Generated by Django 3.0 on 2020-04-13 03:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20200413_0304'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=200)),
                ('blog_content', models.TextField()),
                ('blog_publish', models.DateTimeField(default=datetime.datetime(2020, 4, 13, 3, 16, 24, 903001), verbose_name='date published')),
            ],
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_publish',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 13, 3, 16, 24, 902678), verbose_name='date published'),
        ),
    ]
