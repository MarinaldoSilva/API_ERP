from rest_framework.exceptions import AuthenticationFailed, APIException
"""importando as exceptions e api exeception para escrever api´s personalizadas"""
from .models import User
from companies.models import Enterprise, Employee
from django.contrib.auth.hashers import check_password, make_password
"""Libs para checar uma senha e criar uma senha"""

class Authentication():
    """vamos criar o metodo signin, onde vai ser recebido quem chamou(self)"""
    def signin(self, email, password) -> User:
        """a função esta tipada (-> User) pois o retorno dela sempre será um usuário"""
        exception_auth = AuthenticationFailed("Email ou senha não estão corretos, verifique e tente novamente")

        """1º filtrar para saber se o email já existe, pois o email é algo único no cadastro"""
        user_exists = User.objects.filter(email=email).exists()
               
        """verifica se a senha do usuário passou é a mesma cadastrada"""
        if not user_exists:
            raise exception_auth
        
        """o email passou da primeira validação, agora vamos pegar esse email"""
        user = User.objects.filter(email=email).first()

        """verificando a senha"""
        if not check_password(password, user.password):
            raise exception_auth

        """a senha está ok, e usuário(email cadastrado) esta ok, podemos retornar o obj usuário 
        completo com email, senha, id, username e etc, isso já esta pré-definido no AbstractUser"""
        return user
    

    """função de cadastro de usuário no sistema, type_account="owner" é para saber se você é ou não o dono da empresa ou se é um empregado, e todo empregado tem uma mepresa, que nesse caso é o company_id"""
    def signup(self, name, email, password, type_account="owner", company_id=False):

        """mensagem padrão para campos name, email e password vazios"""
        singup_auth_api_exception = APIException("O campo não pode ser nulo/vazio")

        """email, nome e senha não podem ser vazios ou nulos"""
        if not name or name == "":
            raise singup_auth_api_exception
        elif not email or email == "":
            raise singup_auth_api_exception
        elif not password or password == "":
            raise singup_auth_api_exception
        
        """checando se email já exite no banco"""
        """a variavel user vai receber a coleção de dados de User"""
        user = User
        """retorna um booleando True caso email exista e false caso não"""
        if user.objects.filter(email=email).exists():
            raise APIException("Email já cadastrado!")
        
        """recebe a senha passada por parametro e faz a criaptografia pelo check_password"""
        passaword_hashed = check_password(password)

        """vinculando a força um funcionario ter uma empresa"""
        if type_account == 'employee' and not company_id:
            raise APIException("Todo funcionário tem que estar vinculado a uma empresa")

        if type_account == "is_owner":
            """na criação do usuário e empresa vamos usar o metodo create(). nele vamos passar a lista de elementos que o usuário/empresa tem"""

            create_enterprise = Enterprise.objects.create(
                name = "nome da mepresa",
                user_id = create_user.id
                #o usuário assim que for criado na empresa vai receber o id que foi garado
            )

        if type_account == "employee":
            create_employee = Employee.create(
                user_id = create_user.id,#esse id é como se fosse um cracha
                enterprise_id = company_id or create_enterprise.id
                #se a compania for nula, vamos pegar o valor que foi criado na create_enterprise
            )

        create_user = User.objects.create(
            name = name,
            email = email, 
            #a senha foi criptografada pelo meu metodo check_password, vamos adicionar o hashed no banco
            password = passaword_hashed,
            #se employee recebe zero, se dono recebe 1
            is_owner = 0 if type_account == 'is_owner' else 1 
        )
    
