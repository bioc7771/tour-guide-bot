import requests
def Weather(city):
    API_key = "e77820355cbac076ad2f89e8bb738ca5"    #"Your API Key here"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    #base_url = "https://api.openweathermap.org/data/2.5/weather?id=524901&appid=API_KEY"
    #base_url = "https://api.openweathermap.org/data/2.5/weather?id=524901"
    
    Final_url = base_url + "appid=" + API_key + "&q=" + city + "&units=metric"
    weather_data = requests.get(Final_url).json()
    
    return weather_data['main']
