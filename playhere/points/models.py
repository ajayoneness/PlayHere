from django.db import models



class allpoints(models.Model):
    username = models.TextField(max_length=100)
    points = models.FloatField()
    timetaken = models.IntegerField()
    category = models.TextField(max_length=50,blank=True)
    gamename = models.TextField(max_length=100,blank=True)
