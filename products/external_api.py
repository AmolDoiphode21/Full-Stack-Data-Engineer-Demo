# products/external_api.py
import requests

def fetch_weather(city="London"):
    """
    Fetch current weather for a city from wttr.in (free, no API key required)
    """
    # Make sure to replace spaces with '+' or '%20'
    city = city.replace(" ", "+")
    url = f"https://wttr.in/{city}?format=j1"  # JSON format
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        # wttr.in JSON structure: data['current_condition'][0]
        current = data.get("current_condition", [{}])[0]
        
        weather_info = {
            "city": city,
            "temperature_C": current.get("temp_C"),
            "temperature_F": current.get("temp_F"),
            "humidity": current.get("humidity"),
            "description": current.get("weatherDesc", [{}])[0].get("value")
        }
        
        return weather_info
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
