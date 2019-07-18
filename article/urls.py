from django.contrib import admin
from django.urls import path
from . import views

app_name = "article"

urlpatterns = [
    path('', views.articles, name="articles"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('add_article/', views.add_article, name="add_article"),
    path('article/<int:id>', views.article_detail, name="article_detail"),
    path('update/<int:id>', views.update_article, name="update_article"),
    path('delete/<int:id>', views.delete_article, name="delete_article"),
    path('comment/<int:id>', views.add_comment, name="add_comment"),
]