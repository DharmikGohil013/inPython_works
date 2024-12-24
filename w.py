import requests

# Your API key (replace with your actual API key)
API_KEY = "2a5d1a5de8534cd28e670614240310"

# Base URL for OpenWeatherMap API
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


# Function to fetch weather data
def get_weather(city):
    # Construct the request URL
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"  # units=metric for Celsius

    # Send a GET request to the API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()

        # Extract relevant data
        city_name = data["name"]
        temperature = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        # Print the weather details
        print(f"Weather in {city_name}:")
        print(f"Temperature: {temperature}°C")
        print(f"Condition: {weather}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("City not found or API request failed.")


# Ask the user for a city name
city_name = input("Enter the city name: ")
get_weather(city_name)  # Proper function call
