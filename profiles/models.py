from operator import mod
from django.db import models
# from django.contrib.auth.models import get_user_model
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
# Create your models here.


class User(AbstractUser):
    is_mentor = models.BooleanField(default=False)
    is_mentee = models.BooleanField(default=False)
    age = models.IntegerField(null=True)
    professional_interests = models.TextField(null=True)
    personal_interests = models.TextField(null=True)
    username = models.CharField(max_length=80, unique= True)
    email = models.CharField(max_length=80)
    password1 = models.CharField(max_length=80)
    password2 = models.CharField(max_length=80)

class Mentor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True )
    education = models.CharField(max_length=80, null=True)
    professional_experience = models.TextField(null=True)
    mentee_limit = models.IntegerField(null=True)
    mentorship_duration = models.DurationField(null=True)
    

class Mentee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True )
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE, null= True, default=None)
    goals = ArrayField(
        models.TextField(),
        null=True
    )
    # add_goal...would this be defined here or in the view? i feel like it should be defined in the view beacuse how would a function show up on the db? 
    # delete_goal
    # find_mentor



# class Mentee(Persona):
#     # goalList arraylist
#     # methods:
#     def goal():
#         # add or delete a goal
        
#     def match():
#         # if __ = ___ match

#     def findmentor():
#         # launches survey?

# class Mentor(Persona):
#     # mentor id pk

#     # methods:
#     def limitMentee():
#         # add or delete a goal
        
#     def menteeList():
#         # if __ = ___ match

#     def match():
#         # launches survey?

