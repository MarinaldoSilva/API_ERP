from rest_framework.views import APIView
from companies.models import Enterprise, Employee

class Base(APIView):

    def get_enterprise_user(self, user_id):
        enterprise = {
            "is_owner": False,
            "is_employee": False,
            "permissions": []
        }

        is_owner = Enterprise.objects.filter(user_id=user_id).exists()

        if is_owner: 
            enterprise['is_owner'] = is_owner 
            enterprise['permissions'] = ['is_owner']
        else:
            employee = Employee.objects.filter(user_id = user_id).exists()
            if employee:
                enterprise['is_employee'] = employee
                enterprise['permissions'] = ['employee']

        return enterprise