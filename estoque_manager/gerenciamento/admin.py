# gerenciamento/admin.py
from django.contrib import admin
from .models import Produto, Fornecedor, Movimentacao, Item, Pedido, Usuario 

# Registrar os modelos para que apareçam no painel de administração
admin.site.register(Produto)
admin.site.register(Fornecedor)
admin.site.register(Movimentacao)
admin.site.register(Item)
admin.site.register(Pedido)
admin.site.register(Usuario)  
