from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("Bem vindo a BSI4 Store!")

def sobre(request):
    return HttpResponse("Loja feita em Django")
