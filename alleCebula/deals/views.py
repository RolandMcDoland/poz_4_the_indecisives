from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def deals(request):
    template = loader.get_template('propozycje/zero/productList.html')
    return HttpResponse(template.render(request))