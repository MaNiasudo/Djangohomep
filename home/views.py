from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'website/index.html')

def about(request):
    return render(request, 'website/about.html')

def contact(request):
    return render(request, 'website/contact.html')

def testview(request):
    context = {'name':'taha','family':'efa'}
    return render(request, 'website/test.html',context)