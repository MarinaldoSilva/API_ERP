from accounts.views.singin import Singin
from accounts.views.singup import Singup
from django.urls import path

urlpatterns = [
    path('singin/', Singin.as_view()),
    path('singup/', Singup.as_view())
]