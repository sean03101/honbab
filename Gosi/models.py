from django.db import models
from datetime import datetime
from django.utils.dateformat import DateFormat
from datetime import timedelta
import datetime

# Create your models here.


class Gosi(models.Model):
    Gosiname = models.CharField(max_length=200)

    morning = models.TextField()    
    lunch = models.TextField()    
    dinner = models.TextField()    
    
    date = models.DateField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)