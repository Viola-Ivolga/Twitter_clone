from urllib import request
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
# Create your views here.

def index(request) :

    posts = Post.objects.all()[:20]


    return render(request, 'posts.html',
                   {'posts' : posts})


def delete(request, post_id):

    post = Post.objects.get(id = post_id)
    post.delete()  
    return HttpResponseRedirect('/')                   