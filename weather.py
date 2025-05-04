import requests
import json
from datetime import datetime

# Configuration
API_KEY = "fd207963a19ccec3eb0806dca03061b7"  # Replace with your OpenWeatherMap API key
BASE_URL = "https://api.openweathermap.org/data/2.5/"

def get_current_weather(city):
    """Fetch current weather data for a given city."""
    url = f"{BASE_URL}weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Error: Unable to fetch weather data (Status code: {response.status_code})")
            return None
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None

def get_forecast(city):
    """Fetch 5-day weather forecast for a given city."""
    url = f"{BASE_URL}forecast?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Error: Unable to fetch forecast data (Status code: {response.status_code})")
            return None
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None

def display_current_weather(data):
    """Display current weather information."""
    if not data:
        return
    city = data['name']
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    description = data['weather'][0]['description']
    wind_speed = data['wind']['speed']

    print(f"\nCurrent Weather in {city}:")
    print(f"Temperature: {temp}°C")
    print(f"Feels Like: {feels_like}°C")
    print(f"Humidity: {humidity}%")
    print(f"Pressure: {pressure} hPa")
    print(f"Weather: {description.capitalize()}")
    print(f"Wind Speed: {wind_speed} m/s")

def display_forecast(data):
    """Display 5-day weather forecast."""
    if not data:
        return
    city = data['city']['name']
    print(f"\n5-Day Weather Forecast for {city}:")
    for item in data['list']:
        # Extract date and time
        dt = datetime.fromtimestamp(item['dt'])
        if dt.hour == 12:  # Display only noon forecasts for simplicity
            temp = item['main']['temp']
            description = item['weather'][0]['description']
            print(f"{dt.strftime('%Y-%m-%d %H:%M')}: {temp}°C, {description.capitalize()}")

def main():
    """Main function to run the weather app."""
    while True:
        print("\nWeather Forecast App")
        print("1. Get Current Weather")
        print("2. Get 5-Day Forecast")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '3':
            print("Goodbye!")
            break

        if choice in ['1', '2']:
            city = input("Enter city name: ").strip()
            if not city:
                print("Error: City name cannot be empty.")
                continue

            if choice == '1':
                weather_data = get_current_weather(city)
                display_current_weather(weather_data)
            elif choice == '2':
                forecast_data = get_forecast(city)
                display_forecast(forecast_data)
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()