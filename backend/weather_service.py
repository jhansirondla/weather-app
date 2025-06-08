import requests

API_KEY = '698e6a22689ec546f18ebeab1d64c318'  # Your real API key

def get_weather_data(location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "location": data["name"],
            "temp": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }
    return None



