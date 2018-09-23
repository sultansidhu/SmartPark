"""
Haversine formula to provide distance of two tuples of (lat, lon).
Author: Wayne Dyck
Taken from: https://gist.github.com/rochacbruno/2883505
"""
import math


def haversine(t1, t2):
    """Calculates earth distance, taking into account the curvature of the earth."""
    lat1, lon1 = t1
    lat2, lon2 = t2
    radius = 6371  # km (Earth's mean radius)

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return d
