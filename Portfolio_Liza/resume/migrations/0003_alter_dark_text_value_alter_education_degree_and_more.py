# Generated by Django 4.2.2 on 2023-07-10 14:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_dark_text_education_expertise_languages_my_expertise_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dark_text',
            name='value',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='education',
            name='degree',
            field=models.TextField(max_length=30),
        ),
        migrations.AlterField(
            model_name='education',
            name='description',
            field=models.TextField(max_length=150),
        ),
        migrations.AlterField(
            model_name='expertise',
            name='job_description',
            field=models.TextField(max_length=150),
        ),
        migrations.AlterField(
            model_name='expertise',
            name='job_title',
            field=models.TextField(max_length=30),
        ),
        migrations.AlterField(
            model_name='languages',
            name='name',
            field=models.TextField(max_length=20),
        ),
        migrations.AlterField(
            model_name='languages',
            name='value',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='my_expertise',
            name='job_company',
            field=models.TextField(max_length=30),
        ),
        migrations.AlterField(
            model_name='my_expertise',
            name='job_title',
            field=models.TextField(max_length=30),
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.TextField(max_length=10),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.TextField(max_length=20),
        ),
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.TextField(max_length=30),
        ),
        migrations.AlterField(
            model_name='skill',
            name='value',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='who_am_i',
            name='summary_text',
            field=models.TextField(max_length=150),
        ),
    ]
