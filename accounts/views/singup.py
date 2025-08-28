from rest_framework.views import APIView
from accounts.auth import Authentication
from accounts.serializers import UserSerializer

from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework import status
from django.http import HttpRequest

#cadastro
class Singup(APIView):
    def post(self, request: HttpRequest): #variavel : tipo da variavel
        name = request.data.get('name')
        email = request.data.get('email')
        password = request.data.get('password')
        authentication = Authentication()

        try:
            user = authentication.signup(name=name,email=email,password=password)

            serializer = UserSerializer(user)
            return Response(
                {'user': serializer.data},
                status=status.HTTP_201_CREATED
            )
        
        except APIException as e:
            return Response(
                {'detail': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
