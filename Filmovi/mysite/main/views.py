from django.shortcuts import render
from django.http import HttpResponse

## Create your views here.
def homepage(request):
    return HttpResponse('Welcome to homepage')
    # primjetiti korištenje HTML-a