from django.db import models 
from django.urls import reverse
from django.contrib.auth.models import User 

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default="The Orehbeinp dot com")
    test_tag = models.CharField(max_length=50, default="Test complete, without default, it fails")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    

    def __str__(self):
        return self.title + " | " + str(self.author)
    
    def get_absolute_url(self):
        #return reverse('post-detail', args=(str(self.id))) #This is the one thati do not understand right now, turns out without this it worked, but i thought that it did'nt create the page, it did
        return reverse('home') #It just takes you home

# Create your models here.
