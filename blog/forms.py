from django.forms import ModelForm, widgets
from django import forms
from .models import Blog, Comment


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        exclude = ['created_at','updated_at','created_by']
        widgets = {
            'title':  forms.TextInput(attrs= {'class': 'form-control'}),
            'content': forms.Textarea(attrs= {'class': 'form-control', 'style':'resize:none;'}),
            'image': forms.ClearableFileInput(attrs={'class':'form-control'})
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['id','content']
        widgets = {
            'content': forms.Textarea(attrs= {'class': 'form-control', 'style':'resize:none;'}),
        }