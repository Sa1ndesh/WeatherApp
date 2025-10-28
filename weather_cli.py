"""
Beginner Weather App - Command Line Interface
A simple command-line weather application that fetches and displays current weather data.
"""

import sys
from weather_api import WeatherAPI


def display_weather(weather_data):
    """Display weather information in a formatted way"""
    print("\n" + "="*50)
    print(f"🌤️  WEATHER IN {weather_data['city'].upper()}")
    if weather_data['country']:
        print(f"📍 Country: {weather_data['country']}")
    print("="*50)
    
    # Temperature information
    print(f"🌡️  Temperature: {weather_data['temperature']}°C")
    print(f"🤔 Feels like: {weather_data['feels_like']}°C")
    
    # Weather conditions
    icon = WeatherAPI.get_weather_icon(weather_data['description'])
    print(f"{icon} Condition: {weather_data['description']}")
    
    # Additional information
    print(f"💧 Humidity: {weather_data['humidity']}%")
    print(f"🌬️  Wind Speed: {weather_data['wind_speed']} m/s")
    print(f"☁️  Cloudiness: {weather_data['cloudiness']}%")
    
    if weather_data['pressure']:
        print(f"📊 Pressure: {weather_data['pressure']} hPa")
    
    if weather_data['visibility']:
        print(f"👁️  Visibility: {weather_data['visibility']} km")
    
    print("="*50)


def get_user_input():
    """Get city name from user with input validation"""
    while True:
        city = input("\n🏙️  Enter city name (or 'quit' to exit): ").strip()
        
        if city.lower() in ['quit', 'exit', 'q']:
            print("👋 Thank you for using Weather App!")
            return None
        
        if city:
            return city
        else:
            print("❌ Please enter a valid city name.")


def show_welcome():
    """Display welcome message"""
    print("\n" + "="*60)
    print("🌤️  WELCOME TO THE WEATHER APP")
    print("="*60)
    print("Get real-time weather information for any city!")
    print("Type 'quit' anytime to exit the application.")
    print("="*60)


def main():
    """Main application loop"""
    # Initialize weather API
    weather_api = WeatherAPI()
    
    # Show welcome message
    show_welcome()
    
    # Main application loop
    while True:
        # Get city name from user
        city = get_user_input()
        if city is None:  # User wants to quit
            break
        
        print(f"\n🔍 Fetching weather data for {city}...")
        
        # Fetch weather data
        success, data = weather_api.get_weather_data(city)
        
        if success:
            display_weather(data)
            
            # Ask if user wants to convert temperature
            while True:
                convert = input("\n🔄 Convert to Fahrenheit? (y/n): ").strip().lower()
                if convert in ['y', 'yes']:
                    temp_f = WeatherAPI.celsius_to_fahrenheit(data['temperature'])
                    feels_f = WeatherAPI.celsius_to_fahrenheit(data['feels_like'])
                    print(f"🌡️  Temperature: {temp_f}°F")
                    print(f"🤔 Feels like: {feels_f}°F")
                    break
                elif convert in ['n', 'no', '']:
                    break
                else:
                    print("Please enter 'y' for yes or 'n' for no.")
        else:
            print(f"\n❌ Error: {data['error']}")
            
            # Provide helpful suggestions
            if "not found" in data['error'].lower():
                print("💡 Suggestions:")
                print("   • Check the spelling of the city name")
                print("   • Try using the full city name")
                print("   • Include country name (e.g., 'London, UK')")
            elif "api key" in data['error'].lower():
                print("💡 To fix this:")
                print("   • Sign up at https://openweathermap.org/api")
                print("   • Get your free API key")
                print("   • Update the API_KEY in config.py")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Application interrupted. Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        print("Please check your internet connection and try again.")
        sys.exit(1)
