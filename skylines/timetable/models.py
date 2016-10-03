from __future__ import unicode_literals

from django.db import models


class User(models.Model):
    id = models.IntegerField()
    login = models.CharField(max_length = 10)
    password = models.CharField(max_length = 20)
    access_level = models.IntegerField()



class Airplane(models.Model):
    id = models.IntegerField()
    cost = models.IntegerField()
    seats = models.IntegerField()


class Airport(models.Model):
    id = models.IntegerFiled()
    name = models.CharField(max_length = 10)
    country = models.CharField(max_length = 10)

class TimeTable(models.Model):
    id_plane =  
# Create your models here.
