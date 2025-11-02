from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from .models import Property
from .utils import get_all_properties

@cache_page(60 * 15)
def property_list(request):
    properties = Property.objects.all().values('id', 'title', 'price', 'location')

    data = list(properties)  # convertir QuerySet en liste
    data = get_all_properties()  # récupération avec cache low-level
    return JsonResponse({"data": data})
