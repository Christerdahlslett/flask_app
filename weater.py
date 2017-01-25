from geopy.geocoders import Nominatim
import forecastio
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


def get_location(adress):
	api_key = os.environ["FORECASTIO_API_KEY"]
	geolocator = Nominatim()
	location = geolocator.geocode(adress)
	latitude = location.latitude 
	longitude = location.longitude
	forecast = forecastio.load_forecast(api_key, latitude, longitude).currently()
	summary = forecast.summary 
	temperature = forecast.temperature
	return "Your location is: {} and the weather is {} and the temperature is {}".format(adress, summary, temperature)


