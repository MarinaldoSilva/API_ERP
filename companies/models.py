from django.db import models
from django.conf import settings

class Enterprise(models.Model):
    #id_empresa
    name = models.CharField(max_length=150)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Employee(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Enterprise, on_delete=models.CASCADE)
