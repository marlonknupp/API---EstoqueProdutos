from django.contrib import admin
from .models import Categoria,Produto

class SubCategoriaInline(admin.TabularInline):
    model = Categoria
    fk_name = "parent"
    extra = 1

class ProdutoInline(admin.StackedInline):
    model  = Produto
    extra = 1

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'parent')
    inlines = [ProdutoInline, SubCategoriaInline]   

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Produto)