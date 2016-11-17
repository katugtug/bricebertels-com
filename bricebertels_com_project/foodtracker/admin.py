from django.contrib import admin
from foodtracker.models import *
# Register your models here.

admin.site.register(FoodBase)
admin.site.register(Food)
admin.site.register(Dish)
admin.site.register(Log)
admin.site.register(Unit)
