# Weather App 

A simple weather app that displays the temperature, humidity, pressure, and weather description of a given city.

## Requirements

Python 3
Tkinter
Requests
Usage

1. Clone the repository - heading

```
git clone https://github.com/[username]/weather-app.git - block
```

2. Install the required packages
```
pip install tkinter requests
```

3. Run the script
```
python3 main.py
```

Features

+ User can enter the name of a city
- The app retrieves and displays the weather information of the given city

# Code Description

- The get_weather function takes a city name as an input and returns the weather information of the city
+ The show_weather function retrieves the city name entered by the user and calls the get_weather function to display the weather information
* The GUI is built using Tkinter and displays the city name entry field, a "Show Weather" button, and the weather information.
+ The background image is added to the GUI (if the image background.png is available in the working directory)

Limitations

+ The app only works if the city name is entered correctly.
- The app only displays the weather information of the given city and does not provide any suggestions if the city is not found.
* The app is only capable of retrieving the weather information of the given city and not capable of storing the information for future use.