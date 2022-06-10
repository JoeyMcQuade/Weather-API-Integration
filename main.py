import requests
from decouple import config

def make_requests(city_name):
    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={config('SECRET_API_KEY')}"
    response = requests.get(api_url)
    print(response.json())
    return response.json()

def format_response(data):
    celsius = convert_kelvin_to_celsius(data['main']['temp'])
    weather = data["weather"][0]["description"]
    return f"Welcome to {data['name']} \nThe temperature is {celsius}\N{DEGREE SIGN} \nThe sky is {weather}"

def convert_kelvin_to_celsius(value_in_kelvin):
    return str(value_in_kelvin - 273.15)[:5]

if __name__ == "__main__":
    print(format_response(make_requests("Dubai")))

