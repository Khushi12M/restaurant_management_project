from django.db import models


class RestaurantInfo(models.Model):
     name = models.CharField(max_length=255)
     history= models.TextField()
     mission = models.TextField()
    

    

    def_str_(self):
        return self.name
       