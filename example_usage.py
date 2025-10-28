"""
Example usage of the Weather API module
This file demonstrates how to use the WeatherAPI class programmatically
"""

from weather_api import WeatherAPI


def example_basic_usage():
    """Basic example of fetching weather data"""
    print("=== Basic Weather API Usage ===")
    
    # Initialize the API
    weather_api = WeatherAPI()
    
    # Fetch weather for a city
    city = "London"
    success, data = weather_api.get_weather_data(city)
    
    if success:
        print(f"Weather in {data['city']}:")
        print(f"Temperature: {data['temperature']}°C")
        print(f"Description: {data['description']}")
        print(f"Humidity: {data['humidity']}%")
        print(f"Wind Speed: {data['wind_speed']} m/s")
    else:
        print(f"Error: {data['error']}")


def example_unit_conversion():
    """Example of temperature unit conversion"""
    print("\n=== Temperature Unit Conversion ===")
    
    weather_api = WeatherAPI()
    
    # Get weather in Celsius (metric)
    success, data = weather_api.get_weather_data("Tokyo", units="metric")
    
    if success:
        temp_c = data['temperature']
        temp_f = WeatherAPI.celsius_to_fahrenheit(temp_c)
        
        print(f"Temperature in Tokyo:")
        print(f"Celsius: {temp_c}°C")
        print(f"Fahrenheit: {temp_f}°F")
        
        # Verify conversion
        temp_c_back = WeatherAPI.fahrenheit_to_celsius(temp_f)
        print(f"Converted back: {temp_c_back}°C")


def example_multiple_cities():
    """Example of fetching weather for multiple cities"""
    print("\n=== Multiple Cities Weather ===")
    
    weather_api = WeatherAPI()
    cities = ["New York", "Paris", "Sydney", "Mumbai"]
    
    for city in cities:
        success, data = weather_api.get_weather_data(city)
        
        if success:
            icon = WeatherAPI.get_weather_icon(data['description'])
            print(f"{icon} {data['city']}: {data['temperature']}°C, {data['description']}")
        else:
            print(f"❌ {city}: {data['error']}")


def example_detailed_weather():
    """Example showing all available weather data"""
    print("\n=== Detailed Weather Information ===")
    
    weather_api = WeatherAPI()
    success, data = weather_api.get_weather_data("Berlin")
    
    if success:
        print(f"Detailed weather for {data['city']}, {data['country']}:")
        print("-" * 40)
        
        # Temperature info
        print(f"🌡️  Temperature: {data['temperature']}°C")
        print(f"🤔 Feels like: {data['feels_like']}°C")
        
        # Weather conditions
        icon = WeatherAPI.get_weather_icon(data['description'])
        print(f"{icon} Condition: {data['description']}")
        print(f"📊 Main: {data['main_condition']}")
        
        # Atmospheric conditions
        print(f"💧 Humidity: {data['humidity']}%")
        print(f"📊 Pressure: {data['pressure']} hPa")
        print(f"👁️  Visibility: {data['visibility']} km")
        print(f"☁️  Cloudiness: {data['cloudiness']}%")
        
        # Wind information
        print(f"🌬️  Wind Speed: {data['wind_speed']} m/s")
        print(f"🧭 Wind Direction: {data['wind_direction']}°")
        
        # Sun times (timestamps)
        if data['sunrise'] and data['sunset']:
            from datetime import datetime
            sunrise = datetime.fromtimestamp(data['sunrise']).strftime('%H:%M')
            sunset = datetime.fromtimestamp(data['sunset']).strftime('%H:%M')
            print(f"🌅 Sunrise: {sunrise}")
            print(f"🌇 Sunset: {sunset}")


def example_error_handling():
    """Example of proper error handling"""
    print("\n=== Error Handling Examples ===")
    
    weather_api = WeatherAPI()
    
    # Test with invalid city
    success, data = weather_api.get_weather_data("InvalidCityName123")
    if not success:
        print(f"Expected error for invalid city: {data['error']}")
    
    # Test with empty city name
    success, data = weather_api.get_weather_data("")
    if not success:
        print(f"Expected error for empty city: {data['error']}")
    
    # Test with API key issue (if API key is not set)
    weather_api_no_key = WeatherAPI(api_key="invalid_key")
    success, data = weather_api_no_key.get_weather_data("London")
    if not success:
        print(f"Expected error for invalid API key: {data['error']}")


if __name__ == "__main__":
    """Run all examples"""
    try:
        example_basic_usage()
        example_unit_conversion()
        example_multiple_cities()
        example_detailed_weather()
        example_error_handling()
        
        print("\n✅ All examples completed successfully!")
        
    except Exception as e:
        print(f"\n❌ Error running examples: {e}")
        print("Make sure you have:")
        print("1. Set your API key in config.py")
        print("2. Installed the requests library")
        print("3. Internet connection")
