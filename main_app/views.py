from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from .forms import ReviewForm
from .models import Trail, Review, Photo
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3

# Create your views here.
S3_BASE_URL = 'https://s3.us-west-1.amazonaws.com/'
BUCKET = 'happyhiking'
# Define the home view
@login_required
def add_photo(request, review_id):
  # photo-file will be the "name" attribute on the <input type="file">
  trails = Trail.objects.all()
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    # need a unique "key" for S3 / needs image file extension too
		# uuid.uuid4().hex generates a random hexadecimal Universally Unique Identifier
    # Add on the file extension using photo_file.name[photo_file.name.rfind('.'):]
    key = uuid.uuid4().hex + photo_file.name[photo_file.name.rfind('.'):]
    # just in case something goes wrong
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      # build the full url string
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      
      photo = Photo(url=url, review_id=review_id)
      # Remove old photo if it exists
      review_photo = Photo.objects.filter(review_id=review_id)
      if review_photo.first():
        review_photo.first().delete()
      photo.save()
    except Exception as err:
      print('An error occurred uploading file to S3: %s' % err)
  return render(request, 'trails/index.html', {'trails': trails})

class Home(LoginView):
  template_name = 'home.html'


def about(request):
    return render(request, 'about.html')

@login_required
def trails_index(request):
    trails = Trail.objects.all()
    return render(request, 'trails/index.html', {'trails': trails})

@login_required
def trails_detail(request, trail_id):
    trail = Trail.objects.get(id=trail_id)
    review_form = ReviewForm()
    return render(request, 'trails/detail.html', {
        'trail': trail, 'review_form': review_form
        })

@login_required
def add_review(request, trail_id):
    form = ReviewForm(request.POST)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.trail_id = trail_id
        new_review.save()
    return redirect('trails_detail', trail_id=trail_id)

class TrailCreate(LoginRequiredMixin, CreateView):
    model = Trail
    fields = ['name','length','description']

  
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class TrailUpdate(LoginRequiredMixin, UpdateView):
    model = Trail
    fields = ['length', 'description']

class TrailDelete(LoginRequiredMixin, DeleteView):
    model = Trail
    success_url = '/trails/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in
      login(request, user)
      return redirect('trails_index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)