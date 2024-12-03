from django import forms 
from home.models import Contact , Newsletter
from django.forms import ModelForm


class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = '__all__'

class NewsletterForm(forms.ModelForm):

    class Meta:
        model = Newsletter
        fields = '__all__'