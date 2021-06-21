from django.db import models

# Create your models here.

class Song(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    author = models.CharField(max_length=50, blank=False, null=False)
    pic = models.ImageField()
    song = models.FileField()