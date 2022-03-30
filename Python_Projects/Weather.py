from wsgiref.util import request_uri
import requests

API_KEY = "6cfd4e5bd4a1f2a9bcc0d5bbe96e82d1"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"

response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data["weather"][0]["description"]
    temperature = round(data["main"]["temp"] - 273.15, 2)

    print(f"The Weather currently in {city.capitalize()} is: {weather}")
    print(f"The Temperature in {city.capitalize()} is: {temperature} Celsius.")

else:
    print("An error occurred.")