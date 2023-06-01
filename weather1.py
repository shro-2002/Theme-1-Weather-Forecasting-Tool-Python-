import argparse
import requests
import json

def get_weather(city):
    # OpenWeatherMap API key
    api_key = "88427bee900c081616817726018568b3"

    # API endpoint for current weather data
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        # Send GET request to the API endpoint
        response = requests.get(url)
        response.raise_for_status()

        # Parse the JSON response
        data = json.loads(response.text)

        # Extract relevant weather information
        weather_data = {
            "name": data["name"],
            "country": data["sys"]["country"],
            "temp": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "main": data["weather"][0]["main"],
            "description": data["weather"][0]["description"].title(),
            "pressure": data["main"]["pressure"],
            "humidity": data["main"]["humidity"],
            "speed": data["wind"]["speed"],
            "deg": data["wind"]["deg"],
            "timezone": data["timezone"]
        }

        # Print the weather forecast
        print(f"Weather forecast for {weather_data['name']}, {weather_data['country']}:")
        print(f"Temperature: {weather_data['temp']}°C")
        print(f"Feels Like: {weather_data['feels_like']}°C")
        print(f"Main: {weather_data['main']}")
        print(f"Description: {weather_data['description']}")
        print(f"Pressure: {weather_data['pressure']} hPa")
        print(f"Humidity: {weather_data['humidity']}%")
        print(f"Wind Speed: {weather_data['speed']} m/s")
        print(f"Wind Direction: {weather_data['deg']}°")
        print(f"Timezone: {weather_data['timezone']}")

    except requests.exceptions.HTTPError as err:
        print(f"HTTP Error: {err}")
    except json.JSONDecodeError as err:
        print(f"JSON Decode Error: {err}")
    except KeyError as err:
        print(f"Key Error: {err}")
    except Exception as err:
        print(f"Error: {err}")

def main():
    # Create an argument parser
    parser = argparse.ArgumentParser(description="Get the current weather forecast for a city")

    # Add an argument for the city name
    parser.add_argument("city", type=str, help="Name of the city")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the function to get the weather forecast
    get_weather(args.city)

if __name__ == "__main__":
    main()
