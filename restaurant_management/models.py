from django.db import models
import json

class Restaurant(models.Model):
     address = models.CharField(max_length=255)
     city = models.CharField(max_length=100)
     state = models.CharField(max_length=100)
    zip_code models.CharField(max_length=20)

    opening_hours = models.JSONField(default=dict)

    def_str_(self):
        return self.name
       