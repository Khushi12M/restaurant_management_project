from django.db import models

class RestaurantAddress(models.Model):
     address = models.CharField(max_length=255)
     city = models.CharField(max_length=100)
     state = models.CharField(max_length=100)
    zip_code models.CharField(max_length=20)

    def_str_(self):
        return f "{self.address},{self.city}, {self.state} -{self.zip_code}"