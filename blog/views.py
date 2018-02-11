from django.shortcuts import render
from django.http import  HttpResponse
from . models import  Post

posts = Post.objects.all()
def index(request):
    return render(request, 'index.html',{'posts':posts})

def post(request):
    return HttpResponse("Hi")

