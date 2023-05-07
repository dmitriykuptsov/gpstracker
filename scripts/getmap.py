import requests
from sys import argv
import math

output="muruntau.png"
token=argv[1]
w = 1280
h = 1280
zoom = 13
lat = 64.576502
lng = 41.483513

dim=str(w) + "x" + str(h)

def getPointLatLng(x, y):
    parallelMultiplier = math.cos(lat * math.pi / 180)
    degreesPerPixelX = 360 / math.pow(2, zoom + 8)
    degreesPerPixelY = 360 / math.pow(2, zoom + 8) * parallelMultiplier
    pointLat = lat - degreesPerPixelY * ( y - h / 2)
    pointLng = lng + degreesPerPixelX * ( x  - w / 2)

    return (pointLat, pointLng)

print("Getting bounding box coordinates: ")
#print('NE: ', getPointLatLng(w, 0))
#print('SW: ', getPointLatLng(0, h))
print('NW: ', getPointLatLng(0, 0))
print('SE: ', getPointLatLng(w, h))


URL = "https://api.mapbox.com/styles/v1/mapbox/satellite-v9/static/$lat,$lng,$zoom/$dim?access_token=$token"
URL = URL.replace("$lat", str(lat))
URL = URL.replace("$lng", str(lng))
URL = URL.replace("$zoom", str(zoom))
URL = URL.replace("$dim", str(dim))
URL = URL.replace("$token", str(token))

print("Requesting static map")
print(URL)
r=requests.get(URL)
fd = open(output, "wb")
fd.write(r.content)
fd.close()
