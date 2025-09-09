from django.db.models import Model
from rest_framework.viewsets import ModelViewSet

from .models import Categoria, Produto
from .serializers import CategoriaSerializer, ProdutoSerializer


class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer