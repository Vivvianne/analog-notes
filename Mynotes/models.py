from django.db import models
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    organization = models.CharField(max_length=100)
    agenda = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    attendance = models.TextField()
    content =  models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    
    @classmethod
    def search_by_agenda(cls,search_term):
        Post = cls.objects.filter(agenda__icontains=search_term)
        return Post
    
    def __str__(self):
        return self.organization
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
    


