from django.db import models

# Create your models here.
class TodaySpecial(models.Model):
    name = models.CharField(max_length=150)
    description = models.TexztField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    added_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return (self.name)