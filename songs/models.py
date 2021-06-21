from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Song(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    author = models.ForeignKey(User, blank=False, null=False,  on_delete=models.CASCADE)
    pic = models.ImageField()
    song = models.FileField()

    def __str__(self):
        return self.title
