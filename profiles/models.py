from operator import mod
from django.db import models
# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=80)
    username = models.CharField(max_length=80)
    email = models.CharField(max_length=80)
    password1 = models.CharField(max_length=80)
    password2 = models.CharField(max_length=80)

# class Mentee(User):
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

# class Mentor(User):
#     # mentor id pk

#     # methods:
#     def limitMentee():
#         # add or delete a goal
        
#     def menteeList():
#         # if __ = ___ match

#     def match():
#         # launches survey?

