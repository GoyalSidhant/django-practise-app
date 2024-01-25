
from django.urls import path, include

from watchlist_app.api.views import MovieList, MovieDetail, WatchListList, WatchListDetail, StreamPlatformDetails, StreamPlatformtList

urlpatterns = [
    path('list/', MovieList.as_view(), name  = 'movie-list'),
    path('<int:pk>' , MovieDetail.as_view() , name= 'movie_details'),
    path('watchlist/list/', WatchListList.as_view(), name  = 'watchlist-list'),
    path('watchlist/<int:pk>' , WatchListDetail.as_view() , name= 'watchlist_details'),
    path('streamplatform/list/', StreamPlatformtList.as_view(), name  = 'streamplatform-list'),
    path('streamplatform/<int:pk>' , StreamPlatformDetails.as_view() , name= 'wstreamplatform_details')
]
