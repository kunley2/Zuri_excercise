from django import forms
from .model import Post


class BlogForm(forms):
    
    class Meta:
        model = Post
        fields = '__all__'