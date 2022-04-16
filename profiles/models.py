from operator import mod
from django.db import models
# from django.contrib.auth.models import get_user_model
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    is_mentor = models.BooleanField(default=False)
    is_mentee = models.BooleanField(default=False)
    name = models.CharField(max_length=80)
    username = models.CharField(max_length=80, unique= True)
    email = models.CharField(max_length=80)
    password1 = models.CharField(max_length=80)
    password2 = models.CharField(max_length=80)

class Mentor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True )


class Mentee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True )
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)

# class Persona(models.Model):
#     # registration = get_user_model()
#     name = models.CharField(max_length=80)
#     username = models.CharField(max_length=80)
#     email = models.CharField(max_length=80)
#     password1 = models.CharField(max_length=80)
#     password2 = models.CharField(max_length=80)

# class Mentee(Persona):
#     # goalList arraylist
#     # mentee id pk
#     # mentor id fk

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

