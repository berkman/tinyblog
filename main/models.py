from django.db import models

class User(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    access_level = models.CharField(max_length=10)
    last_login = models.DateTimeField('last_login', auto_now_add=True)
