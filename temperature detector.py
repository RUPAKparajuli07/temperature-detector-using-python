import requests
import tkinter as tk
from tkinter import font
import time

API_KEY = "bc295a4bc8727b69c6df749ba9cc88be"

def get_temperature(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temperature = data["main"]["temp"] - 273.15
        return temperature
    else:
        return "Error: Could not retrieve temperature data."

def update_temperature():
    temperature = get_temperature(API_KEY, city_entry.get())
    if isinstance(temperature, str):
        temperature_label.config(text=temperature, fg="black")
    else:
        temperature_label.config(text=f"{temperature:.2f}°C")
        if temperature < 10:
            temperature_label.config(fg="blue")
        elif temperature < 20:
            temperature_label.config(fg="green")
        else:
            temperature_label.config(fg="red")

# Create the main window
window = tk.Tk()
window.title("Weather App")

# Set the background color based on the current time
current_time = int(time.strftime("%H"))
if current_time < 6 or current_time > 18:
    window.configure(background="dark blue")
else:
    window.configure(background="light blue")

# Create a frame for the city entry and label
city_frame = tk.Frame(window)
city_frame.grid(row=0, column=0, padx=10, pady=10)

# Create the city entry and label
city_label = tk.Label(city_frame, text="Enter City:")
city_label.grid(row=0, column=0)
city_entry = tk.Entry(city_frame, width=20)
city_entry.grid(row=0, column=1, padx=5)
city_entry.focus()

# Create a frame for the temperature label
temperature_frame = tk.Frame(window)
temperature_frame.grid(row=1, column=0, padx=10, pady=10)

# Create the temperature label
temperature_font = font.Font(size=24)
temperature_label = tk.Label(temperature_frame, text="", font=temperature_font)
temperature_label.pack()

# Create the button to update the temperature
update_button = tk.Button(window, text="Update Temperature", command=update_temperature)
update_button.grid(row=2, column=0, padx=10, pady=10)

# Make the window resizable
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.columnconfigure(0, weight=1)

# Start the main loop
window.mainloop()
