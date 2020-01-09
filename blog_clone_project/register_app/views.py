from django.shortcuts import render
from register_app import forms

from register_app import models

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate

# Create your views here.


def register_user(request):

    registered = False

    if request.method == 'POST':
        user_form = forms.UserCreationForm(data=request.POST)

        if user_form.is_valid():

            user_data = user_form.save(commit=False)
            user_data.set_password(user_data.password)
            user_data.save()

            registered = True

            if registered:
                return redirect('login_app:login_user')

    user_form = forms.UserCreationForm()
    context_dict = {'registered': registered,
                    'user_form': user_form}
    return render(request, template_name='register_app/register_app.html', context={'registered': registered,
                                                                                    'user_form': user_form})

