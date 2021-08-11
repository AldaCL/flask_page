from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.


posts = [
    {
        'author' : 'Corey S',
        'title' :'Blog post 1',
        'content' : 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author' : 'Jane Doe',
        'title' :'Blog post 2',
        'content' : 'Seconf post content',
        'date_posted': 'August 47, 2018'
    }
]

def home (request):

    context = {
        'posts' : posts
    }

    return render(request,'blog/home.html',context)


def about (request):
    return render(request,'blog/about.html', {'title':'About'})

