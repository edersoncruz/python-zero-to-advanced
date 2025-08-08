from django.shortcuts import render

# Create your views here.

def blog(request):
    print("This is my blog view")
    return render(request, 'blog/index.html')

def exemplo(request):
    print("This is my exemplo view")
    return render(request, 'blog/exemplo.html')