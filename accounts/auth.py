#verificar as exessões possiveis de autenticação e APIs
from rest_framework.exceptions import AuthenticationFailed, APIException
#pegar os models de Usuário e empresa
from accounts.models import User
from companies.models import Enterprise, Employee
#criptorgrafia de senha: verificar senha e criar senha 
from django.contrib.auth.hashers import check_password, make_password

"""
vai ter dois metodos singin e signup:1º Entrar -> verifica se o email existe e se a senha é a do email encontrado
2º Cadastrar -> :ver se o email não existe, qual tipo de conta(dono de empresa(vai ter que ter uma empresa para ser dono), funcionario)
"""

class Authentication:
    def singin(self, email, password):
        
        exception = AuthenticationFailed("Email e/ou senha não encontrado")

        #verifica se o email passado no param existe e retorna um boolean, 
        #caso seja False, cai na exception
        user_exists = User.objects.filter(email=email).exists()
    
        if not user_exists: 
            raise exception
        
        #todos os dados do usuario que tem o email passado no param estão aqui, caso exista é claro.
        user = User.objects.filter(email=email).first()
        #verifica se a senha passada no param é igual a senha do usuario que tem o email passado no param
        #user.password é a senha criptografada no banco, é feita a comparação dos hashes
        if not check_password(password, user.password): 
            raise exception
        
        return user

    #função de cadastro
    def signup(self, name, email, password, type_account = 'owner', company_id=False):
        if not name or name == '':#ver se foi deixado em branco ou está vazio
            raise APIException("O nome é obrigatório.")
        if not email or email == '':
            raise APIException("O email é obrigatório.")
        if not password or password == '':
            raise APIException("A senha é obrigatória.")
        
        #employee = funcionario, owner = dono da empresa
        #todo funcionario tem que ter uma empresa onde vai trabalhar
        if type_account == 'employee' and not company_id:
            raise APIException("O ID da empresa é obrigatório para funcionários.")

        user_exists = User.objects.filter(email=email).exists()#email é id unico
        
        if user_exists:
            raise APIException("Já existe um usuário cadastrado com este email.")

        password_hash = make_password(password)

        create_user = User.objects.create(
            name = name,
            username = email,#isso garante que o username sera unico, se não for assi vai ser salvo uma string vazia no banco, e vai dar erro.
            email = email,
            password = password_hash,
            is_owner = 0 if type_account == 'employee' else 1 
        )

        #criando empresa para o dono
        if type_account == 'owner':
            empresa = Enterprise.objects.create(
                name = "Nome da empresa",
                user_id = create_user.id
            )
        
        #criando funcionario para a empresa
        if type_account == 'employee':
           employee = Employee.objects.create(
                empresa_id = empresa.id,
                user_id = create_user.id
           )
        
        return create_user