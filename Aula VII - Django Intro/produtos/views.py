from django.db.models import Model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from .models import Categoria, Produto
from .serializers import CategoriaSerializer, ProdutoSerializer


class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['preco', 'estoque']  # Filtragem exata por preço e estoque
    search_fields = ['nome']  # Busca textual
    ordering_fields = ['nome', 'preco']  # Ordenação
    ordering = ['id']  # Ordenação padrão

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer