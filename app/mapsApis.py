import googlemaps
from pprint import pprint


API_KEY = 'AIzaSyD37xmgajiD-RrnJAG151511f6OAprUsl8'

map_client = googlemaps.Client(API_KEY)


work_place_address = '1 Market st, San Francisco, CA'
response = map_client.geocode(work_place_address)
pprint(response)