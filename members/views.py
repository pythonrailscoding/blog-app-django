from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.models import User
from .forms import RegisterForm, EditProfileForm, BlogPasswordChangeForm, BlogUserProfileForm, BlogUserCreateProfilePageForm
from django.urls import reverse_lazy
from django.contrib import messages
from yapp.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin

class BlogUserCreateView(CreateView):
    model = User
    form_class = RegisterForm
    #form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class BlogUserProfilePage(UpdateView):
	model = Profile
	#fields = '__all__'
	form_class = BlogUserProfileForm
	template_name = 'edit_profile_page.html'
	success_url = reverse_lazy('index')

class BlogUserUpdateView(LoginRequiredMixin, UpdateView):
	model = User
	form_class = EditProfileForm
	template_name = 'registration/update.html'
	success_url = reverse_lazy('index')

class BlogUserPasswordChangeView(PasswordChangeView):
	form_class = BlogPasswordChangeForm
	template_name = 'registration/change-password.html'
	success_url = reverse_lazy('index')
	'''
	def get_context_data(self, *args, **kwargs):
		#users = User.objects.all()
		#context = BlogUserPasswordChangeView.get_context_data(*args, **kwargs)

		page_user = get_object_or_404(User, id=self.kwargs['pk'])

		#context['page_user'] = page_user
		return page_user	
		'''	

class BlogUserCreateProfilePageView(LoginRequiredMixin, CreateView):
	model = Profile
	#fields = '__all__'
	form_class = BlogUserCreateProfilePageForm
	template_name = 'edit_profile.html'
	success_url = reverse_lazy('index')

class BlogUserShowProfilePageView(DetailView):
	model = Profile
	template_name = 'show_profile.html'

	def get_context_data(self, *args, **kwargs):
		users = Profile.objects.all()
		context = super(BlogUserShowProfilePageView, self).get_context_data(*args, **kwargs)

		page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

		context['page_user'] = page_user
		return context

class BlogUserUpdateView(LoginRequiredMixin, UpdateView):
	model = User
	form_class = EditProfileForm
	template_name = 'registration/change_user.html'
	success_url = reverse_lazy('index')
	def get_context_data(self, *args, **kwargs):
		users = User.objects.all()
		context = super(BlogUserUpdateView, self).get_context_data(*args, **kwargs)

		page_user = get_object_or_404(User, id=self.kwargs['pk'])

		context['page_user'] = page_user
		return context

