from django.core.cache import cache
from .models import Property

def get_all_properties():
    # Vérifier si le queryset est déjà en cache
    properties = cache.get('all_properties')
    
    if properties is None:
        # Si pas en cache, récupérer depuis la DB
        properties = list(Property.objects.all().values('id', 'title', 'price', 'location'))
        # Stocker en cache pour 1 heure (3600 secondes)
        cache.set('all_properties', properties, 3600)
    
    return properties
