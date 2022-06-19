from django.db import models

class TimeTable(models.Model):
    name = models.CharField(max_length=400)
    time_duration = models.CharField(max_length=400)
    link = models.CharField(max_length=400)