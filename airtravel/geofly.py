from geograpy.labels import Labels
import pandas as pd
import numpy as np
import regex as re
#import re

from geopy.extra.rate_limiter import RateLimiter
from geopy.geocoders import Nominatim
from geopy import distance


# Insert faculty, associate, postdoc etc. under filename
file = open('filename', 'r')
lines = file.readlines()

string = ','.join(lines)

geolocator = Nominatim(user_agent="PI")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=5)

toronto = geocode("Pearson Toronto")
coord_toronto = (toronto.latitude, toronto.longitude)

print("The coordinates of Toronto airport are: " + coord_toronto)

def process(s):
    s = re.sub("[\n0-9>/]", "", s)
    s = re.sub("[-]", "", s)
    #print(s)
    g = geocode(s)
    try:
        coord_g = (g.latitude, g.longitude)
        return distance.great_circle(coord_toronto, coord_g)
    except:
        return 0

distances = [process(l) for l in lines]

total_distance = np.sum(distances)
print("The total distance travelled is: " + total_distance)





