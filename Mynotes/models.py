from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    organization = models.CharField(max_length=100)
    agenda = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    attendance = models.TextField()
    content =  models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.organization


