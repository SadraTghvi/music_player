from django.db import models

# Create your models here.

class Song(models.Model):
    title = models.CharField()
    author = models.CharField()
    pic = models.ImageField()
    song = models.FileField()