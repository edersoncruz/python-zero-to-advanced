from django.shortcuts import render

# Create your views here.

def home(request):
    print("This is my Home view")
    return render(request, 'home/index.html')