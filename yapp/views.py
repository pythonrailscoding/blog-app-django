from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy
from .forms import PostForm

class BlogListView(ListView):
    model = Post
    template_name = 'yapp/index.html'
    ordering = ['-date']

class BlogDetailView(DetailView):
    model = Post
    template_name = 'yapp/detail.html'

class BlogCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'yapp/create.html'
    success_url = reverse_lazy('index')

class BlogUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    #fields = '__all__'
    template_name = 'yapp/update.html'
    success_url = reverse_lazy('index')

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'yapp/delete.html'
    success_url = reverse_lazy('index')

