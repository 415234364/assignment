import numpy as np
import math
def validation(latitude,lontitude):
    if latitude>90 or latitude<-90 or lontitude>180 or lontitude<-180:
        return False
    return True
def haversine_distance(lat1, lon1, lat2, lon2):
    """Return the distance in km between two points around the Earth.

    Latitude and longitude for each point are given in degrees.
    """
    if validation(lat1,lon1) and validation(lat2,lon2):
        distance=2*6371*np.arcsin(math.sqrt(math.sin((lat2-lat1)/2)**2+math.cos(lat1)*math.cos(lat2)*math.sin((lon2-lon1)/2)**2))
    return distance
