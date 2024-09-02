from django.urls import path
from . import views  # Importe as views do seu aplicativo

urlpatterns = [
    path('/app', views.index, name='index'),  # Rota para a página inicial
    # Adicione outras rotas do seu aplicativo aqui
]
