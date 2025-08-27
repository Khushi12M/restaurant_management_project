from django.db import models


class RestaurantInfo(models.Model):
     name = models.CharField(max_length=20)
    address = models.TextField()
    phone = models.CharField(max_length=20, blank=true, null=true)
    email= models.EmailField(blank=True, null=True)

    
    def_str_(self):
        return self.name
       