from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Define the home view
def home(request):
  return HttpResponse('<h1>Let\'s Get Hiking!</h1>')

