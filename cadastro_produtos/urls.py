from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProdutoViewSet

router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet)  # O endpoint será /produtos/

urlpatterns = [
    path('api/', include(router.urls)),  # Inclui todos os endpoints da API
]
