from django.test import TestCase
from django.http import HttpResponse

# Create your tests here.


def post_test(request):
    return HttpResponse("Hello World")
