# Ex02 Django ORM Web Application
## Date:19.09.2025 

## AIM
To develop a Django application to store and retrieve data from a car Database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
~~~
admin.py

from django.contrib import admin
from .models import car,carAdmin
admin.site.register(car,carAdmin)

models.py

from django.db import models
from django.contrib import admin
class car(models.Model):
    cid=models.IntegerField()
    cname=models.CharField(max_length=100)
    rate=models.IntegerField()
    year=models.IntegerField()
    horse_power=models.FloatField()

class carAdmin(admin.ModelAdmin):
    list_display=('cid','cname','rate','year','horse_power')
~~~


## OUTPUT

![alt text](<Screenshot 2025-09-19 103554.png>)


## RESULT
Thus the program for creating movies database using ORM hass been executed successfully
