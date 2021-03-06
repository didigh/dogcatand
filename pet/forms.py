from django import forms
from .models import Blog,Comment,Re

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields=['contents']

class ReForm(forms.ModelForm):
    class Meta:
        model = Re
        fields=['contents']