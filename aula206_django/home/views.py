from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    print("This is my Home view")
    return HttpResponse("Hello, world! 1 This is my Home app")