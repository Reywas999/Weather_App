#!/usr/bin/env python
# coding: utf-8

# In[1]:

# Retrieve a FREE API key from https://home.openweathermap.org/
api_key = "YOURAPIKEY"


# In[2]:

# Necessary imports
import tkinter as tk
from PIL import Image, ImageTk
import requests
from tkinter import Tk, Button, Label, Entry
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[6]:

# Weather class storing all of the functions to retrieve the weather data
class Weather:
    def __init__(self, api_key):
        # Initilize the api key
        self.api_key = api_key

    def get_weather_by_town(self, town):
        # Create and pull the correct URL given an input town
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = base_url + "appid=" + self.api_key + "&q=" + town + "&units=metric"
        response = requests.get(complete_url)
        # Raise error if the API key is invalid (or if the free version no longer permits this data pull)
        if response.status_code == 401:
            return {"cod": "401", "message": "Invalid API key or subscription level issue"}
        # Return the URL response
        return response.json()

    def get_weather_by_geolocation(self):
        # Retrieves the URL for the user location if their location is accessible.
        lat, lon = self.get_location()
        if lat is not None and lon is not None:
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            complete_url = base_url + "appid=" + self.api_key + "&lat=" + str(lat) + "&lon=" + str(lon) + "&units=metric"
            response = requests.get(complete_url)
            return response.json()
        else:
            return {"cod": "404"}

    def get_location(self):
        # Returns the coordinates of the user location if it is accessible
        try:
            geolocator = Nominatim(user_agent="my_weather_app")
            location = geolocator.geocode("Your Address")
            if location:
                return location.latitude, location.longitude
            else:
                raise ValueError("Location not found")
        except (GeocoderTimedOut, GeocoderServiceError) as e:
            print(f"Geocoding error: {e}")
            return None, None

    def show_weather_with_icon(self, city):
        # takes a city input, calls the get_weather_by_town function to retrieve the URL response for that city
        # Then displays the weather metrics described below along with an accompanying icon.
        try:
            weather = self.get_weather_by_town(city)
            if weather["cod"] != "404":
                main = weather["main"]
                wind = weather["wind"]
                weather_desc = weather["weather"][0]["description"]
                temp = main["temp"]
                pressure = main["pressure"]
                humidity = main["humidity"]
                wind_speed = wind["speed"]
                
                weather_info = f"Temperature: {temp}°C\nPressure: {pressure} hPa\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s\nDescription: {weather_desc}"
                
                icon_code = weather["weather"][0]["icon"]
                icon_url = f"http://openweathermap.org/img/wn/{icon_code}.png"
                icon_response = requests.get(icon_url, stream=True)
                icon_image = Image.open(icon_response.raw)
                icon_photo = ImageTk.PhotoImage(icon_image)
                
                weather_label.config(text=weather_info, image=icon_photo, compound='left')
                weather_label.image = icon_photo
            else:
                weather_info = "City Not Found!"
                weather_label.config(text=weather_info)
        except Exception as e:
            weather_label.config(text=f"Error: {e}")

    def show_forecast(self, city):
        # Takes a city input, retrieves the URL response using the get_weather_by_town function, and then
        # Outputs the 5-day forecast
        try:
            forecast = self.get_weather_by_town(city)
            if forecast["cod"] != "404":
                forecast_info = ""
                for item in forecast["list"][:5]:
                    date = item["dt_txt"]
                    temp = item["main"]["temp"]
                    description = item["weather"][0]["description"]
                    forecast_info += f"{date}\nTemperature: {temp}°C\nDescription: {description}\n\n"
            else:
                forecast_info = "City Not Found!"
            
            forecast_label.config(text=forecast_info)
        except Exception as e:
            forecast_label.config(text=f"Error: {e}")

    def show_weather_by_location(self):
        # Calls the get_weather_by_geolocation function to retrieve user location and then displays their
        # weather.
        try:
            weather = self.get_weather_by_geolocation()
            if weather["cod"] != "404" and "main" in weather and "wind" in weather and "weather" in weather:
                main = weather["main"]
                wind = weather["wind"]
                weather_desc = weather["weather"][0]["description"]
                temp = main["temp"]
                pressure = main["pressure"]
                humidity = main["humidity"]
                wind_speed = wind["speed"]
                
                weather_info = f"Temperature: {temp}°C\nPressure: {pressure} hPa\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s\nDescription: {weather_desc}"
            else:
                weather_info = "Location Not Found or Invalid API Response!"
            
            weather_label.config(text=weather_info)
        except Exception as e:
            weather_label.config(text=f"Error: {e}")

def get_weather_with_icon():
    # Retrieving a city input and then calling the show_weather_with_icon function to retrieve weather data
    city = city_entry.get()
    weather_app.show_weather_with_icon(city)

def get_forecast():
    # Retrieving a city input and then calling the show_forecast function to retrieve weather forecast data
    city = city_entry.get()
    weather_app.show_forecast(city)

def get_weather_by_location():
    # Calling the show_weather_by_location function to retrieve weather data for user location.
    weather_app.show_weather_by_location()

# Initialize the Weather class with your API key
weather_app = Weather(api_key)

# Tkinter GUI setup
root = tk.Tk()
root.title("Weather App")

### Combining all of the possible functions into one UI: ###
city_entry = Entry(root)
city_entry.pack()

weather_label = Label(root, text="")
weather_label.pack()

get_weather_icon_button = Button(root, text="Get Weather with Icon", command=get_weather_with_icon)
get_weather_icon_button.pack()

get_forecast_button = Button(root, text="Get 5-Day Forecast", command=get_forecast)
get_forecast_button.pack()

get_location_weather_button = Button(root, text="Get Weather by Location", command=get_weather_by_location)
get_location_weather_button.pack()

forecast_label = Label(root, text="", font=("Helvetica", 14))
forecast_label.pack()

# Running the script
root.mainloop()


# In[ ]:




