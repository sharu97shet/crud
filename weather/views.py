from django.shortcuts import render, redirect, HttpResponse
import requests

# import r
from .models import City
from .forms import CityForm
# Create your views here.


def index(request):

    cities = City.objects.all()

    # url = 'https://jsonplaceholder.typicode.com/users/1'
    # url = 'https://api.openweathermap.org/data/2.5/weather?q=""&appid=965ff3f2d751c3b33fae174324138c9e'
    err_msg = ''
    message = ''
    message_class = ''
    # r = requests.get(url).json()
    # print(r)

    form = CityForm()

    if request.method == 'POST':

        form = CityForm(request.POST)

        new_city = request.POST['name']

        print(new_city)

        form.save()

        if form.is_valid():

            weather_data = []

            # form = CityForm()
            url = f'https://api.openweathermap.org/data/2.5/weather?q={new_city}&appid=965ff3f2d751c3b33fae174324138c9e'

            print(url)

          # for city in cities:
            r = requests.get(url.format(new_city)).json()
            # r = requests.get(url.format(city)).json()
        city_weather = {
            'city': new_city,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }
        weather_data.append(city_weather)
        context = {
            'weather_data': weather_data,
            'form': form,
            'message': message,
            'message_class': message_class
        }
        return render(request, 'weather.html', context)

    # output = url.name  {'form': student}

    return render(request, 'weather.html', {'form': form})

    # return HttpResponse('op is ', r)

    # url = 'should_be_unique_for_you'
    url = requests.get('https://w3schools.com/python/demopage.htm')
    err_msg = ''
    message = ''
    message_class = ''
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            new_city = form.cleaned_data['name']
            existing_city_count = City.objects.filter(name=new_city).count()
            if existing_city_count == 0:
                r = requests.get(url.format(new_city)).json()
                if r['cod'] == 200:
                    form.save()
                else:
                    err_msg = 'City does not exist!'
            else:
                err_msg = 'City already exists!'
        if err_msg:
            message = err_msg
            message_class = 'is-danger'
        else:
            message = 'City added Successfully!'
            message_class = 'is_success'

    form = CityForm()
    cities = City.objects.all()
    weather_data = []
    for city in cities:
        r = requests.get(url.format(city)).json()
        city_weather = {
            'city': city.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }
        weather_data.append(city_weather)
    context = {
        'weather_data': weather_data,
        'form': form,
        'message': message,
        'message_class': message_class
    }
    return render(request, 'weather.html', context)


def abcd(request):

    return render(request, 'weather.html')


def delete_city(requests, city_name):
    City.objects.get(name=city_name).delete()
    return redirect('home')
