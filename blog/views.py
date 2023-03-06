from django.shortcuts import render

posts = [
{    'author': 'Mika Sims',
    'title': 'Blog Post 1',
    'content': 'First post content',
    'created_at': 'May 27, 2022'},

{    'author': 'Jane Doe',
    'title': 'Blog Post 2',
    'content': 'Second post content',
    'created_at': 'March 14, 2022'}
]

def home(request):
    context ={
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})