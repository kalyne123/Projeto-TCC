# estoque/urls.py

# Importa a função 'path' para definir as URLs
from django.urls import path
# Importa as views do app de gerenciamento
from gerenciamento import views  # Atualizado para importar de gerenciamento

# Define uma lista de padrões de URL
urlpatterns = [
    path('', views.home, name='home'),  # Rota para a página inicial
    path('cadastro/', views.cadastro_usuario, name='cadastro'),  # Atualizada para a nova view de cadastro de usuário
    path('login/', views.login_view, name='login'),  # Rota para a página de login
    path('produtos/', views.produtos, name='produtos'),  # Rota para a página de produtos
    path('fornecedores/cadastro/', views.cadastro_fornecedor, name='cadastro_fornecedor'),  # Cadastro de fornecedores
    path('fornecedores/excluir/<int:id>/', views.excluir_fornecedor, name='excluir_fornecedor'),  # Excluir fornecedor
    path('fornecedores/historico/', views.historico_fornecedores, name='historico_fornecedores'),  # Histórico de fornecedores
    path('estoque/cadastro/', views.cadastro_estoque, name='cadastro_estoque'),  # Cadastro de estoque
    path('relatorios/', views.relatorios, name='relatorios'),  # Rota para visualizar relatórios
]
