from django.shortcuts import render
from .models import City

import requests

def index(request):
    api_key = '04da3c1e475d3205fd68f53e365ea0b8'
    cities = City.objects.all()
    city_weather_list = []
    for city in cities:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        r = requests.get(url).json()
        data = {
        'city': r['name'],
        'temperature': r['main']['temp'],
        'pressure': r['main']['pressure'],
        'humidity': r['main']['humidity'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],}
        city_weather_list.append(data)

    context = {
        'city_weather_list': city_weather_list
    }

    return render(request, 'weatherapp/index.html', context)