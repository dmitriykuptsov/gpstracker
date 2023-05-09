import requests
from sys import argv
import math

output="muruntau.png"
token=argv[1]
w = 1280
h = 1280

URL = "https://api.mapbox.com/styles/v1/mapbox/streets-v12/static/[64.501910,41.448598,64.636402,41.513259]/1280x1280?access_token=$token"

print("Requesting static map")
print(URL)
r=requests.get(URL)
fd = open(output, "wb")
fd.write(r.content)
fd.close()
