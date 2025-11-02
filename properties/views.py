from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from .models import Property

@cache_page(60 * 15)
def property_list(request):
    properties = Property.objects.all().values('id', 'title', 'price', 'location')

    data = list(properties)  # convertir QuerySet en liste
    return JsonResponse({"data": data})
