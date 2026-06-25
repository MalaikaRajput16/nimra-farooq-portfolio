from django.db import models

# Create your models here.
from django.db import models

class Education(models.Model):
    degree = models.CharField(max_length=200) # e.g., "BS Computer Science"
    institute = models.CharField(max_length=200) # e.g., " University of management and technology"
    year = models.CharField(max_length=50) # e.g., "2024 - 2028"

    def __str__(self):
        return self.degree