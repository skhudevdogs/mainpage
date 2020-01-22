from django.shortcuts import render,redirect,get_object_or_404
from .models import Article,Comment

# Create your views here.
def main(request):
    return render(request, 'board/Notice.html')
def home(request):
    articles = Article.objects
    return render(request, 'board/Notice.html',{'articles':articles})

def new(request):
    return render(request, 'board/new.html')

def create(request):
    article = Article()
    article.title = request.GET['title']
    article.content = request.GET['content']
    # article.user_id = request.GET['user_id']
    article.save()
    return redirect('../')

def base(request):
    return render(request, 'board/base.html')

    
