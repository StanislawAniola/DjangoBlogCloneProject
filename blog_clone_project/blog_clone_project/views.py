from django.shortcuts import render


def index_view(request):
    return render(request, template_name='main/index_view.html')
