from django.shortcuts import render
from register_app import forms

# Create your views here.


def register_user(request):

    registered = False

    if request.method == 'POST':
        user_form = forms.UserCreationForm(data=request.POST)

        if user_form.is_valid():

            user_data = user_form.save(commit=False)
            user_data.set_password(password=user_data.password)
            user_data.save()

            registered = True

    user_form = forms.UserCreationForm()
    context_dict = {registered: 'registered',
                    user_form: 'user_form'}
    return render(request, template_name='register_app/register_app.html', context=context_dict)

