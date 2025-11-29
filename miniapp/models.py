from django.db import models

class SensorData(models.Model):
    temperature = models.FloatField(verbose_name='Temperature')
    humidity = models.FloatField(verbose_name='Humidity')
    co2 = models.FloatField(verbose_name='CO2')
    noise = models.FloatField(verbose_name='Noise level')
    light = models.FloatField(verbose_name='Light level')
    color = models.CharField(max_length=50, verbose_name='Color')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.timestamp} - {self.color}"

    def __str__(self):
        return f"{self.temperature, self.humidity, self.co2, self.noise, self.light, self.color}"