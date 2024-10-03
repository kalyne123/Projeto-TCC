# estoque_manager/urls.py
# Importa a classe admin do Django para gerenciar o painel administrativo
from django.contrib import admin
# Importa funções para definir rotas e incluir URLs de outros arquivos
from django.urls import path, include

# Define uma lista de padrões de URL
urlpatterns = [
    # Rota para o painel administrativo do Django
    path('admin/', admin.site.urls),
    
    # Inclui as URLs definidas no arquivo 'estoque.urls'
    path('', include('estoque.urls')),  # Incluindo as URLs do app estoque
]
