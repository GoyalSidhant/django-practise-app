# from django.shortcuts import render
# from watchlist_app.models import Movie
# from django.http import JsonResponse
# # Create your views here.


# def movie_list(request):
#     movies = Movie.objects.all()
#     print(movies.values())
#     return JsonResponse({'data': list(movies.values())})


# def movie_details(request,  pk):
#     movie = Movie.objects.get(pk=pk)
#     return JsonResponse({movie}) ## error 

