from __future__ import unicode_literals

from django.db import models
from datetime import date

# Create your models here.

class FoodBase(models.Model):
    # Core numbers for 100g of a food.
    name = models.CharField(max_length=255)
    fat = models.FloatField()
    protein = models.FloatField()
    carbs = models.FloatField()
    fiber = models.FloatField()
    alcohol = models.FloatField()
    def __str__(self):
        name = "{} {}g f, {}g p, {}g c, {}g f, {}g a".format(self.name,self.fat,self.protein,self.carbs,self.fiber,self.alcohol)
        return name

class Tag(models.Model):
    name = models.SlugField(max_length=255)
    friendly_name = models.CharField(max_length=255)

class Unit(models.Model):
    # eg 1 pound, 1 oz
    name = models.CharField(max_length=255, default="Unknown Unit of Measure")
    multiplier = models.FloatField(help_text="x 100g")
    def __str__(self):
        return "{} ({})".format(self.name,self.multiplier)

class Food(models.Model):
    # A food list item has an quantity associated with it.
    # A food is just a pairing of an amount and a foodbase and quanitity
    name = models.CharField(max_length=255, default="Unknown Food")
    foodbase = models.ForeignKey(FoodBase,related_name="base")
    unit = models.ForeignKey(Unit, null=True, blank=True)
    quantity = models.FloatField(default=1)
    def __str__(self):
        return "{} ({})".format(self.foodbase.name, self.unit.name)

class Dish(models.Model):
    # A dish is a collection of foods, meant to be saved and used again for speed of entry.
    name = models.CharField(max_length=255)
    foods = models.ManyToManyField(Food)
    def __str__(self):
        return self.name

class Log(models.Model):
    # A log is a list of foods and dishes consumed in a period.
    dishes = models.ManyToManyField(Dish, null=True,blank=True)
    foods = models.ManyToManyField(Food, null=True,blank=True)
    period = models.IntegerField(help_text='Hours of the period, typically 24',default=24)
    start_date = models.DateField(default=date.today)
    def __str__(self):
        return "Log: {}".format(self.start_date)












# garbage



