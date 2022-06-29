from django.urls import path
from . import views

urlpatterns = [
    path('',views.LinkListApi.as_view(),name='api-list'),
    path('create/', views.LinkCreateApi.as_view(),name='api-create'),
    path("delete/<int:pk>/", views.LinkDeleteView.as_view(), name="api-delete"),
    path("detail/<int:pk>", views.LinkDetailApi.as_view(), name="api-detail"),
    path("update/<int:pk>", views.LinkUpdateAPI.as_view(), name="api-update"),
]