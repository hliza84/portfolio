"""Module providingFunction printing python version."""
from django.shortcuts import render
from .models import (Person,
                     PersonalInfo,
                     MyExpertise,
                     WhoAmI,
                     Expertise,
                     Education,
                     Skill,
                     Languages,
                     DarkText,
                     SocialInfo)

# Create your views here.


def home(request):
    """Function home."""
    person = Person.objects.all()
    personal_info = PersonalInfo.objects.all()
    my_expertise = MyExpertise.objects.all()
    who_am_i = WhoAmI.objects.all()
    expertise = Expertise.objects.all()
    education = Education.objects.all()
    skill = Skill.objects.all()
    language = Languages.objects.all()
    dark_text = DarkText.objects.all()
    social = SocialInfo.objects.all()
    data = {
        "logo": "L|H",
        "person": person,
        "personal_info": personal_info,
        "my_expertise": my_expertise,
        "Who_am_I": who_am_i,
        "Expertise": expertise,
        "Education": education,
        "Skills": skill,
        "Languages": language,
        "Dark_text": dark_text,
        "social": social
    }

    return render(request, "index.html", context=data)
