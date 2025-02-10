from django.http import HttpResponse

from django.shortcuts import render

def home(request):
   # return HttpResponse("Home page")
   
   return render(request, 'website/index.html')

def about(request):
    return HttpResponse("About page")

def contact(request):
    return HttpResponse("contact page")