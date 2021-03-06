from django.shortcuts import render
import requests
from .models import City

from .forms import CityForm

# Create your views here.

def index(request):

    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=ec5f2fe7c03091f1609b96cb1139265b"

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities:
        r = requests.get(url.format(city)).json()
        city_weather = {
            'city': city.name,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

    print(weather_data)

    context = {
        'weather_data' : weather_data,
        'form' : form
    }

    return render(request,'myweather/weather.html',context)
