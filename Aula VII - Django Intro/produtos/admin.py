from django.contrib import admin

from .models import Produto


# Register your models here.
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "preco", "estoque", "categoria", "criado_em", "atualizado_em")
    search_fields = ("nome",)
    list_filter = ("criado_em", "atualizado_em")

