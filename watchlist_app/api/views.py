from watchlist_app.models import Movie, StreamPlatform, WatchList, Review
from watchlist_app.api.serializer import MovieSerializer, WatchListSerializer, StreamPlatformSerializer, ReviewSerializer
from rest_framework.response import Response
from rest_framework import status, generics, mixins

from rest_framework.views import APIView
class MovieList(APIView):
    
    def get(self , request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    
    def post(self , request): 
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

        

class MovieDetail(APIView):

    def get(self, request, pk):
        try : 
            movie = Movie.objects.get(pk=pk)
            serializer = MovieSerializer(movie)
            return Response(serializer.data)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        

    def put(self , request , pk):
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request , pk):
         movie = Movie.objects.get(pk=pk)
         movie.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)



class WatchListList(APIView):
    
    def get(self , request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        #serializer = WatchListSerializer(movies, many=True, context = {'request':request})
        return Response(serializer.data)
    
    def post(self , request): 
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

        

class WatchListDetail(APIView):

    def get(self, request, pk):
        try : 
            movie = WatchList.objects.get(pk=pk)
            serializer = WatchListSerializer(movie)
            return Response(serializer.data)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        

    def put(self , request , pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request , pk):
         movie = WatchList.objects.get(pk=pk)
         movie.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)
    

class StreamPlatformtList(APIView):
    
    def get(self , request):
        movies = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(movies, many=True)
        return Response(serializer.data)
    
    def post(self , request): 
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

        

class StreamPlatformDetails(APIView):

    def get(self, request, pk):
        try : 
            movie = StreamPlatform.objects.get(pk=pk)
            serializer = StreamPlatformSerializer(movie)
            return Response(serializer.data)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        

    def put(self , request , pk):
        movie = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request , pk):
         movie = StreamPlatform.objects.get(pk=pk)
         movie.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)
    


class ReviewDetail( mixins.RetrieveModelMixin , generics.GenericAPIView):

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request , *args, **kwargs)
    
   
    

class ReviewList(mixins.ListModelMixin , mixins.CreateModelMixin , generics.GenericAPIView):

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request , *args, **kwargs)
    
    def post(self, request , *args , **kwargs):
        return self.create(request, *args, **kwargs)