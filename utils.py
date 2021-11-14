import numpy as np
import math
def haversine_distance(lat1, lon1, lat2, lon2):
    """Return the distance in km between two points around the Earth.

    Latitude and longitude for each point are given in degrees.
    """

    distance=2*6371*np.arcsin(math.sqrt(math.sin((lat2-lat1)/2)**2+math.cos(lat1)*math.cos(lat2)*math.sin((lon2-lon1)/2)**2))
    return distance
