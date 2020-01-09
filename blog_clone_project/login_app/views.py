from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.


def login_user(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        login_user_data = authenticate(request, username=username, password=password)

        if login_user_data:
            login(request, login_user_data)
            return HttpResponseRedirect(reverse('blog_app:post_list'))
        else:
            return HttpResponse('Invalid personal data supplied')

    return render(request, template_name='login_app/login_app.html')


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index_view'))

