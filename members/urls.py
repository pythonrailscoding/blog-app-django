from django.urls import path
from django.contrib.auth.views import PasswordChangeView
from .views import BlogUserCreateView, BlogUserUpdateView, BlogUserPasswordChangeView, BlogUserProfilePage, BlogUserCreateProfilePageView, BlogUserShowProfilePageView
from django.contrib.auth.models import User

urlpatterns = [
	path('register/', BlogUserCreateView.as_view(), name="register"),
	path('<int:pk>/edit_profile_page/', BlogUserUpdateView.as_view(), name='edit_profile_page'),
	path('<int:pk>/password/', BlogUserPasswordChangeView.as_view(), name='change'),
	path('<int:pk>/edit_profile/', BlogUserProfilePage.as_view(), name='edit_profile'),
	path('create_profile/', BlogUserCreateProfilePageView.as_view(), name='create_profile_page'),
	path('<int:pk>/show/', BlogUserShowProfilePageView.as_view(), name='show_profile_page'),
]
