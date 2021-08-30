from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Trail(models.Model):
    name = models.CharField(max_length=75)
    description = models.TextField(max_length=400)
    length = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("trails_detail", kwargs={"trail_id": self.id})

EXPERIENCE = (
    ('B', 'Beginner'),
    ('I', 'Intermidiate'),
    ('E', 'Experience'),
)

class Review(models.Model):
    date = models.DateField('Hike Date')
    text = models.TextField(max_length=500)
    difficulty = models.CharField(
        max_length=1,
        choices= EXPERIENCE,
        default=EXPERIENCE[0][0]
    )

    hike = models.ForeignKey(Trail, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_difficulty_display()} on {self.date}"