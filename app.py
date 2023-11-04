import requests
import json
import time

# Define the base URL for the OpenWeatherMap API
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Global variables
API_KEY = '1492dce316b9b92a1b89b41fae9ad98b'
favorite_cities = []

# Function to get weather information by city name
def get_weather(city, units='metric'):
    params = {
        'q': city,
        'units': units,
        'appid': API_KEY
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if data['cod'] == 200:
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        print(f"Weather in {city}: {description.capitalize()}")
        print(f"Temperature: {temperature}°{units}")
    else:
        print("City not found or an error occurred.")

# Function to display the favorite cities list
def show_favorite_cities():
    print("Favorite Cities:")
    for city in favorite_cities:
        print(city)

# Function to add a city to the favorite list
def add_to_favorite(city):
    if city not in favorite_cities:
        favorite_cities.append(city)
        save_favorite_cities()

# Function to remove a city from the favorite list
def remove_from_favorite(city):
    if city in favorite_cities:
        favorite_cities.remove(city)
        save_favorite_cities()

# Function to save the favorite cities list to a file
def save_favorite_cities():
    with open('favorite_cities.json', 'w') as file:
        json.dump(favorite_cities, file)

# Function to load the favorite cities list from a file
def load_favorite_cities():
    try:
        with open('favorite_cities.json', 'r') as file:
            data = json.load(file)
            if isinstance(data, list):
                favorite_cities.extend(data)
    except FileNotFoundError:
        pass

# Main application loop with auto-refresh
if __name__ == '__main__':
    load_favorite_cities()

    while True:
        print("\n1. Check Weather")
        print("2. Show Favorite Cities")
        print("3. Add Favorite City")
        print("4. Remove Favorite City")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            city = input("Enter city name: ")
            get_weather(city)
        elif choice == '2':
            show_favorite_cities()
        elif choice == '3':
            city = input("Enter city name to add to favorites: ")
            add_to_favorite(city)
        elif choice == '4':
            city = input("Enter city name to remove from favorites: ")
            remove_from_favorite(city)
        elif choice == '5':
            save_favorite_cities()
            break

        # Auto-refresh every 15-30 seconds
        time.sleep(15 + 15 * (int(time.time()) % 2))
