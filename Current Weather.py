import tkinter as tk
from tkinter import ttk
import requests

API_KEY = 'YOUR_OPENWEATHERMAP_API_KEY'
CITY_NAME = 'YOUR_CITY_NAME'
UNITS = 'metric'  # You can use 'imperial' for Fahrenheit or 'metric' for Celsius

def get_weather():
    try:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&units={UNITS}&appid={API_KEY}'
        response = requests.get(url)
        data = response.json()

        if data['cod'] == '404':
            weather_label.config(text="City not found")
        else:
            main_info = data['weather'][0]['main']
            description = data['weather'][0]['description']
            temperature = data['main']['temp']

            weather_label.config(text=f"{main_info} - {description}\nTemperature: {temperature}°C")
    except Exception as e:
        weather_label.config(text=f"Error fetching data: {e}")

# GUI setup
root = tk.Tk()
root.title("Weather Display")

weather_label = ttk.Label(root, text="", font=("Helvetica", 14))
weather_label.pack(padx=10, pady=10)

refresh_button = ttk.Button(root, text="Refresh", command=get_weather)
refresh_button.pack(pady=10)

# Initial fetch
get_weather()

# Run the Tkinter main loop
root.mainloop()
