from django.shortcuts import render,redirect,get_object_or_404
from .models import Article,Comment
from django.utils import timezone
from user.models import CustomUser
from .forms import ArticleForm
# from django.core.paginator import paginator

# Create your views here.
def main(request):
    return render(request, 'board/Notice.html')
def read(request):
    articles = Article.objects
    article_list = Article.objects.all()
    # paginator = Paginator(article_list, 10)
    # page = request.GET.get('page')
    return render(request, 'board/Notice.html',{'articles':articles})

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.time = timezone.now()
            post.save()
            return redirect('../') 
    else:
        form = ArticleForm()
        return render(request, 'board/new.html', {'form':form})
    

    
