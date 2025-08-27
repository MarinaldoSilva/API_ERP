from accounts.views.base import Base
from accounts.auth import Authentication
from accounts.serializers import UserSerializer
from rest_framework.response import Response

class Singup(Base):
    def post(self, request):
        name = request.data.get('name')
        email = request.data.get('email')
        password = request.data.get('password')

        authentication = Authentication()
        user = authentication.signup(name=name, email=email,password=password)

        serializer = UserSerializer(user)

        return Response({
            'user':serializer.data
        })