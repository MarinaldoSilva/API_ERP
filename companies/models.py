from django.db import models
from django.conf import settings

"""settings.AUTH_USER_MODEL -> importa as configurações de usuário personalizado que criados no User.user"""

class Enterprise(models.Model):
    #id_empresa
    nome = models.CharField(max_length=150)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

"""todo funcionario vai recebr o id que vem de User_id da classe User e um Id da empresa, pois todo funcionario tem que ter uma empresa"""

class Employee(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Enterprise, on_delete=models.CASCADE)
