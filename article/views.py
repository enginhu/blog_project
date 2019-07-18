"""
high level support for doing this and that.
"""
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ArticleForm

from .models import Article, Comment

# Create your views here.
def index(request):
    """
    Index Page
    """
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

@login_required(login_url="user:login")
def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context = {
        "articles":articles
    }
    return render(request, "dashboard.html", context)

@login_required(login_url="user:login")
def add_article(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request, "Article has been created.")
        return redirect("index")
    context = {
        "form": form
    }
    return render(request, "add_article.html",context)

@login_required(login_url="user:login")
def update_article(request, id):
    article = get_object_or_404(Article, id=id)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=article)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request, "Article has been successfully updated.")
        return redirect("index")

    return render(request, "update_article.html", {"form":form})

@login_required(login_url="user:login")
def delete_article(request, id):
    article = get_object_or_404(Article, id=id)
    article.delete()
    messages.success(request, "Article has been successfully deleted.")
    return redirect("article:dashboard")

def articles(request):
    keyword = request.GET.get("keyword")
    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        return render(request, "articles.html", {"articles":articles})
    articles = Article.objects.all()
    return render(request, "articles.html", {"articles":articles})

def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    comments = article.comments.all()
    return render(request, "article_detail.html",{"article":article, "comments":comments})

def add_comment(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")

        new_comment = Comment(comment_author=comment_author, comment_content=comment_content)
        new_comment.article = article
        new_comment.save()
    return redirect(reverse("article:article_detail", kwargs={"id":id}))
