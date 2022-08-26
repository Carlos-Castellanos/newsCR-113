# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import( 
    CreateView, 
    DeleteView,
    UpdateView
)

from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    UserPassesTestMixin
   )   #113

from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# https://docs.djangoproject.com/en/4.1/ref/class-based-views/flattened-index/
from django.urls import reverse_lazy
from .models import Article

# Create your views here.

class ArticleListView(ListView):
    template_name = "articles/list.html"   
    model = Article


class ArticleDetailView(DetailView):
    template_name = "articles/detail.html"  
    model = Article

class ArticleCreateView(LoginRequiredMixin, CreateView): 
    template_name = "articles/new.html"  
    model = Article
    fields = ["title","subtitle","a_type","status","body"]  

    def form_valid(self, form):      
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): 
    template_name = "articles/edit.html"  
    model = Article
    fields = ["title","subtitle","a_type","status","body"]  

    def test_func(self):                                
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):  
    template_name = "articles/delete.html"  
    model = Article
    success_url = reverse_lazy('article_list')

    def test_func(self):                                
        obj = self.get_object()
        return obj.author == self.request.user
