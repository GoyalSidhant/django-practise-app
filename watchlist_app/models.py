from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
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


class Review(models.Model):
    rating = models.PositiveBigIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length = 200, null = True)
    created = models.DateField(auto_now_add=True)
    update = models.DateTimeField(auto_now = True)
    active = models.BooleanField(default=True)
    watchlist = models.ForeignKey(WatchList, on_delete = models.CASCADE, related_name = 'reviews')

    def __str__(self):
        return self.description

   