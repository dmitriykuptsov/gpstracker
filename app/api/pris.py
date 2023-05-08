import requests
import urllib.parse
import json

def auth(base_url, username, password):
	return None

def get_equipment(base_url, activelist):
	param = urllib.parse.quote(activelist)
	url = base_url + "/v1/system/referencedata/activelists/" + param
	response = requests.get(url)
	response = json.loads(response.content.decode("utf-8"))
	return response["activeList"]

def get_coordinates(base_url, function):
	url = base_url + "/v1/equipment/positions?functions=" + function
	response = requests.get(url)
	response = json.loads(response.content.decode("utf-8"))
	return response
