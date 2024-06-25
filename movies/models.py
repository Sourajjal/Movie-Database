from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    director = models.CharField(max_length=100)
    release_date = models.CharField(max_length=4)
    genre = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.CharField(max_length=100)
    upload_time = models.TimeField(auto_now=True)
    poster = models.ImageField(upload_to='posters/', null=True, blank=True)

    def __str__(self):
        return self.title