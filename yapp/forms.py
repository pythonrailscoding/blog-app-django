from django import forms
from .models import Post
from django.forms import ModelForm

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('user', 'title', 'body')

        widgets = {
            #'user': forms.TextInput(attrs={'class':'form-control'}),
            'user': forms.Select(attrs={'class':'form-control'}),
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the title of the Form'}),
            #'date': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Date in yyyy-mm-dd format'}),
            'body': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter the description'}),
        }
