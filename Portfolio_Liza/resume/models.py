"""Module providingFunction printing python version."""
from django.db import models
from django.core.validators import (MaxValueValidator,
                                    MinValueValidator,
                                    EmailValidator,
                                    URLValidator,)

# Create your models here.


class Person(models.Model):
    """Class representing a person"""
    first_name = models.TextField(max_length=20)
    last_name = models.TextField(max_length=30)


class PersonalInfo(models.Model):
    """Class representing a personal_info"""
    birth_date = models.DateField()
    email = models.EmailField(validators=[EmailValidator])
    phone = models.CharField(max_length=20)
    address = models.TextField(max_length=60)
    created_on = models.DateTimeField(auto_now=True)


class SocialInfo(models.Model):
    """Class representing a social"""
    link = models.URLField(validators=[URLValidator])
    created_on = models.DateTimeField(auto_now=True)


class MyExpertise(models.Model):
    """Class representing a my_expertise"""
    job_title = models.TextField(max_length=30)
    job_company = models.TextField(max_length=30)
    created_on = models.DateTimeField(auto_now=True)


class WhoAmI(models.Model):
    """Class representing a who_am_i"""
    summary_text = models.TextField(max_length=150)
    created_on = models.DateTimeField(auto_now=True)


class Expertise(models.Model):
    """Class representing a expertise"""
    job_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    job_title = models.TextField(max_length=30)
    job_description = models.TextField(max_length=150, blank=True, null=True)
    created_on = models.DateTimeField(auto_now=True)


class Education(models.Model):
    """Class representing a education"""
    date = models.DateField()
    degree = models.TextField(max_length=30)
    description = models.TextField(max_length=150, blank=True, null=True)
    created_on = models.DateTimeField(auto_now=True)


class Skill(models.Model):
    """Class representing a skill"""
    name = models.TextField(max_length=30)
    value = models.PositiveIntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(1)], default=1)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} skill value is {self.value}"


class Languages(models.Model):
    """Class representing a language"""
    name = models.TextField(max_length=20)
    value = models.PositiveIntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(1)], default=1)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} languages value is {self.value}"


class DarkText(models.Model):
    """Class representing a dark_text"""
    value = models.PositiveIntegerField()
    name = models.TextField(max_length=30)
    created_on = models.DateTimeField(auto_now=True)
