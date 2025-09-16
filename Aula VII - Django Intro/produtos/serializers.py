from rest_framework.serializers import ModelSerializer, ValidationError

from .models import Categoria, Produto


class ProdutoSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

    def validate_preco(self, preco):
        if preco <= 0:
            raise ValidationError("Preço deve ser maior que 0")
        
    def validate(self, data):
        preco = data.get('preco')
        estoque = data.get('estoque')
        nome = data.get('nome')

        if estoque < 0:
            raise ValidationError('Estoque tem que ser maior que 0')
        
        if nome == "":
            raise ValidationError('O nome não pode ser vazio')
        
        if estoque > 0 and (preco is None or preco <= 0):
            raise ValidationError('Produto com estoque deve ter preço maior que zero.')
        return data

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'