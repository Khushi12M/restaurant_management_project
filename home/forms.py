from django import forms
from. models import Contact

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields= ['name', 'feedback_text']