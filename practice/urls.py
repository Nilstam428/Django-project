from django.contrib import admin
from django.urls import path, include
from . import views
# localhost:8000/practice_step
# localhost:8000/practice_step/
urlpatterns = [
    path('', views.practice_step, name='practice_step'),

]
