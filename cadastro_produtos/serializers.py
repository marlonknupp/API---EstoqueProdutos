from rest_framework import serializers
from .models import Categoria, Produto

# Defina o ProdutoSerializer primeiro
class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'nome', 'descricao', 'preco']

# Agora, defina o CategoriaSerializer
class CategoriaSerializer(serializers.ModelSerializer):
    # Produtos serão serializados normalmente
    produtos = ProdutoSerializer(many=True, read_only=True)
    
    # Subcategorias serão buscadas manualmente
    subcategorias = serializers.SerializerMethodField()

    class Meta:
        model = Categoria
        fields = ['id', 'nome', 'produtos', 'subcategorias', 'parent']

    def get_subcategorias(self, obj):
        # Buscando as subcategorias dessa categoria, que têm 'parent' igual ao id da categoria atual
        subcategorias = Categoria.objects.filter(parent=obj)
        return CategoriaSerializer(subcategorias, many=True).data
