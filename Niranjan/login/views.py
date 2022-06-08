from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse(HTML_STRING)
HTML_STRING="<h1>Niranjan</h1>"
