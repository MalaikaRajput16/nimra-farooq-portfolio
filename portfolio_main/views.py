from django.shortcuts import render
from bio.models import Bio
from education.models import Education
from skills.models import Skill
from experience.models import Experience

def home(request):
    context = {
        'bio': Bio.objects.first(),
        'education_list': Education.objects.all(),
        'skills_list': Skill.objects.all(),
        'experience_list': Experience.objects.all(),
    }
    return render(request, 'index.html', context)
 