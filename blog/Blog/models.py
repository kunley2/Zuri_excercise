from django.db import models
from django.contrib.auth import get_user_model#,models.User


User = get_user_model()
# Create your models here.
class Posts(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Created_date = models.DateTimeField() 
    Published_date = models.DateTimeField()
    
    class Meta:
        verbose_name = "Blog_posts"
        verbose_name_plural = "Blog_posts"
    
    def __str__(self):
        return self.name
    
        
       
        