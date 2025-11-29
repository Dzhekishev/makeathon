from django.shortcuts import render
from .models import SensorData
from rest_framework import generics
from .serializers import*

def sensordata(request):
    # Берём последние 50 записей
    data = SensorData.objects.all().order_by('-timestamp')[:50]

    # Готовим данные для графиков
    timestamps = [d.timestamp.strftime("%H:%M:%S") for d in reversed(data)]
    temperature = [d.temperature for d in reversed(data)]
    humidity = [d.humidity for d in reversed(data)]
    co2 = [d.co2 for d in reversed(data)]
    noise = [d.noise for d in reversed(data)]
    light = [d.light for d in reversed(data)]
    colors = [d.color for d in reversed(data)]

    context = {
        'timestamps': timestamps,
        'temperature': temperature,
        'humidity': humidity,
        'co2': co2,
        'noise': noise,
        'light': light,
        'colors': colors,
        'data_table': reversed(data),  # для таблицы
    }

    return render(request, 'miniapp/index.html', context)


class Sensordata_View(generics.ListCreateAPIView):
    queryset = SensorData.objects.all()
    serializer_class = SensorData_Serializers
