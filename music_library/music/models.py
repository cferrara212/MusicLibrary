from django.db import models

# Create your models here.

class Song(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    album = models.CharField(max_length=50)
    release_date = models.DateTimeField(auto_now_add=True)
    genre = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.title