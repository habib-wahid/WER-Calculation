from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    given_text = models.TextField()
    automated_text = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
