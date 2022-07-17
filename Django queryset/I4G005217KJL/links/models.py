from django.db import models
from django.contrib.auth.models import User
from .managers import ActiveLinkManager 

# Create your models here.
class Link(models.Model):
    target_url = models.URLField(max_length=200)
    description = models.CharField(max_length=200)
    identifier = models.SlugField(max_length=50,unique=True,blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField()
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.target_url
    
    objects = models.Manager
    public = ActiveLinkManager()
    