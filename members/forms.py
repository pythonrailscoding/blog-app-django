from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from yapp.models import Profile

class RegisterForm(UserCreationForm):
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Enter Your Email'}))
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')

	def __init__(self, *args, **kwargs):
		super(RegisterForm, self).__init__( *args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'Enter Your Username'
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Enter Your Password'
		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Re-enter Your Password'


	#class Meta:
		'''
		model = User
		fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email')

		widgets = {
			'username': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your Username'}),
			'password1': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your Password'}),
			"password2": forms.TextInput(attrs={'class':'form-control', 'placeholder':'Re - Enter Your Password'}),
			'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
			'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),
			'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter Your Email'}),

		}
		'''

class EditProfileForm(UserChangeForm):
	
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Update your Email'}))
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Your First Name'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Your Last Name'}))
	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Your Username'}))
	#last_login = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	#is_superuser = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
	#is_staff = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
	#is_active = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
	#date_joined = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email')


class BlogPasswordChangeForm(PasswordChangeForm):
	old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Enter your old password'}))
	new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password', 'placeholder':'Enter your new password'}))
	new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password', 'placeholder':'Reconfirm your new password'}))
	
	class Meta:
		model = User
		fields = ('old_password', 'new_password1', 'new_password2')

class BlogUserProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('user', 'pic', 'website_url', 'twitter_url', 'facebook_url', 'instagram_url', 'body')

		widgets = {
			'user': forms.TextInput(attrs={'class':'form-control', 'value': '', 'id': 'userid', 'type':'hidden'}),
			'website_url': forms.TextInput(attrs={'class':'form-control'}),
			'facebook_url': forms.TextInput(attrs={'class':'form-control'}),
			'twitter_url': forms.TextInput(attrs={'class':'form-control'}),
			'instagram_url': forms.TextInput(attrs={'class':'form-control'}),
		}

class BlogUserCreateProfilePageForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('user', 'pic', 'website_url', 'twitter_url', 'facebook_url', 'instagram_url', 'body')


		widgets = {
			'user': forms.TextInput(attrs={'class':'form-control', 'value': '', 'id': 'userid', 'type':'hidden'}),
			'website_url': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your Website Url'}),
			'facebook_url': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your Facebook Url'}),
			'twitter_url': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your Twitter Url'}),
			'instagram_url': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your Instagram Url'}),
		}
