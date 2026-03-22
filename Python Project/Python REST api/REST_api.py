import os
import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

api_key = os.environ.get("WEATHER_KEY")
print(f"API Key: {api_key[:5]}...")

city = input("Enter City name: ")
api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
response = requests.get(api_url)
data = response.json()

if response.status_code != 200:
    print('Oops, something went wrong. try again later.')
    exit()

# Prepare data
weather_data = [
    ("City", f"{data['name']}, {data['sys']['country']}"),
    ("Temperature (°C)", data["main"]["temp"]),
    ("Feels Like (°C)", data["main"]["feels_like"]),
    ("Condition", data["weather"][0]["description"].title()),
    ("Humidity (%)", data["main"]["humidity"]),
    ("Wind Speed (m/s)", data["wind"]["speed"]),
    ("Sunrise", datetime.fromtimestamp(data["sys"]["sunrise"]).strftime('%H:%M:%S')),
    ("Sunset", datetime.fromtimestamp(data["sys"]["sunset"]).strftime('%H:%M:%S'))
]

# Print table manually
print("\n" + "=" * 45)
print(f"{'Parameter':<22} | {'Value':<20}")
print("=" * 45)

for key, value in weather_data:
    print(f"{key:<22} | {str(value):<20}")

print("=" * 45)