from django.shortcuts import render
from app.models import Car


def add_product(request):
    if request.method == "POST":
        car_brand = request.POST.get('brand')
        car_year = request.POST.get('year')
        car_color = request.POST.get('color')
        car_mileage = request.POST.get('mileage')
        car_price = request.POST.get('price')
        Car.objects.create(car_brand=car_brand,
                           car_year=car_year,
                           car_color=car_color,
                           car_mileage=car_mileage,
                           car_price=car_price)

    return render(request, 'add_product.html')


def show_cars(request):
    cars = Car.objects.all()
    return render(request, 'show_cars.html', {'cars': cars})
