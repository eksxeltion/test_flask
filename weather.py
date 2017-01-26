import os
import forecastio
from geopy.geocoders import Nominatim
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

def get_weather(place):
	geolocator = Nominatim()
	location = geolocator.geocode(place)
	forecast = forecastio.load_forecast(os.environ['FORECAST_API_KEY'], location.latitude, location.longitude).currently()
	summary = forecast.summary
	temperature = forecast.temperature
	precipitation = forecast.precipProbability
	return "{} at {}F, {}% probability of precipitation ".format(summary, temperature, precipitation)

