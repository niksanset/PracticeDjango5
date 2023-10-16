from django.db import models


class Car(models.Model):
    car_brand = models.CharField(max_length=100)
    car_year = models.IntegerField()
    car_color = models.CharField(max_length=100)
    car_mileage = models.IntegerField()
    car_price = models.IntegerField()

    def __str__(self):
        return f"{self.car_brand} - {self.car_year} - {self.car_color} - {self.car_mileage} - {self.car_price}"
