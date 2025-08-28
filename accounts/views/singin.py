from accounts.auth import Authentication
from accounts.serializers import UserSerializer
from accounts.views.base import Base
from django.http import HttpRequest
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

class Singin(APIView):
    def post(self, request: HttpRequest):
        email = request.data.get('email')
        password = request.data.get('password')

        if not all([email, password]):
            return Response(
                {"detail":"Email e senha são obrigatórios"},
                status=status.HTTP_400_BAD_REQUEST
            )

        authentication = Authentication()
        user = authentication.singin(email=email, password=password)

        if not user:
            return Response(
                {"detail":"Credenciais de usário invalidas"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        base = Base()
        enterprise = base.get_enterprise_user(user.id)
        
        serializer = UserSerializer(user)

        token = RefreshToken.for_user(user)

        return Response({
            "user": serializer.data,
            "enterprise": enterprise,
            "refresh": str(token) ,
            "access_token": str(token.access_token)
        })