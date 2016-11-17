from django.conf.urls import url
from foodtracker import views

# /food/food-name
# or then
# /food/uuid

# all foods values in 100g increments

# logger app.
# /log/
# Allows you to store and save a 


urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^log/$', views.logIndex, name="logIndex"),
    url(r'^food/$', views.foodIndex, name="foodIndex"),
    url(r'^food/(\d+)/', views.food, name="food")
]