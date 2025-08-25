from django.db import models
from django.contrib.auth.models import AbstractUser, Permission
from companies.models import Enterprise


class User(AbstractUser):
    #id_user
    nome = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    is_owner = models.BooleanField(default=True)

    #USERNAME_FIELD = 'email'
    
    def __str__(self):
        return f"User: {self.nome} -> {self.email}"
    
#Departamentos 
class Group(models.Model):
    #id_grupo
    nome = models.CharField(max_length=85)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)

#permissão Departamentos 
class GroupPermission(models.Model):
    #id_permissao_do_grupo
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

class UserGroup(models.Model):
    #id_grupo_do_usuario ou listagem 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)