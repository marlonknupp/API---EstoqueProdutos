from django.contrib import admin
from .models import Categoria,Produto

class ProdutoInline(admin.StackedInline):
    model  = Produto
    extra = 1

class CategoriaAdmin(admin.ModelAdmin):
    inlines = [ProdutoInline]   

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Produto)