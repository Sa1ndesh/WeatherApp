"""
Configuration settings for the Weather App
"""

# OpenWeatherMap API Configuration
API_KEY = "your_api_key_here"  # Replace with your actual API key from openweathermap.org
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Default settings
DEFAULT_UNITS = "metric"  # metric (Celsius), imperial (Fahrenheit), kelvin
DEFAULT_LANGUAGE = "en"   # Language for weather descriptions

# GUI Settings
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 500
WINDOW_TITLE = "Weather App"

# Colors for GUI
COLORS = {
    "primary": "#2196F3",
    "secondary": "#FFC107", 
    "success": "#4CAF50",
    "error": "#F44336",
    "background": "#F5F5F5",
    "text": "#333333"
}

# Weather condition mappings for icons
WEATHER_ICONS = {
    "clear sky": "☀️",
    "few clouds": "🌤️",
    "scattered clouds": "⛅",
    "broken clouds": "☁️",
    "shower rain": "🌦️",
    "rain": "🌧️",
    "thunderstorm": "⛈️",
    "snow": "❄️",
    "mist": "🌫️",
    "fog": "🌫️",
    "haze": "🌫️"
}
