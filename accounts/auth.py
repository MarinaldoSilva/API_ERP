from rest_framework.exceptions import AuthenticationFailed, APIException
from django.contrib.auth import authenticate, get_user_model
from companies.models import Enterprise, Employee

User = get_user_model()

class Authentication:

    def singin(self, email, password):        
        user = authenticate(username = email, password=password)

        if not user: 
            raise AuthenticationFailed("Email e/ou senha não encontrado")
        return user   

    def signup(self, name, email, password, type_account = 'owner', company_id=False):     

        if not all([name, email, password]):
            raise APIException("Nome, email e senha são obrigatórios, verifique os campos e tente novamente.")
        
        """todo funcionario tem que ter uma empresa onde vai trabalhar"""
        if type_account == 'employee' and not company_id:
            raise APIException("O ID da empresa é obrigatório para funcionários.")

        user_exists = User.objects.filter(email=email).exists()#email é id unico
        
        if user_exists:
            raise APIException("Já existe um usuário cadastrado com este email.")

        """usamos um create_user para criar usuários, e o create para os demaias"""
        create_user = User.objects.create_user(
            name = name,
            username = email,
            #isso garante que o username sera unico, se não for assi vai ser salvo uma string vazia no banco, e vai dar erro
            email = email,
            password = password,
            #is_owner = 0 if type_account == 'employee' else 1 
            is_owner = (type_account=='owner')#retorna um booleano
        )

        """criando empresa para o dono"""
        if type_account == 'owner':
            empresa = Enterprise.objects.create(
                name = "Nome da empresa",
                user_id = create_user.id
            )
        
        """criando funcionario para a empresa"""
        if type_account == 'employee':
           employee = Employee.objects.create(
                empresa_id = company_id,
                user_id = create_user.id
           )
        
        return create_user