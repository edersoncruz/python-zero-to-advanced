from django.shortcuts import render
from blog.data import posts

# Create your views here.

def blog(request):
    print("This is my blog view")

    context = {
            'text': 'Estamos no BLOGG',
            'posts': posts
        }
    
    return render(
        request, 
        'blog/index.html',
        context
        )

def exemplo(request):
    print("This is my exemplo view")

    context = {
            'text': 'Estamos nO EXEMPLOOO',
            'title': 'Exemplo - '
        }
    
    return render(
        request, 
        'blog/exemplo.html',
        context
        )

def post(request, post_id):
    found_post: dict = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break
        

    context = {
            'text': 'Estamos no postss',
            'post': found_post,
            'title': found_post['title'] + ' - '
        }
    
    return render(
        request, 
        'blog/post.html',
        context
        )