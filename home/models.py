from django. db import models
class Feedback(models.Model):
    name= models.CharField(max_length=100)
    feedback_text= models.TextField()
    submitted_at = models.DateField(auto_now_add=True)
  

    def_str_(self):
        return self.name