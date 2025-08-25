from rest_framework.views import APIView
from companies.models import Enterprise

class Base(APIView):
    #dicionario dos dados onde por padrão não é dono da empresa e não tem permissões
    def get_enterprise_user(self, user_id):
        enterprise = {
            "is_owner": False,
            "permissions": []
        }

        """verifica se o user é dono de alguma empresa, e a atribuição é automatica, pois com o exist() retorna um booleano"""
        enterprise["is_owner"] = Enterprise.objects.filter(user_id = user_id).exists()

        if enterprise['is_owner']: return enterprise