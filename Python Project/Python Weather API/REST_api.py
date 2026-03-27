import os
from dotenv import load_dotenv
import requests
from datetime import datetime

load_dotenv()

# Hiding API key using dotenv
api_key = os.environ['WEATHER_KEY']
print(f"API Key: {api_key[:3]}...")

# city fetch from user input
city = input("Enter your city name: ")

url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
# NOTE: all are based on standard units by default

response = requests.get(url)
data = response.json()

if response.status_code != 200:
    print("Something went wrong :(")
    exit()

# printing parameters:
print('='*42)
print('*'*12 + '   ' + 'Weather Info' + '   ' + '*'*12)
print('='*42)
print(f"{'City':<20} |  {data['name']}")
print(f"{'Temperature (\u00b0C)':<20} |  {round(data['main']['temp']-273.15, 2)}")
print(f"{'Feel Like (\u00b0C)':<20} |  {round(data['main']['feels_like']-273.15, 2)}")
print(f"{'Min.Temperature (\u00b0C)':<20} |  {round(data['main']['temp_min']-273.15, 2)}")
print(f"{'Max.Temperature (\u00b0C)':<20} |  {round(data['main']['temp_max']-273.15, 2)}")
print(f"{'Condition':<20} |  {data['weather'][0]['description'].title()}")
print(f"{'Humidity (%)':<20} |  {data['main']['humidity']}%")
print(f"{'Atm. Pressure (hPa)':<20} |  {data['main']['pressure']}")
print(f"{'Wind Speed (m/s)':<20} |  {data['wind']['speed']}m/s")
print(f"{'Wind Degree':<20} |  {data['wind']['deg']}\u00b0")
print(f"{'Sunrise Time':<20} |  {datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M')}")
print(f"{'Sunset Time':<20} |  {datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M')}")
print('='*42)