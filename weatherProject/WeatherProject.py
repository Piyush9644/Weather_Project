import requests
import os
from datetime import datetime

user_api = os.environ['Weather_Data']
location = input("enter the city name: ")

complete_api_link = "https://api.openwheatherapp.org/data/2.5/weather?q="+location+"&appid="+user_api
#print (compete_api_link)
api_link = requests.get(complete_api_link)
api_data = api_link.json()

if api_data['cod'] == '404':
    print ("invalid city: {}, please check you city name".format(location))
else:
    #create variables to store and display data
    temp_city = ((api_data['main']['temp']) - 273.15)
    weather_desc = api_data['weather'][θ]['description']
    hmdt = api_data['main']['humidity']
    wind_spd =api_data['wind']['speed']
    date_time = datetime.now().strftime("%d %b %y | %I:%M:%S %p")

    print ("----------------------------------------------------------")
    print ("weather stats for - {}  ||  {}".format(location.upper(), date_time))
    print ("----------------------------------------------------------")

    print ("current temperature is: {:.2f} deg c".format(temp_city))
    print ("current weather desc  :",weather_desc)
    print ("current weather desc  :",hmdt, '%')
    print("current wind speed     :",wind_spd ,'kmph')

