from django.shortcuts import  render, redirect
from .forms import MenteeProfileForm, MentorProfileForm, NewUserForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from profiles.models import User

# for register page...so only needs to get?
def register_request(request):
	# if request.method == "GET":
	# 	return render(request=request, template_name="register.html")
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

# for the mentor signup page
# def mentor_request(request):
# 	if request.method == "POST":
# 		form = NewMentorForm(request.POST)
# 		if form.is_valid():
# 			user = form.save()
# 			login(request, user)
# 			messages.success(request, "Registration successful." )
# 			return redirect("profiles:login")
# 		messages.error(request, "Unsuccessful registration. Invalid information.")
# 	form = NewMentorForm()
# 	return render (request=request, template_name="mentor_signup.html", context={"register_form":form})

# for the mentee signup page
# def mentee_request(request):
# 	if request.method == "POST":
# 		form = NewMenteeForm(request.POST)
# 		if form.is_valid():
# 			user = form.save()
# 			login(request, user)
# 			messages.success(request, "Registration successful." )
# 			return redirect("profiles:login")
# 		messages.error(request, "Unsuccessful registration. Invalid information.")
# 	form = NewMenteeForm()
# 	return render (request=request, template_name="mentee_signup.html", context={"register_form":form})


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
		redirect("profiles:mentor_landing")
	return render (request=request, template_name="update_mentor_profile.html", context={"mentor_profile_form":form})


# for the mentee profile page
def mentee_profile_request(request):
	form = MenteeProfileForm()
	if request.method == "POST":
		form = MenteeProfileForm(request.POST)
		if form.is_valid():
			obj = form.save(commit=False) # Return an object without saving to the DB
			obj.user = User.objects.get(pk = request.user.id) # Add an author field which will contain current user's id
			obj.save() # Save the final "real form" to the DB
		else:
			print("ERROR : Form is invalid")
		redirect("profiles:mentee_landing")
	return render (request=request, template_name="update_mentee_profile.html", context={"mentee_profile_form":form})

# # for the mentor landing page; this will also contain GET 
# def mentor_profile_request(request):

# # for the mentee landing page; this will also contain GET 
# def mentee_profile_request(request):

def mentee_profile(request):
	if request.method == "GET":
		return render(request=request, template_name="mentee_profile.html")

def mentor_profile(request):
	if request.method == "GET":
		return render(request=request, template_name="mentor_profile.html")
