from accounts.views.base import Base
from accounts.auth import Authentication
from accounts.serializers import UserSerializer

from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

class Singin(Base):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        authentication = Authentication()
        user = authentication.singin(self, email=email, password=password)

        enterprise = self.get_enterprise_user(user.id)
        
        serializer = UserSerializer(user)

        token = RefreshToken.for_user(user)

        return Response({
            "user": serializer.data,
            "enterpize": enterprise,
            "refresh": RefreshToken ,
            "acess_token": token.access_token
        })