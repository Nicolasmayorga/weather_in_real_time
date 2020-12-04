import requests
import os
import time
from datetime import datetime

# City request
city = input("Enter the city name: ")

#api authoruzation
api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=b74fbea137c6b26d931ae7ab48e59c38"
#apa = "https://api.openweathermap.org/data/2.5/forecast/daily?q="+city+"&cnt=7&appid={API key}"
#conditions    
json_data = requests.get(api).json()
condition = json_data['weather'][0]['main']

# data from the api 
temp = int(json_data['main']['temp'] - 273.15)
min_temp = int(json_data['main']['temp_min'] - 273.15)
max_temp = int(json_data['main']['temp_max'] - 273.15)
weather_desc = json_data['weather'][0]['description']
pressure = json_data['main']['pressure']
humidity = json_data['main']['humidity']
wind = json_data['wind']['speed']
sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))

date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")



print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(city.upper(), date_time))
print ("-------------------------------------------------------------")


print ("Current temperature is: {:.2f} C°".format(temp))
print ("The minimum temperature could be: {:.2f} C°".format(min_temp))
print ("The max temperature could be: {:.2f} C°".format(max_temp))
print ("Current weather desc: ",weather_desc)
print ("Current pressure: ",pressure)
print ("Current Humidity: ",humidity, '%')
print ("Current wind speed: ",wind ,'kmph')
print ("The sunrise will be at: ", sunrise)
print ("The sunset will be at :",sunset)


