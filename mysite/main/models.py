from django.db import models
from datetime import datetime


# Create your models here.
class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=200)
    tutorial_content = models.TextField()
    tutorial_publish = models.DateTimeField('date published',
                                            default=datetime.now())


class Blog(models.Model):
    blog_title = models.CharField(max_length=200)
    blog_content = models.TextField()
    blog_publish = models.DateTimeField('date published',
                                        default=datetime.now())


def __str__(self):
    return self.tutorial_title, self.blog_title
