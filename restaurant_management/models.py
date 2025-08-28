from django.db import models


class Chef(models.Model):
     name = models.CharField(max_length=20)
     bio = models.TextField()
    phone = models.CharField(max_length=20, blank=true, null=true)
   

    
    def_str_(self):
        return self.name
       