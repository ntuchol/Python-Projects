import requests

api_key = "YOUR_API_KEY"
city = "London"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

response = requests.get(url)
weather_data = response.json()

print(f"Current temperature in {city}: {weather_data['main']['temp']} K")
from pyowm import OWM

owm = OWM('YOUR_API_KEY')
mgr = owm.weather_manager()

observation = mgr.weather_at_place('New York, US')
weather = observation.weather

print(f"Temperature in New York: {weather.temperature('celsius')['temp']}°C")
