from operator import mod
from unicodedata import name
from django.db import models
# from django.contrib.auth.models import get_user_model
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django import forms
# Create your models here.


class User(AbstractUser):
    username = models.CharField(max_length=80, unique= True)
    email = models.CharField(max_length=80)
    password1 = models.CharField(max_length=80)
    password2 = models.CharField(max_length=80)
    USER_TYPE = (
        ('mentee','Mentee'),
        ('mentor','Mentor'),
    )
    user_type = models.CharField(max_length=80, null=True, choices=USER_TYPE)

class Mentor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True )
    education = models.CharField(max_length=80, null=True)
    professional_experience = models.TextField(null=True)
    mentee_limit = models.IntegerField(null=True)
    mentorship_duration = models.DurationField(null=True)

    PROFESSIONAL_INTERESTS = (
        ('Technical Interviews','Technical Interviews'),
        ('Web Development','Wed Development'),
        ('App Development','App Development'),
        ('Math','Math'),
        ('Computer Science','Computer Science'),
        ('Science','Science'),
        ('Engineering','Engineering'),
    )
    PERSONAL_INTERESTS = (
        ('Painting','Painting'),
        ('Music','Music'),
        ('Photogrpahy','Photography'),
        ('Reading','Reading'),
        ('Sports','Sports'),
        ('Cooking','Cooking'),
    )

    professional_interests = models.CharField(max_length=80, null=True, choices=PROFESSIONAL_INTERESTS)
    personal_interests = models.CharField(max_length=80, null=True, choices=PERSONAL_INTERESTS)

    

class Mentee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True )
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE, null= True, default=None)
    goals = ArrayField(
        models.TextField(),
        null=True
    )

    PROFESSIONAL_INTERESTS = (
        ('Technical Interviews','Technical Interviews'),
        ('Web Development','Wed Development'),
        ('App Development','App Development'),
        ('Math','Math'),
        ('Computer Science','Computer Science'),
        ('Science','Science'),
        ('Engineering','Engineering'),
    )
    PERSONAL_INTERESTS = (
        ('Painting','Painting'),
        ('Music','Music'),
        ('Photogrpahy','Photography'),
        ('Reading','Reading'),
        ('Sports','Sports'),
        ('Cooking','Cooking'),
    )

    professional_interests = models.CharField(max_length=80, null=True, choices=PROFESSIONAL_INTERESTS)
    personal_interests = models.CharField(max_length=80, null=True, choices=PERSONAL_INTERESTS)
    #Create goals
    def save(self,*args,**kwargs):
        created = not self.pk
        super(Mentee,self).save(*args,**kwargs)
        if created:
            Goal.objects.create(mentee=1,name= Mentee.goals, achieved = False)
    
class Goal(models.Model):
    mentee = models.ForeignKey(Mentee, on_delete=models.CASCADE, null= True, default=None)
    name = models.CharField('Goal Name', max_length=80)
    achieved = models.BooleanField('Achieved', default=False)

