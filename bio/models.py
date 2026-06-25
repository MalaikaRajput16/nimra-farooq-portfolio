from django.db import models

# Create your models here.
from django.db import models

class Bio(models.Model):

    name = models.CharField(max_length=100, default="Nimra Farooq")
    
    # REPLACE with your title (e.g., "Full Stack Developer" or "BSCS Student")
    job_title = models.CharField(max_length=100, default="Web Developer Student")
    
    # Write a short professional description about yourself
    description = models.TextField(default="Hi, I'm Nimra Farooq, a Computer Science Student, passionate about building clean, efficient code and solving real problems with technology. I enjoy web development, algorithms, and learning new frameworks. Currently explooring JavaScript, React, Python and working on projects that improve user experience. Let's build something great together. I don't chase perfect code. I chase consistent progress. Every line I write today makes tomorrow's version of me better developer.")
    
    # This field will store your profile picture 
    profile_picture = models.ImageField(upload_to='profile/', blank=True, null=True)

    def __str__(self):
        return self.name