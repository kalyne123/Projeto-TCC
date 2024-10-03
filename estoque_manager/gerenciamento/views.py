from django.shortcuts import render, redirect  # Importa funções para renderizar e redirecionar
from django.contrib.auth import login, authenticate  # Importa a função de login e autenticação
from estoque.forms import UserRegistrationForm, CustomAuthenticationForm  # Importa os formulários criados
from gerenciamento.models import Fornecedor, Produto, Movimentacao, Item, Pedido, Usuario  # Importa os modelos

# Função para a página inicial
def home(request):
    return render(request, 'estoque/home.html',{})

# Função para a página de login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']  # Captura o nome de usuário
        password = request.POST['password']  # Captura a senha
        user = authenticate(request, username=username, password=password)  # Autentica o usuário
        if user is not None:  # Se a autenticação for bem-sucedida
            login(request, user)  # Loga o usuário
            return redirect('home')  # Redireciona para a página inicial
    else:
        form = CustomAuthenticationForm()  # Se não for POST, cria um formulário vazio
    
    return render(request, 'estoque/login.html', {'form': form})

# Função para a página de cadastro de usuário
def cadastro_usuario(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Salva o usuário, mas não grava no banco ainda
            user.set_password(form.cleaned_data['password'])  # Define a senha de forma segura
            user.save()  # Salva o usuário no banco de dados
            return redirect('login')  # Redireciona para a página de login após o cadastro
    else:
        form = UserRegistrationForm()  # Se não for POST, cria um formulário vazio
    
    return render(request, 'estoque/cadastro.html', {'form': form})

# Função para listar produtos
def produtos(request):
    produtos = Produto.objects.all()  # Obtém todos os produtos do banco de dados
    return render(request, 'estoque/produtos.html', {'produtos': produtos})

# Função para cadastrar um fornecedor
def cadastro_fornecedor(request):
    if request.method == 'POST':
        # Lógica para cadastrar um novo fornecedor (não implementada aqui)
        return redirect('fornecedores')
    
    return render(request, 'estoque/cadastro_fornecedor.html')

# Função para excluir um fornecedor
def excluir_fornecedor(request, id):
    fornecedor = Fornecedor.objects.get(id=id)  # Busca o fornecedor pelo ID fornecido
    fornecedor.delete()  # Exclui o fornecedor do banco de dados
    return redirect('fornecedores')  # Redireciona para a página de fornecedores

# Função para mostrar histórico de fornecedores
def historico_fornecedores(request):
    fornecedores = Fornecedor.objects.all()  # Busca todos os fornecedores no banco de dados
    return render(request, 'estoque/historico_fornecedores.html', {'fornecedores': fornecedores})

# Função para a página de cadastro de movimentação de estoque
def cadastro_estoque(request):
    if request.method == 'POST':
        # Lógica para cadastrar uma nova movimentação de estoque (não implementada aqui)
        return redirect('estoque')
    
    return render(request, 'estoque/cadastro_estoque.html')

# Função para gerar relatórios
def relatorios(request):
    return render(request, 'estoque/relatorios.html')  # Renderiza o template 'relatorios.html'
