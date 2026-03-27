dict1 = {'coord': {'lon': 77.4, 'lat': 23.2667},
         'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}],
         'base': 'stations',
         'main': {'temp': 304.28, 'feels_like': 302.27, 'temp_min': 304.28, 'temp_max': 304.28, 'pressure': 1013, 'humidity': 18, 'sea_level': 1013, 'grnd_level': 956},
         'visibility': 6000,
         'wind': {'speed': 3.09, 'deg': 200},
         'clouds': {'all': 20},
         'dt': 1774247195,
         'sys': {'type': 1, 'id': 9063, 'country': 'IN', 'sunrise': 1774227112, 'sunset': 1774270934},
         'timezone': 19800,
         'id': 1275841,
         'name': 'Bhopal',
         'cod': 200
         }
print(f"Weather in {dict1['name']} is {dict1['weather']['description']}.....")

# sample templete...
print('='*42)
print('*'*12 + '   ' + 'Weather Info' + '   ' + '*'*12)
print('='*42)
print(f"{'City':<20}||{dict1['name']:>20}")
print(f"{'Condition':<20}||{dict1['weather'][0]['description'].title():>20}")
print(f"{'sample1':<20}||{'sample2':>20}")
