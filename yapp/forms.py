from django import forms
from .models import Post, Comment, FeedBackModel, FeedBackReply, Note
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('user', 'title', 'image', 'body', 'second_image')

        widgets = {
            #'user': forms.TextInput(attrs={'class':'form-control'}),
            'user': forms.TextInput(attrs={'class':'form-control', 'value': '', 'id': 'userid', 'type': 'hidden'}),
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the title of Your Post'}),
            #'date': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Date in yyyy-mm-dd format'}),
            'body': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter the description'}),
        }


'''
class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
'''

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('user', 'body')

        widgets = {
            'user': forms.TextInput(attrs={'class':'form-control', 'value': '', 'id': 'userid', 'type':'hidden' }),
            #'post': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the title of the Form'}),
            #'date': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Date in yyyy-mm-dd format'}),
            'body': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter the description'}),
            
        }

class FeedbackCreateForm(forms.ModelForm):
    class Meta:
        model = FeedBackModel
        fields = ('user', 'title', 'complaint')

        widgets = {
            'user': forms.TextInput(attrs={'class':'form-control', 'value': '', 'id': 'userid', 'type':'hidden' }),
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your Title'}),
            'complaint': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter Your Feedback'}),
        }

class ReplyForm(forms.ModelForm):
    class Meta:
        model = FeedBackReply
        fields = ('user', 'complaint')

        widgets = {
            'user': forms.TextInput(attrs={'class':'form-control', 'value': '', 'id': 'userid', 'type':'hidden' }),
            #'post': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the title of the Form'}),
            #'date': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Date in yyyy-mm-dd format'}),
            'complaint': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter the description'}),
            
        }

class NoteCreate(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('user', 'title', 'body')

        widgets = {
            'user': forms.TextInput(attrs={'class':'form-control', 'value': '', 'id': 'userid', 'type':'hidden' }),
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter The Title' }),
            'body': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter the description'}),  
        }