from django.db import models


class AboutUs(models.Model):
     title= models.CharField(max_length=255, default="About Our Restaurant")
     description = models.TextField()
      image = models.TextField(upload_to='about_us/',blank=True, null=True)
    

    

    def_str_(self):
        return self.title
       