from tkinter import *
from tkinter import ttk
import requests

def get_weather(city):
    api_key = "5378aeb144a9ec3dd610244d296f76ff"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city
    response = requests.get(complete_url)
    data = response.json()
    if data["cod"] != "404":
        if "main" in data:
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            pressure = data["main"]["pressure"]
            weather_description = data["weather"][0]["description"]
            result = "Temperature (in Celsius unit) = " + str(round(temp-273.15, 2)) + "\nHumidity = " + str(humidity) + "\nPressure = " + str(pressure) + "\nWeather = " + str(weather_description)
        else:
            result = "Weather data not available"
    else:
        result = "City Not Found"
    return result


def show_weather():
    city = city_entry.get()
    weather_info = get_weather(city)
    weather_label.config(text=weather_info)

root = Tk()
root.title("Weather App")

root.geometry("512x512")

# Create the rest of the GUI elements
city_label = ttk.Label(root, text="Enter City Name :")
city_entry = ttk.Entry(root, width=30)
show_weather_button = ttk.Button(root, text="Show Weather", command=show_weather)
weather_label = ttk.Label(root, text="")

# Place the elements on the window
city_label.pack()
city_entry.pack()
show_weather_button.pack()
weather_label.pack()
try:
    # Load the image and create a PhotoImage object
    image = PhotoImage(file="background.png")
    # Create a label to display the image
    background_label = Label(root, image=image)
    background_label.pack(fill=BOTH, expand=True)
except Exception as e:
    print(e)

root.mainloop()
