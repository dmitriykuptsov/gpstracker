import requests
import urllib.parse
import json
import random

def auth(base_url, username, password):
	return None

def get_equipment(base_url, activelist):
	param = urllib.parse.quote(activelist)
	url = base_url + "/v1/system/referencedata/activelists/" + param
	response = requests.get(url)
	response = json.loads(response.content.decode("utf-8"))
	return response["activeList"]

def get_coordinates(base_url, function, simulate = False, min_x = 64.540093, max_x = 64.608378, max_y = 41.499359, min_y = 41.447125, equipment = []):
	if not simulate:
		url = base_url + "/v1/equipment/positions?functions=" + function + "&max-positions=1"
		response = requests.get(url)
		response = json.loads(response.content.decode("utf-8"))
		return response["results"]
	else:
		results = []
		for e in equipment:
			x = random.uniform(min_x, max_x)
			y = random.uniform(min_y, max_y)
			results.append({
				"code": e["code"],
				"description": e["description"],
				"positions": [
					{
						"x": x,
						"y": y,
						"z": 0,
					}
					]
				}
			)
		#print(results)
		return results;

