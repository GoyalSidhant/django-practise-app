from rest_framework.decorators import api_view
from user_app.api.serializer import RegistrationSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from user_app.models import create_auth_token


@api_view(['GET'])
def logout_view(request):
     if request.method == "POST":
         request.user.authtoken.delete()
         return Response(status=200)


@api_view(['POST'])
def registration_view(request):
    if request.method == "POST":
        serializer = RegistrationSerializer(data= request.data)

        data  = {}


        if serializer.is_valid():
            account = serializer.save()
            token = Token.objects.get_or_create(user=account).key
            data['toekn'] = token
        else: 
            data = serializer.errors
        return Response(data)
        
