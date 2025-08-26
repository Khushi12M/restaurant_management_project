from django.db import models


class OpeningHour(models.Model):
     day = models.CharField(max_length=20)
     open_time = models.TextField()
    close_time = models.TextField()
    

    

    def_str_(self):
        return f" {self.day}: {self.open_time.strftime('%I:%M %P)}
       