from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView
from . import views

urlpatterns = [
    path('', BlogListView.as_view(), name="index"),
    path('detail/<int:pk>/', BlogDetailView.as_view(), name="detail"),
    path('create/', BlogCreateView.as_view(), name="create"),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name="update"),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name="delete"),
]
