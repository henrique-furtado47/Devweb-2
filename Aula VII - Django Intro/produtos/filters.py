from numbers import Number

from django_filters import FilterSet, NumberFilter

from .models import Produto


class ProdutoFilter(FilterSet):
    preco_minimo = NumberFilter(field_name='preco', lookup_expr='gte')
    preco_maximo = NumberFilter(field_name='preco', lookup_expr='lte')

class Meta:
  model = Produto
  fields = ['preco_minimo', 'preco_maximo', 'estoque']
