"""
Advanced Weather App - GUI Version with Tkinter
A modern graphical weather application with enhanced features and user-friendly interface.
"""

import tkinter as tk
from tkinter import ttk, messagebox
import threading
from datetime import datetime
from weather_api import WeatherAPI
from config import WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE, COLORS


class WeatherGUI:
    """Main GUI class for the Weather Application"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.weather_api = WeatherAPI()
        self.current_units = "metric"  # metric or imperial
        self.current_weather_data = None
        
        self.setup_window()
        self.create_widgets()
        self.setup_styles()
    
    def setup_window(self):
        """Configure the main window"""
        self.root.title(WINDOW_TITLE)
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.configure(bg=COLORS["background"])
        self.root.resizable(True, True)
        
        # Center the window on screen
        self.center_window()
        
        # Set minimum window size
        self.root.minsize(500, 400)
    
    def center_window(self):
        """Center the window on the screen"""
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (WINDOW_WIDTH // 2)
        y = (self.root.winfo_screenheight() // 2) - (WINDOW_HEIGHT // 2)
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x}+{y}")
    
    def setup_styles(self):
        """Configure ttk styles"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure button styles
        style.configure('Search.TButton', 
                       background=COLORS["primary"], 
                       foreground='white',
                       font=('Arial', 10, 'bold'))
        
        style.configure('Unit.TButton',
                       background=COLORS["secondary"],
                       foreground='white',
                       font=('Arial', 9))
    
    def create_widgets(self):
        """Create and arrange all GUI widgets"""
        # Main container
        main_frame = tk.Frame(self.root, bg=COLORS["background"])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title
        title_label = tk.Label(main_frame, 
                              text="🌤️ Weather App", 
                              font=('Arial', 24, 'bold'),
                              bg=COLORS["background"],
                              fg=COLORS["text"])
        title_label.pack(pady=(0, 20))
        
        # Search frame
        self.create_search_frame(main_frame)
        
        # Weather display frame
        self.create_weather_frame(main_frame)
        
        # Status bar
        self.create_status_bar(main_frame)
    
    def create_search_frame(self, parent):
        """Create the search input section"""
        search_frame = tk.Frame(parent, bg=COLORS["background"])
        search_frame.pack(fill=tk.X, pady=(0, 20))
        
        # City input
        tk.Label(search_frame, 
                text="Enter City Name:", 
                font=('Arial', 12),
                bg=COLORS["background"],
                fg=COLORS["text"]).pack(anchor=tk.W)
        
        input_frame = tk.Frame(search_frame, bg=COLORS["background"])
        input_frame.pack(fill=tk.X, pady=(5, 0))
        
        self.city_entry = tk.Entry(input_frame, 
                                  font=('Arial', 12),
                                  width=30)
        self.city_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        self.city_entry.bind('<Return>', lambda e: self.search_weather())
        
        self.search_button = ttk.Button(input_frame,
                                       text="🔍 Search",
                                       style='Search.TButton',
                                       command=self.search_weather)
        self.search_button.pack(side=tk.RIGHT)
        
        # Unit toggle frame
        unit_frame = tk.Frame(search_frame, bg=COLORS["background"])
        unit_frame.pack(fill=tk.X, pady=(10, 0))
        
        tk.Label(unit_frame,
                text="Temperature Unit:",
                font=('Arial', 10),
                bg=COLORS["background"],
                fg=COLORS["text"]).pack(side=tk.LEFT)
        
        self.celsius_button = ttk.Button(unit_frame,
                                        text="°C",
                                        style='Unit.TButton',
                                        width=5,
                                        command=lambda: self.toggle_units("metric"))
        self.celsius_button.pack(side=tk.LEFT, padx=(10, 5))
        
        self.fahrenheit_button = ttk.Button(unit_frame,
                                           text="°F", 
                                           style='Unit.TButton',
                                           width=5,
                                           command=lambda: self.toggle_units("imperial"))
        self.fahrenheit_button.pack(side=tk.LEFT)
    
    def create_weather_frame(self, parent):
        """Create the weather information display section"""
        # Weather container with border
        weather_container = tk.Frame(parent, 
                                   bg='white',
                                   relief=tk.RAISED,
                                   borderwidth=2)
        weather_container.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Scrollable frame for weather info
        canvas = tk.Canvas(weather_container, bg='white')
        scrollbar = ttk.Scrollbar(weather_container, orient="vertical", command=canvas.yview)
        self.weather_frame = tk.Frame(canvas, bg='white')
        
        self.weather_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=self.weather_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Initial message
        self.show_initial_message()
    
    def create_status_bar(self, parent):
        """Create the status bar at the bottom"""
        self.status_var = tk.StringVar()
        self.status_var.set("Ready - Enter a city name to get weather information")
        
        status_bar = tk.Label(parent,
                             textvariable=self.status_var,
                             font=('Arial', 9),
                             bg=COLORS["background"],
                             fg=COLORS["text"],
                             anchor=tk.W)
        status_bar.pack(fill=tk.X, side=tk.BOTTOM)
    
    def show_initial_message(self):
        """Display initial welcome message"""
        for widget in self.weather_frame.winfo_children():
            widget.destroy()
        
        welcome_frame = tk.Frame(self.weather_frame, bg='white')
        welcome_frame.pack(expand=True, fill=tk.BOTH)
        
        tk.Label(welcome_frame,
                text="🌍",
                font=('Arial', 48),
                bg='white').pack(pady=(50, 20))
        
        tk.Label(welcome_frame,
                text="Welcome to Weather App!",
                font=('Arial', 18, 'bold'),
                bg='white',
                fg=COLORS["text"]).pack(pady=(0, 10))
        
        tk.Label(welcome_frame,
                text="Enter a city name above and click Search\nto get current weather information.",
                font=('Arial', 12),
                bg='white',
                fg=COLORS["text"],
                justify=tk.CENTER).pack()
    
    def search_weather(self):
        """Search for weather data in a separate thread"""
        city = self.city_entry.get().strip()
        if not city:
            messagebox.showwarning("Input Error", "Please enter a city name.")
            return
        
        # Disable search button and show loading
        self.search_button.configure(state='disabled', text="Searching...")
        self.status_var.set(f"Fetching weather data for {city}...")
        
        # Run API call in separate thread to prevent GUI freezing
        thread = threading.Thread(target=self._fetch_weather_data, args=(city,))
        thread.daemon = True
        thread.start()
    
    def _fetch_weather_data(self, city):
        """Fetch weather data from API (runs in separate thread)"""
        success, data = self.weather_api.get_weather_data(city, self.current_units)
        
        # Update GUI in main thread
        self.root.after(0, self._update_weather_display, success, data)
    
    def _update_weather_display(self, success, data):
        """Update the weather display with fetched data"""
        # Re-enable search button
        self.search_button.configure(state='normal', text="🔍 Search")
        
        if success:
            self.current_weather_data = data
            self.display_weather_data(data)
            self.status_var.set(f"Weather data updated for {data['city']} - {datetime.now().strftime('%H:%M:%S')}")
        else:
            self.show_error_message(data['error'])
            self.status_var.set("Error fetching weather data")
    
    def display_weather_data(self, data):
        """Display weather information in the GUI"""
        # Clear previous content
        for widget in self.weather_frame.winfo_children():
            widget.destroy()
        
        # Main weather info frame
        main_info = tk.Frame(self.weather_frame, bg='white')
        main_info.pack(fill=tk.X, padx=20, pady=20)
        
        # City and country
        city_text = f"{data['city']}"
        if data['country']:
            city_text += f", {data['country']}"
        
        tk.Label(main_info,
                text=city_text,
                font=('Arial', 20, 'bold'),
                bg='white',
                fg=COLORS["text"]).pack()
        
        # Weather icon and description
        icon = WeatherAPI.get_weather_icon(data['description'])
        tk.Label(main_info,
                text=f"{icon} {data['description']}",
                font=('Arial', 16),
                bg='white',
                fg=COLORS["text"]).pack(pady=(5, 15))
        
        # Temperature section
        temp_frame = tk.Frame(self.weather_frame, bg='white')
        temp_frame.pack(fill=tk.X, padx=20, pady=(0, 20))
        
        unit_symbol = "°C" if self.current_units == "metric" else "°F"
        
        # Main temperature
        tk.Label(temp_frame,
                text=f"{data['temperature']}{unit_symbol}",
                font=('Arial', 36, 'bold'),
                bg='white',
                fg=COLORS["primary"]).pack()
        
        tk.Label(temp_frame,
                text=f"Feels like {data['feels_like']}{unit_symbol}",
                font=('Arial', 12),
                bg='white',
                fg=COLORS["text"]).pack()
        
        # Details section
        self.create_details_section(data, unit_symbol)
    
    def create_details_section(self, data, unit_symbol):
        """Create the detailed weather information section"""
        details_frame = tk.Frame(self.weather_frame, bg='white')
        details_frame.pack(fill=tk.X, padx=20, pady=(0, 20))
        
        tk.Label(details_frame,
                text="Weather Details",
                font=('Arial', 14, 'bold'),
                bg='white',
                fg=COLORS["text"]).pack(pady=(0, 10))
        
        # Create grid of details
        grid_frame = tk.Frame(details_frame, bg='white')
        grid_frame.pack(fill=tk.X)
        
        details = [
            ("💧 Humidity", f"{data['humidity']}%"),
            ("🌬️ Wind Speed", f"{data['wind_speed']} m/s"),
            ("☁️ Cloudiness", f"{data['cloudiness']}%"),
            ("📊 Pressure", f"{data['pressure']} hPa"),
            ("👁️ Visibility", f"{data['visibility']} km"),
            ("🧭 Wind Direction", f"{data['wind_direction']}°")
        ]
        
        for i, (label, value) in enumerate(details):
            row = i // 2
            col = i % 2
            
            detail_frame = tk.Frame(grid_frame, bg='white')
            detail_frame.grid(row=row, column=col, sticky='w', padx=(0, 40), pady=5)
            
            tk.Label(detail_frame,
                    text=label,
                    font=('Arial', 10, 'bold'),
                    bg='white',
                    fg=COLORS["text"]).pack(anchor='w')
            
            tk.Label(detail_frame,
                    text=value,
                    font=('Arial', 10),
                    bg='white',
                    fg=COLORS["text"]).pack(anchor='w')
    
    def show_error_message(self, error_message):
        """Display error message in the weather frame"""
        for widget in self.weather_frame.winfo_children():
            widget.destroy()
        
        error_frame = tk.Frame(self.weather_frame, bg='white')
        error_frame.pack(expand=True, fill=tk.BOTH)
        
        tk.Label(error_frame,
                text="❌",
                font=('Arial', 48),
                bg='white',
                fg=COLORS["error"]).pack(pady=(50, 20))
        
        tk.Label(error_frame,
                text="Error",
                font=('Arial', 18, 'bold'),
                bg='white',
                fg=COLORS["error"]).pack(pady=(0, 10))
        
        tk.Label(error_frame,
                text=error_message,
                font=('Arial', 12),
                bg='white',
                fg=COLORS["text"],
                wraplength=400,
                justify=tk.CENTER).pack()
        
        # Show helpful tips for common errors
        if "not found" in error_message.lower():
            tips_text = ("💡 Tips:\n"
                        "• Check the spelling of the city name\n"
                        "• Try using the full city name\n"
                        "• Include country name (e.g., 'London, UK')")
        elif "api key" in error_message.lower():
            tips_text = ("💡 To fix this:\n"
                        "• Sign up at openweathermap.org\n"
                        "• Get your free API key\n"
                        "• Update API_KEY in config.py")
        else:
            tips_text = "💡 Please check your internet connection and try again."
        
        tk.Label(error_frame,
                text=tips_text,
                font=('Arial', 10),
                bg='white',
                fg=COLORS["text"],
                justify=tk.LEFT).pack(pady=(20, 0))
    
    def toggle_units(self, units):
        """Toggle between Celsius and Fahrenheit"""
        if units != self.current_units:
            self.current_units = units
            
            # Update button states
            if units == "metric":
                self.celsius_button.configure(state='disabled')
                self.fahrenheit_button.configure(state='normal')
            else:
                self.celsius_button.configure(state='normal')
                self.fahrenheit_button.configure(state='disabled')
            
            # Refresh display if we have current data
            if self.current_weather_data:
                city = self.current_weather_data['city']
                self.search_weather()
    
    def run(self):
        """Start the GUI application"""
        # Set initial button states
        self.celsius_button.configure(state='disabled')
        
        # Focus on city entry
        self.city_entry.focus()
        
        # Start the main loop
        self.root.mainloop()


def main():
    """Main function to run the GUI application"""
    try:
        app = WeatherGUI()
        app.run()
    except Exception as e:
        messagebox.showerror("Application Error", f"An unexpected error occurred:\n{str(e)}")


if __name__ == "__main__":
    main()
