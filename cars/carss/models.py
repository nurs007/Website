from django.db import models
from django.utils import timezone

class Carrs (models.Model):
    types_of_car = models.CharField(max_length = 50)
    description = models.TextField()
    mileage =  models.CharField(max_length = 50)
    location_of_the_car = models.CharField(max_length = 50)
    prace_of _the_car = models.DecimalField(max_digits=50, decimal_places=5, default="")
    photos =models.ImageField(upload_to='относительный каталог для файлов/', blank=True, verbose_name='подпись')
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
