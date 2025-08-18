from django.db import models
from django.contrib.auth.models import User

class MenuItem(models. Model):
    name = models.CharField(max_length=100)
    description= models.TextField()
    price= models.DecimalField(max_digits=8, decimal_places=2)


    def_str_(self):
        return self.name

       
 