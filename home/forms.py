from django import forms


class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=100. required=True)
    email =forms .EmailField(required=True)
    message = forms. CharField(widget=forms.Textarea, required=True)
  
    
       