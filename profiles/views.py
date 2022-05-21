from multiprocessing.dummy import current_process
import re
from turtle import update
from django.shortcuts import  render, redirect
from .forms import MenteeProfileForm, MentorProfileForm, NewUserForm, MatchForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from profiles.models import User
from .filters import InterestFilter
from .models import *


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("profiles:login")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, "You are now logged in as {username}.")
				if user.user_type == 'mentor':
					return redirect("profiles:mentor_profile")
				else:
					return redirect("profiles:mentee_profile")	
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

# for the mentor profile page
def mentor_profile_request(request):
	form = MentorProfileForm()
	if request.method == "POST":
		form = MentorProfileForm(request.POST)
		if form.is_valid():
			obj = form.save(commit=False) # Return an object without saving to the DB
			obj.user = User.objects.get(pk = request.user.id) # Add an author field which will contain current user's id
			obj.save() # Save the final "real form" to the DB
		else:
			print("ERROR : Form is invalid")
		redirect("profiles:mentor_profile")
	return render (request=request, template_name="mentor_profile.html", context={"mentor_profile_form":form})


# for the mentee profile page
def mentee_profile_request(request):
	form = MenteeProfileForm()

	if request.method == "POST":
		form = MenteeProfileForm(request.POST)
		if form.is_valid():
			current_user = request.user.id
			obj = form.save(commit=False) # Return an object without saving to the DB
			obj.user = User.objects.get(pk = current_user) # Add an author field which will contain current user's id
			obj.save() # Save the final "real form" to the DB
			# instance = Mentee.objects.values('goals')[5]
			# goals = instance['goals']
			current_mentee = Mentee.objects.get(user=current_user)
			goals = current_mentee.goals
			if not Goal.objects.filter(mentee = current_mentee).exists():
				for goal in goals:
					Goal.objects.create(mentee = current_mentee, name= goal, achieved = False)
			else:
				current_goal = Goal.objects.filter(mentee = current_mentee).first()
				current_goal_id = current_goal.id
				for goal in goals:
					Goal.objects.filter(mentee = current_mentee, id = current_goal_id).update(name= goal)
					current_goal_id += 1
		else:
			print("ERROR : Form is invalid")
		redirect("profiles:mentee_profile")
	return render (request=request, template_name="mentee_profile.html", context={"mentee_profile_form":form})


# def mentee_profile(request):
# 	if request.method == "GET":
# 		return render(request=request, template_name="mentee_profile.html")
	

# def mentor_profile(request):
# 	if request.method == "GET":
# 		return render(request=request, template_name="mentor_profile.html")

# for marketplace page where the filters can be applied
def marketplace_request(request):
	mentors = Mentor.objects.filter(mentee_limit__gte=1)
	interest_filter = InterestFilter(request.GET, queryset=mentors)
	return render (request=request, template_name="marketplace.html", context={"interest_filter":interest_filter})

def matching_request(request):
	mentor_id = int(request.GET['mentorID'])
	limit = int(request.GET['menteeLimit'])
	if limit > 0:
		Mentee.objects.filter(user = request.user.id).update(mentor = mentor_id)
		limit-=1
		Mentor.objects.filter(user = mentor_id).update(mentee_limit = limit)
		
	return render(request=request, template_name="meet_mentor.html")

def goal_tracker_request(request):
	# goal_list = Goal.objects.filter(mentee= request.user.id).values_list('name')
	goal_list = Goal.objects.filter(mentee= request.user.id)
	if request.method == "POST":
		id_list = request.POST.getlist('boxes')
		print(id_list)
		# Update the database
		goal_list.update(achieved = False)
		for id in id_list:
			Goal.objects.filter(pk = int(id.rstrip(','))).update(achieved = True)
		messages.success(request, 'Congratulations! You achieved all goals!')
		return redirect('profiles:goal_tracker')
	else:
		return render(request=request, template_name="goal_tracker.html",context={"goals": goal_list})

