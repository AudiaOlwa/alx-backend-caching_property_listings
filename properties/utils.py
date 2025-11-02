from django.core.cache import cache
from .models import Property
import logging

def get_all_properties():
    # Vérifier si le queryset est déjà en cache
    properties = cache.get('all_properties')
    
    if properties is None:
        # Si pas en cache, récupérer depuis la DB
        properties = list(Property.objects.all().values('id', 'title', 'price', 'location'))
        # Stocker en cache pour 1 heure (3600 secondes)
        cache.set('all_properties', properties, 3600)
    
    return properties


logger = logging.getLogger(__name__)

def get_redis_cache_metrics():
    """
    Récupère et log les métriques Redis : hits, misses, hit ratio
    """
    client = cache.client.get_client(write=True)
    stats = client.info('stats')

    hits = stats.get('keyspace_hits', 0)
    misses = stats.get('keyspace_misses', 0)
    total_requests = hits + misses
    hit_ratio = hits / total_requests if total_requests > 0 else 0

    # Log metrics correctement
    logger.info(f"Redis Cache Metrics: Hits={hits}, Misses={misses}, Hit Ratio={hit_ratio:.2f}")

    return {
        'hits': hits,
        'misses': misses,
        'hit_ratio': hit_ratio
    }
