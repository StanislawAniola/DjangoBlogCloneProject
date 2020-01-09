from django import forms
from django.contrib.auth.forms import User


class UserCreationForm(forms.ModelForm):

    class Meta:

        model = User
        fields = ['username', 'email', 'password']

        help_texts = {'username': None,}

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
