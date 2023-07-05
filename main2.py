import tkinter as tk
import requests

def get_weather():
    city = entry.get()
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=e5c7fd1692cdbb4dc58d39698a9fd8b6"
    response = requests.get(url)
    data = response.json()

    if 'weather' in data:
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        result['text'] = f"Weather: {weather}\nTemperature: {temperature}°F\nHumidity: {humidity}%\nWind Speed: {wind_speed} mph"
    else:
        result['text'] = "Error: Failed to fetch weather data."

root = tk.Tk()
root.title("Weather App")

label = tk.Label(root, text="Enter city name:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Get Weather", command=get_weather)
button.pack()

result = tk.Label(root, text="")
result.pack()

root.mainloop()
