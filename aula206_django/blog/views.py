from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def blog(request):
    print("This is my blog")
    return HttpResponse("Hello, world! 1 This is my blog app.")

def exemplo(request):
    print("This is my exemplo")
    return HttpResponse("Hello, world! 1 This is my exemplo app.")