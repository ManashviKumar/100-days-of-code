# My api of openweathermap website
# api_key="496906d2d4ff46f74c70bde21d92d226"

# 1. Method
#import request of weather from the website
# import requests
# LAT=25.467
# LON=91.366
# response=requests.get(url=f"https://api.openweathermap.org/data/2.5/forecast?lat={LAT}&lon={LON}&appid=496906d2d4ff46f74c70bde21d92d226")
# response.raise_for_status() #raise exception if there is any problem with url
# print(response.json())

# 2. Method
import requests
Endpoint="https://api.openweathermap.org/data/2.5/forecast"
api_key="496906d2d4ff46f74c70bde21d92d226"
weather_params={
    "lat":25.467,
    "lon":91.366,
    "appid":api_key,
    "cnt":4,
}

response = requests.get(Endpoint,params=weather_params)
response.raise_for_status()
weather_data=response.json()

will_rain=False
for hour_data in weather_data["list"]:
    condition_code=hour_data["weather"][0]["id"]
    if int(condition_code) < 700 :
        will_rain=True
if will_rain:
    print("Bring Umbrella")