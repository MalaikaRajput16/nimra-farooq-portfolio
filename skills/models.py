

# Create your models here.
from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField(help_text="Percentage 1-100")

    def __str__(self):
        return self.name