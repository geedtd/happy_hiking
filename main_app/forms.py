from django.db.models.base import Model
from django.forms import ModelForm
from .models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review 
        fields = ['date','text','difficulty',]