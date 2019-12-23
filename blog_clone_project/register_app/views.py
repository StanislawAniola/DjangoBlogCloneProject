from django.shortcuts import render
from register_app import forms

# Create your views here.


def register_user(request):
    registered = False

    if request.method == 'POST':
        user_form = forms.UserCreationForm(data=request.POST)

        if user_form.is_valid():
            
