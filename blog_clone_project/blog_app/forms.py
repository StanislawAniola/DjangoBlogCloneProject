from django import forms
from blog_app import models


class UserPostForm(forms.ModelForm):

    class Meta():
        model = models.UserPostModel

        fields = ['post_author', 'post_title', 'post_text']

        widgets = {
            'post_title': forms.TextInput(attrs={'class': 'group-control'}),
            'post_text': forms.Textarea(attrs={'class': 'group-control'}),
        }


class UserCommentForm(forms.ModelForm):

    class Meta():
        model = models.UserCommentModel

        fields = ['comment_author', 'comment_text']

        widgets = {
            'comment_author': forms.TextInput(attrs={'class': 'group-control'}),
            'comment_text': forms.Textarea(attrs={'class': 'group-control'}),
        }
