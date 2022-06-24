from django.urls import path
from . import views

app_name = 'Blog'
urlpatterns = [
    path('create/', views.PostCreateView.as_view(),name="create"),
    path('',views.PostListView.as_view(),name='index'),
    path('delete/<slug:slug>',views.PostDeleteView.as_view(),name='delete'),
    path('detail/<slug:slug>',views.DetailView.as_view(),name='detail'),
    path('update/<slug:slug>',views.PostUpdateView.as_view(),name='update')
]