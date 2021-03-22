from django.db import models

# Create your models here.


class Comment(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.IntegerField()
    text = models.CharField(max_length=255)
