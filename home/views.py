from django.shortcuts import render
from home.models import Contact
from home.forms import ContactForm , NewsletterForm
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,'website/index.html')

def about(request):
    return render(request, 'website/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
           form.save()
        messages.success(request, "Your Message Sended")


    form = ContactForm()    
    return render(request, 'website/contact.html', {'form':form})

def news_letter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')
        

    

    