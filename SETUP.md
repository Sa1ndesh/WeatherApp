# 🚀 Setup Guide for Weather App

This guide will help you set up and run the Weather App on your system.

## 📋 Prerequisites

- Python 3.7 or higher
- Internet connection
- OpenWeatherMap API key (free)

## 🔧 Installation Steps

### 1. Get Your API Key

1. Visit [OpenWeatherMap](https://openweathermap.org/api)
2. Sign up for a free account
3. Navigate to the API keys section
4. Copy your API key

### 2. Configure the Application

1. Open `config.py` in a text editor
2. Replace `"your_api_key_here"` with your actual API key:
   ```python
   API_KEY = "your_actual_api_key_here"
   ```
3. Save the file

### 3. Install Dependencies

Open a terminal/command prompt in the project directory and run:

```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install requests
```

## 🎮 Running the Applications

### Command Line Version (Beginner)
```bash
python weather_cli.py
```

### GUI Version (Advanced)
```bash
python weather_gui.py
```

## 🔍 Troubleshooting

### Common Issues

**"Invalid API key" error:**
- Make sure you've replaced the API key in `config.py`
- Verify your API key is active (may take a few minutes after signup)

**"City not found" error:**
- Check spelling of city name
- Try including country code (e.g., "London, UK")
- Use full city names instead of abbreviations

**Connection errors:**
- Check your internet connection
- Verify firewall isn't blocking the application
- Try a different city name to test

**Import errors:**
- Make sure you've installed the requirements: `pip install -r requirements.txt`
- Check that you're using Python 3.7+

### Getting Help

If you encounter issues:
1. Check the error message carefully
2. Verify your API key is correct
3. Test your internet connection
4. Try running with a simple city name like "London"

## 🌟 Features Overview

### CLI Version Features:
- Simple text-based interface
- Current weather information
- Temperature unit conversion
- Error handling with helpful messages

### GUI Version Features:
- Modern graphical interface
- Real-time weather updates
- Detailed weather information
- Temperature unit toggle (°C/°F)
- Weather icons and visual indicators
- Scrollable interface
- Status updates

## 📝 Example Usage

### CLI Example:
```
🏙️  Enter city name (or 'quit' to exit): New York

🔍 Fetching weather data for New York...

==================================================
🌤️  WEATHER IN NEW YORK
📍 Country: US
==================================================
🌡️  Temperature: 22.5°C
🤔 Feels like: 24.1°C
☀️ Condition: Clear Sky
💧 Humidity: 65%
🌬️  Wind Speed: 3.2 m/s
☁️  Cloudiness: 10%
📊 Pressure: 1013 hPa
👁️  Visibility: 10.0 km
==================================================
```

### GUI Features:
- Enter city name in the search box
- Click "Search" or press Enter
- Toggle between °C and °F using the unit buttons
- View detailed weather information in an organized layout
- Get real-time status updates in the status bar

Enjoy using your Weather App! 🌤️
