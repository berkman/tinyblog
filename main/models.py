from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    subject = models.CharField(max_length=200)
    body = models.CharField(max_length=2000)
    user = models.ForeignKey(User)
    post_timestamp = models.DateTimeField('date published')
