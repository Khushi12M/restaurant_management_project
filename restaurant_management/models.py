from django.db import models

class RestaurantInfo(models.Model):
    name= models.CharField(max_length=100)

    def_str_(self):
        return self.name