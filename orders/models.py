from django.db import models

class RestaurantsInfo(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)

    
    def__str__(self):
        return self.name
