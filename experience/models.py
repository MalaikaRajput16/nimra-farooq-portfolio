from django.db import models

# Create your models here.
from django.db import models

class Experience(models.Model):
    title = models.CharField(max_length=200) 
    # Project/Job Title
    organization = models.CharField(max_length=200)
     # Company or "Personal Project"
    description = models.TextField() 
    # What did you do?

    def __str__(self):
        return self.title