from django.shortcuts import render, HttpResponse
from foodtracker.models import Food, Dish, Log, Unit, FoodBase
from django.core import serializers
# Create your views here.

def index(request):
    context = {}
    return render(request, "foodtracker/index.html", context)

def foodIndex(request):
    allFood = FoodBase.objects.all().order_by('name')
    context = {"allFood":allFood}
    return render(request, "foodtracker/foodIndex.html", context)

def logIndex(request):
    context = {}
    return render(request, "foodtracker/logIndex.html", context)

def food(request, id):
    foodbase = FoodBase.objects.all().filter(id=id)
    units = Unit.objects.all()

    class Calculation:
        def __init__(self, base, unit):
            self.name = "{} of {}".format(unit.name, base.name)
            self.fat = round(base.fat * unit.multiplier, 1)
            self.protein = round(base.protein * unit.multiplier, 1)
            self.carbs = round(base.carbs * unit.multiplier, 1)
            self.fiber = round(base.fiber * unit.multiplier, 1)
            self.alcohol = round(base.alcohol * unit.multiplier, 1)
    
    calculations = []

    for unit in units:
        calculations.append(Calculation(foodbase[0], unit))

    context = {"foodbase": foodbase[0],
               "calculations": calculations,
               "request":request.GET}

    if request.method == "GET":
        if "f" in request.GET:
            if request.GET['f'] == "json":            
                data = serializers.serialize('json', foodbase)
                returnvar = HttpResponse(data, content_type="application/json")
            else:
                returnvar = render(request, "foodtracker/food.html", context)
        else:
            returnvar = render(request, "foodtracker/food.html", context)
        return returnvar 