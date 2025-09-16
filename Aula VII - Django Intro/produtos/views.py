from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ModelViewSet

from .filters import ProdutoFilter
from .models import Categoria, Produto
from .serializers import CategoriaSerializer, ProdutoSerializer


class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProdutoFilter
    filterset_fields = {
        'estoque': ['exact', 'gte', 'lte']
    }
    search_fields = ['nome']
    ordering_fields = ['nome', 'preco']
    ordering = ['id']
class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer