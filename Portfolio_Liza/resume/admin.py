"""Module providingFunction printing python version."""
from django.contrib import admin
from .models import (Person, PersonalInfo, MyExpertise,
                     WhoAmI, Expertise, Education,
                     Skill, Languages,
                     DarkText, SocialInfo)

# Register your models here.
admin.site.register(Person)
admin.site.register(PersonalInfo)
admin.site.register(MyExpertise)
admin.site.register(WhoAmI)
admin.site.register(Expertise)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Languages)
admin.site.register(DarkText)
admin.site.register(SocialInfo)
