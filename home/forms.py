from django import forms 
from home.models import Contact , Newsletter
from django.forms import ModelForm
from captcha.fields import CaptchaField


class ContactForm(forms.ModelForm):
    captcha = CaptchaField() # Using captcha for preventing spam attacks
    
    class Meta:
        model = Contact
        fields = '__all__'

class NewsletterForm(forms.ModelForm):

    class Meta:
        model = Newsletter
        fields = '__all__'