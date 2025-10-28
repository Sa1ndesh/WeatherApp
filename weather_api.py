"""
Shared weather API functionality for both CLI and GUI versions
"""

import requests
import json
from typing import Dict, Optional, Tuple
from config import API_KEY, BASE_URL, DEFAULT_UNITS


class WeatherAPI:
    """Handles all weather API interactions"""
    
    def __init__(self, api_key: str = API_KEY):
        self.api_key = api_key
        self.base_url = BASE_URL
    
    def get_weather_data(self, city: str, units: str = DEFAULT_UNITS) -> Tuple[bool, Dict]:
        """
        Fetch weather data for a given city
        
        Args:
            city (str): City name to get weather for
            units (str): Temperature units (metric, imperial, kelvin)
            
        Returns:
            Tuple[bool, Dict]: (success, data) where data contains weather info or error message
        """
        if not self.api_key or self.api_key == "your_api_key_here":
            return False, {"error": "Please set your API key in config.py"}
        
        if not city.strip():
            return False, {"error": "Please enter a valid city name"}
        
        try:
            # Construct API URL
            url = f"{self.base_url}?q={city.strip()}&appid={self.api_key}&units={units}"
            
            # Make API request
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                return True, self._parse_weather_data(data)
            elif response.status_code == 404:
                return False, {"error": f"City '{city}' not found. Please check the spelling."}
            elif response.status_code == 401:
                return False, {"error": "Invalid API key. Please check your configuration."}
            else:
                return False, {"error": f"API error: {response.status_code}"}
                
        except requests.exceptions.Timeout:
            return False, {"error": "Request timed out. Please check your internet connection."}
        except requests.exceptions.ConnectionError:
            return False, {"error": "Connection error. Please check your internet connection."}
        except requests.exceptions.RequestException as e:
            return False, {"error": f"Network error: {str(e)}"}
        except json.JSONDecodeError:
            return False, {"error": "Invalid response from weather service."}
        except Exception as e:
            return False, {"error": f"Unexpected error: {str(e)}"}
    
    def _parse_weather_data(self, data: Dict) -> Dict:
        """
        Parse and structure weather data from API response
        
        Args:
            data (Dict): Raw API response data
            
        Returns:
            Dict: Structured weather information
        """
        try:
            return {
                "city": data.get("name", "Unknown"),
                "country": data.get("sys", {}).get("country", ""),
                "temperature": round(data.get("main", {}).get("temp", 0), 1),
                "feels_like": round(data.get("main", {}).get("feels_like", 0), 1),
                "humidity": data.get("main", {}).get("humidity", 0),
                "pressure": data.get("main", {}).get("pressure", 0),
                "description": data.get("weather", [{}])[0].get("description", "").title(),
                "main_condition": data.get("weather", [{}])[0].get("main", ""),
                "wind_speed": data.get("wind", {}).get("speed", 0),
                "wind_direction": data.get("wind", {}).get("deg", 0),
                "visibility": data.get("visibility", 0) / 1000 if data.get("visibility") else 0,  # Convert to km
                "cloudiness": data.get("clouds", {}).get("all", 0),
                "sunrise": data.get("sys", {}).get("sunrise", 0),
                "sunset": data.get("sys", {}).get("sunset", 0),
            }
        except Exception as e:
            return {"error": f"Error parsing weather data: {str(e)}"}
    
    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        """Convert Celsius to Fahrenheit"""
        return round((celsius * 9/5) + 32, 1)
    
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit: float) -> float:
        """Convert Fahrenheit to Celsius"""
        return round((fahrenheit - 32) * 5/9, 1)
    
    @staticmethod
    def get_weather_icon(description: str) -> str:
        """Get weather icon emoji based on description"""
        from config import WEATHER_ICONS
        
        description_lower = description.lower()
        for condition, icon in WEATHER_ICONS.items():
            if condition in description_lower:
                return icon
        
        # Default icons based on keywords
        if any(word in description_lower for word in ["sun", "clear"]):
            return "☀️"
        elif any(word in description_lower for word in ["cloud", "overcast"]):
            return "☁️"
        elif any(word in description_lower for word in ["rain", "drizzle"]):
            return "🌧️"
        elif "snow" in description_lower:
            return "❄️"
        elif any(word in description_lower for word in ["storm", "thunder"]):
            return "⛈️"
        else:
            return "🌤️"  # Default icon
