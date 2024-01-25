from rest_framework import serializers
from watchlist_app.models import Movie, WatchList, StreamPlatform

class MovieSerializer(serializers.ModelSerializer):

    len_name = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = '__all__'
        # exclude = 

    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Same same no diffrent")
        
        return data

    def validate_name(self, value):
        if len(value) > 10 : 
            raise serializers.ValidationError("Name to long")
        else : 
            return value
        
    def get_len_name(self, object):
        return len(object.name)
    

class WatchListSerializer(serializers.ModelSerializer):

    class Meta:
        model = WatchList
        fields = '__all__'
        # exclude = 

class StreamPlatformSerializer(serializers.ModelSerializer):

    watchlist = WatchListSerializer(many =True, read_only = True)

    class Meta:
        model = StreamPlatform
        fields = '__all__'
        # exclude = 


    





# class MovieSerializer(serializers.Serializer):

#     id = serializers.IntegerField(read_only =True)
#     name = serializers.CharField()
#     description = serializers.CharField()
#     active = serializers.BooleanField()


#     def create(self , validated_data): ## POST 
#         return Movie.objects.create(**validated_data)
    

#     def update(self, instance ,validated_data):  ##put
#         instance.name = validated_data.get('name' , instance.name)
#         instance.description = validated_data.get('description' , instance.description)
#         instance.active = validated_data.get('active' , instance.active)
#         instance.save()
#         return instance
    
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Same same no diffrent")
        
#         return data

#     def validate_name(self, value):
#         if len(value) > 10 : 
#             raise serializers.ValidationError("Name to long")
#         else : 
#             return value