import requests

API_KEY = '096122609932057e7534c8ba725747d4'
BASE_API = 'https://pro.openweathermap.org/data/2.5/forecast/hourly'


def fetch_weather_data(city_name):
    api_url = f'{BASE_API}?q={city_name}&appid={API_KEY}&units=metric'
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code}")
        return None
