from django.db import models
import datetime

# Create your models here.

class DRFTest(models.Model):
    name = models.CharField(max_length=125, null=False, blank=False, unique=True)
    date_added = models.DateField(default=datetime.datetime.now())
    image = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=5000, null=True, blank=True)
