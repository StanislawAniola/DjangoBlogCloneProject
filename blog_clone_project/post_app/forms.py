from django import forms
from post_app import models


class PostForm(forms.ModelForm):

    class Meta():

        model = models.PostModel
        fields = ['post_author', 'post_text']

        widgets = {
            'post_author': forms.TextInput(attrs={'class': 'form-control'}),
            'post_text': forms.TextInput(attrs={'class': 'form-control'}),
        }
