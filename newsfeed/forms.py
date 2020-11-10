from django import forms
from .models import BlogComment


class NewCommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ['content']
