from accounts.views.singin import Singin
from accounts.views.singup import Singup
from django.urls import path

urlpatterns = [
    path('singin/', Singin.as_view()),
    path('singup/', Singup.as_view()) 
]
"""é o tipo de requisição HTTP (GET, POST, PUT, DELETE, etc.) que determina qual método dentro da sua classe será executado de forma automatica, por isso não precisamos passar diretamente a função especifica, fora que a as.view() "adapta" a classe para ser lida como uma função(a forma padrão de recebimento), é uma forma comum e moderna"""