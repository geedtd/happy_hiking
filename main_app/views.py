from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import ReviewForm
from .models import Trail, Review, Photo
import uuid
import boto3

# Create your views here.
S3_BASE_URL = 'https://s3.us-west-1.amazonaws.com/'
BUCKET = 'happyhiking'
# Define the home view
def add_photo(request, cat_id):
  # photo-file will be the "name" attribute on the <input type="file">
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
  return redirect('trails_detail', trail_id=trail_id)

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

def add_review(request, trail_id):
    form = ReviewForm(request.POST)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.trail_id = trail_id
        new_review.save()
    return redirect('trails_detail', trail_id=trail_id)

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

