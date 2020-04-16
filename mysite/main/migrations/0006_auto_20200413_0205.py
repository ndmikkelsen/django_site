# Generated by Django 3.0 on 2020-04-13 02:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200413_0155'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('shirt_size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=1)),
            ],
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_publish',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 13, 2, 5, 20, 68933), verbose_name='date published'),
        ),
    ]