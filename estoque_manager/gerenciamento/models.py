# gerenciamento/models.py

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Gerenciador personalizado para o modelo Usuario
class UsuarioManager(BaseUserManager):
    def create_user(self, nome, email, senha=None):
        # Cria um novo usuário com email e senha
        if not email:
            raise ValueError('O email deve ser fornecido')  # Garante que o email seja fornecido
        usuario = self.model(
            nomeUsuario=nome,
            emailUsuario=self.normalize_email(email),  # Normaliza o email para garantir consistência
        )
        usuario.set_password(senha)  # Aplica o hashing à senha para segurança
        usuario.save(using=self._db)  # Salva o novo usuário no banco de dados
        return usuario

    def create_superuser(self, nome, email, senha):
        # Cria um superusuário com permissões administrativas
        usuario = self.create_user(
            nome,
            email,
            senha=senha,
        )
        usuario.is_admin = True  # Marca o usuário como admin
        usuario.save(using=self._db)  # Salva o superusuário no banco de dados
        return usuario

# Tabela para armazenar informações de usuários
class Usuario(AbstractBaseUser):
    IDUsuario = models.AutoField(primary_key=True)  # Identificador único do usuário
    nomeUsuario = models.CharField(max_length=50)  # Nome do usuário
    emailUsuario = models.EmailField(max_length=100, unique=True)  # E-mail do usuário, deve ser único

    # Campos adicionais para controle de acesso
    is_active = models.BooleanField(default=True)  # Marca se o usuário está ativo
    is_admin = models.BooleanField(default=False)  # Marca se o usuário é administrador

    objects = UsuarioManager()  # Adiciona o gerenciador personalizado

    USERNAME_FIELD = 'emailUsuario'  # Define o campo que será usado para login
    REQUIRED_FIELDS = ['nomeUsuario']  # Campos obrigatórios para criação de usuário

    def __str__(self):
        return self.nomeUsuario  # Retorna o nome do usuário como representação do objeto

    def has_perm(self, perm, obj=None):
        # Verifica se o usuário tem permissão para um determinado perm
        return True

    def has_module_perms(self, app_label):
        # Verifica se o usuário tem permissão para um módulo
        return True

    @property
    def admin(self):
        # Propriedade para verificar se é admin
        return self.is_admin

# Tabela para armazenar produtos
class Produto(models.Model):
    IDProduto = models.AutoField(primary_key=True)  # Identificador único do produto
    nomeProduto = models.CharField(max_length=50)  # Nome do produto
    descricaoProduto = models.CharField(max_length=50)  # Descrição do produto
    precoProduto = models.DecimalField(max_digits=10, decimal_places=2)  # Preço do produto
    quantEstoque = models.FloatField()  # Quantidade disponível em estoque

    def __str__(self):
        return self.nomeProduto  # Retorna o nome do produto como representação do objeto

# Tabela para armazenar fornecedores
class Fornecedor(models.Model):
    IDFornecedor = models.AutoField(primary_key=True)  # Identificador único do fornecedor
    nomeFornecedor = models.CharField(max_length=50)  # Nome do fornecedor
    DDDfornecedor = models.CharField(max_length=50)  # DDD do telefone do fornecedor
    numeroFornecedor = models.CharField(max_length=50)  # Número do telefone do fornecedor
    enderecoFornecedor = models.CharField(max_length=50)  # Endereço do fornecedor
    emailFornecedor = models.CharField(max_length=50)  # E-mail do fornecedor

    def __str__(self):
        return self.nomeFornecedor  # Retorna o nome do fornecedor como representação do objeto

# Tabela para registrar movimentações de estoque
class Movimentacao(models.Model):
    IDMovimentacao = models.AutoField(primary_key=True)  # Identificador único da movimentação
    tipoMovimentacao = models.CharField(max_length=50)  # Tipo de movimentação (entrada/saída)
    quantMovimentacao = models.FloatField()  # Quantidade movimentada
    dataMovimentacao = models.DateField()  # Data da movimentação
    observacaoMovimentacao = models.CharField(max_length=50)  # Observações sobre a movimentação
    fk_Produtos_IDProduto = models.ForeignKey(Produto, on_delete=models.RESTRICT)  # Chave estrangeira referenciando Produtos

    def __str__(self):
        return f'{self.tipoMovimentacao} - {self.quantMovimentacao}'  # Retorna uma string representativa da movimentação

# Tabela para armazenar itens em pedidos
class Item(models.Model):
    IDItens = models.AutoField(primary_key=True)  # Identificador único do item
    quantItens = models.FloatField()  # Quantidade de itens
    precoUniItens = models.DecimalField(max_digits=10, decimal_places=2)  # Preço unitário dos itens
    fk_Produtos_IDProduto = models.ForeignKey(Produto, on_delete=models.RESTRICT)  # Chave estrangeira referenciando Produtos

    def __str__(self):
        return f'{self.quantItens} de {self.precoUniItens}'  # Retorna uma string representativa do item

# Tabela para registrar pedidos
class Pedido(models.Model):
    IDPedido = models.AutoField(primary_key=True)  # Identificador único do pedido
    fk_Produtos_IDProduto = models.ForeignKey(Produto, on_delete=models.CASCADE)  # Chave estrangeira referenciando Produtos
    fk_Fornecedores_IDFornecedor = models.ForeignKey(Fornecedor, on_delete=models.RESTRICT)  # Chave estrangeira referenciando Fornecedores
    datPedido = models.DateField()  # Data do pedido
    horarioPedido = models.CharField(max_length=50)  # Horário do pedido
    totalPedido = models.FloatField()  # Total do pedido

    def __str__(self):
        return f'Pedido {self.IDPedido} - Total: {self.totalPedido}'  # Retorna uma string representativa do pedido
