# serializers.py
from rest_framework import serializers
from .models import Categoria, Produto

# Defina o ProdutoSerializer primeiro
class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'nome', 'descricao', 'preco', 'categoria']

# Agora, defina o CategoriaSerializer
class CategoriaSerializer(serializers.ModelSerializer):
    produtos = ProdutoSerializer(many=True, read_only=True)

    class Meta:
        model = Categoria
        fields = ['id', 'nome', 'produtos']
