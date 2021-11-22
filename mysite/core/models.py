# import the standard Django Model
# from built-in library
from django.db import models
from django.contrib.auth.models import User  
from django.urls import reverse

# declare a new model with a name "GeeksModel"
class GeeksModel(models.Model):
 
    # fields of the model
    title = models.CharField(max_length = 200)
    description = models.TextField()
 
    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.title 

    def get_absolute_url(self):
        return reverse('home')    