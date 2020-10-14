from django.db import models
import datetime
from django.utils import timezone

class Date(models.Model):
    date = models.DateField(null=True)
    def showDate(self):
        return self.date

class Steps(models.Model):
    date = models.ForeignKey(Date, on_delete=models.CASCADE)
    number_of_steps = models.IntegerField(default=0)
    def showSteps(self):
        return self.number_of_steps