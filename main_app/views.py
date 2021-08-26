from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView

# Create your views here.

# Define the home view
class Home(LoginView):
  template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

class Trail:
    def __init__(self, name, description ):
        self.name = name
        self.description = description

trails = [
    Trail('Malibu Creek', 'Beautiful in Malibu'),
    Trail('Stargazer Trail', 'Hike with beautiful views of the Pacific on the border of San Pedro and PV')
]

def trails_index(request):
    return render(request, 'trails/index.html', {'trails': trails})