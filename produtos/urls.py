from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cadastro_produtos.urls')),  # Inclui as URLs da API
]
