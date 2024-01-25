from django.db import models

# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class StreamPlatform(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=500)
    website = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class WatchList(models.Model):
    title = models.CharField(max_length=50)
    stroyline = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)
    platform = models.ForeignKey(StreamPlatform, on_delete = models.CASCADE , related_name = "watchlist")

    def __str__(self):
        return self.title
