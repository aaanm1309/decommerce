from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    textos = {"Eu quero colocar varioes textos aqui","Eu vou ver o que eu posso fazer depois"}
    contexto = {'title': 'django E-commerce',
                'textos': textos}
    return render(request, 'index.html', contexto)


def contact(request):
    return render(request, 'contact.html')


def product(request):
    return render(request, 'product.html', )


def product_list(request):
    return render(request, 'product_list.html')


def privacidade(request):
    return render(request, 'privacidade.html')

