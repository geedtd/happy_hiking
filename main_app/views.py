from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Trail
from .forms import ReviewForm

# Create your views here.

# Define the home view
class Home(LoginView):
  template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

def trails_index(request):
    trails = Trail.objects.all()
    return render(request, 'trails/index.html', {'trails': trails})

def trails_detail(request, trail_id):
    trail = Trail.objects.get(id=trail_id)
    review_form = ReviewForm()
    return render(request, 'trails/detail.html', {
        'trail': trail, 'review_form': review_form
        })

class TrailCreate(CreateView):
    model = Trail
    fields = ['name','length','description']

        # This inherited method is called when a
    # valid cat form is being submitted
    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the cat
        # Let the CreateView do its job as usual
        return super().form_valid(form)
    
class TrailUpdate(UpdateView):
    model = Trail
    fields = ['length', 'description']

class TrailDelete(DeleteView):
    model = Trail
    success_url = '/trails/'

