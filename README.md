# 🌤️ Weather App Project

A comprehensive Python weather application that fetches and displays real-time weather data using the OpenWeatherMap API. This project includes both beginner-friendly command-line and advanced GUI versions.

## 🎯 Project Overview

This project demonstrates:
- API integration with OpenWeatherMap
- JSON data parsing and handling
- User input validation and error handling
- GUI development with Tkinter
- Unit conversion (Celsius ↔ Fahrenheit)
- Modern Python programming practices

## 📁 Project Structure

```
Weather app/
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
├── config.py                # Configuration settings
├── weather_cli.py           # Beginner: Command-line version
├── weather_gui.py           # Advanced: GUI version
├── weather_api.py           # Shared API functionality
└── assets/                  # Weather icons and images
    └── icons/
```

## 🚀 Quick Start

### 1. Get Your API Key
1. Sign up at [OpenWeatherMap](https://openweathermap.org/api)
2. Get your free API key
3. Update `config.py` with your API key

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Apps

**Beginner Version (Command Line):**
```bash
python weather_cli.py
```

**Advanced Version (GUI):**
```bash
python weather_gui.py
```

## 🧑‍💻 Beginner Version Features

- Simple command-line interface
- City name input
- Current weather display:
  - Temperature
  - Humidity
  - Weather conditions
- Basic error handling

## 🧠 Advanced Version Features

- Modern GUI with Tkinter
- Real-time weather updates
- Detailed weather information:
  - Current temperature, humidity, wind speed
  - Weather description and conditions
- Unit conversion (°C ↔ °F)
- Weather icons
- Error handling with user-friendly messages
- Input validation

## 🔧 Configuration

Edit `config.py` to set your OpenWeatherMap API key:

```python
API_KEY = "your_api_key_here"
```

## 📚 Learning Outcomes

By working with this project, you'll learn:
- ✅ API integration and JSON parsing
- ✅ GUI development with Tkinter
- ✅ Error handling and data validation
- ✅ Object-oriented programming
- ✅ Code organization and modularity
- ✅ User experience design

## 🌟 Future Enhancements

- 5-day weather forecast
- GPS-based location detection
- Weather graphs with matplotlib
- Database storage for favorite cities
- Animated weather icons
- Dark/light theme toggle

## 📄 License

This project is open source and available under the MIT License.
