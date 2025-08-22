from django import forms

class ContactForm(forms.form)
name = forms.CharField(max_length=100, request=True)
email = forms.EmailField(required=True)
message = forms.CharField(widget= forms.Textarea, required=True)