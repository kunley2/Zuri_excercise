from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView, DeleteView,UpdateView
from .models import Posts
from django.urls import reverse,reverse_lazy




class PostCreateView(CreateView):
    model = Posts
    fields = '__all__'
    template_name = "Blog/create.html"
    success_url = reverse_lazy('Blog:index')
    
    
    
class PostListView(ListView):
    model = Posts
    template_name = "Blog/post_list.html"
    fields = "__all__"
    
    
class PostDetailView(DetailView):
    model = Posts
    template_name = "Blog/detail.html"
    
class PostDeleteView(DeleteView):
    model = Posts
    template_name = "Blog/delete.html"
    fields = "__all__"
    success_url = reverse_lazy('Blog:index')
    
class PostUpdateView(UpdateView):
    model = Posts
    template_name = "Blog/create.html"
    fields = "__all__"
    success_url = reverse_lazy('Blog:index')
    






