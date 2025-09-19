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

