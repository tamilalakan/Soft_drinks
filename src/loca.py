from geopy.geocoders import Nominatim
import requests

geolocator = Nominatim(user_agent='MyGeocoder')
location = geolocator.geocode("11.6431946, 78.1508203").raw
print(location)
