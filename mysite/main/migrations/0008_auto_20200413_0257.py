# Generated by Django 3.0 on 2020-04-13 02:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200413_0212'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=200)),
                ('blog_content', models.TextField()),
                ('blog_publish', models.DateTimeField(default=datetime.datetime(2020, 4, 13, 2, 57, 14, 880723), verbose_name='date published')),
            ],
        ),
        migrations.DeleteModel(
            name='Musician',
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_publish',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 13, 2, 57, 14, 880378), verbose_name='date published'),
        ),
    ]
