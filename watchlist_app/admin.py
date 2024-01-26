from django.contrib import admin
from watchlist_app.models import Movie , StreamPlatform, WatchList, Review
# Register your models here.
admin.site.register(Movie)
admin.site.register(StreamPlatform)
admin.site.register(WatchList)
admin.site.register(Review)