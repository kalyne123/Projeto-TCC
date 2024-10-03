# estoque/forms.py
from django import forms  # Importa a classe de formulários do Django para criação de formulários personalizados.
from gerenciamento.models import Usuario  # Importa o modelo Usuario que foi criado anteriormente.
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm  # Importa formulários padrão de criação e autenticação de usuários.

# Formulário para registro de novos usuários.
class UserRegistrationForm(UserCreationForm):
    # Campo de senha, exibido como um campo de entrada oculto.
    password1 = forms.CharField(widget=forms.PasswordInput)  
    password2 = forms.CharField(widget=forms.PasswordInput)  # Campo para confirmação da senha.

    class Meta:  # Classe interna que define as configurações do formulário.
        model = Usuario  # Especifica que o modelo a ser usado é o Usuario customizado.
        fields = ['nomeUsuario', 'emailUsuario', 'password1', 'password2']  # Define os campos que aparecerão no formulário.

# Formulário de autenticação personalizado (login).
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=50)  # Campo para nome de usuário
    password = forms.CharField(widget=forms.PasswordInput)  # Campo para senha

    class Meta:
        model = Usuario  # Utiliza o modelo Usuario para autenticação.
        fields = ('username', 'password')  # Define os campos que serão utilizados para login.
