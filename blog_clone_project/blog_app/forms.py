from django import forms
from blog_app import models


class UserPostForm(forms.ModelForm):

    class Meta():
        model = models.UserPostModel

        fields = ['post_author', 'post_title', 'post_text']

        widgets = {
            'post_author': forms.Select(attrs={'class': 'btn btn-outline-dark dropdown-toggle form-control'}),
            'post_title': forms.TextInput(attrs={'class': 'form-control'}),
            'post_text': forms.Textarea(attrs={'class': 'form-control'}),
        }


class UserCommentForm(forms.ModelForm):

    class Meta():
        model = models.UserCommentModel

        fields = ['comment_author', 'comment_text']

        widgets = {
            'comment_author': forms.TextInput(attrs={'class': 'form-control'}),
            'comment_text': forms.Textarea(attrs={'class': 'form-control'}),
        }
