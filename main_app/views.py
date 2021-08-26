from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .models import Trail

# Create your views here.

# Define the home view
class Home(LoginView):
  template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

# class Trail:
#     def __init__(self, name, description ):
#         self.name = name
#         self.description = description

# trails = [
#     Trail('Malibu Creek', 'Beautiful in Malibu'),
#     Trail('Stargazer Trail', 'Hike with beautiful views of the Pacific on the border of San Pedro and PV')
# ]

def trails_index(request):
    trails = Trail.objects.all()
    return render(request, 'trails/index.html', {'trails': trails})

def trails_detail(request, trail_id):
    trail = Trail.objects.get(id=trail_id)
    return render(request, 'trails/detail.html', {'trail': trail})