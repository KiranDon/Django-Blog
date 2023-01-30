from django.db import models
from datetime import datetime
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000000)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    author = models.CharField(max_length=100)

    def split_content(self):
        return self.content.split("\n")

class Comment(models.Model):
    comment_by = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    comment = models.CharField(max_length=100000)