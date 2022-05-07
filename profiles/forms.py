
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from profiles.models import User, Mentee, Mentor

# Create your forms here


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta(UserCreationForm.Meta):
		model = User
		fields = ("username", "first_name", "last_name", "email", "password1", "password2","user_type")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.user_type = self.cleaned_data['user_type']
		if commit:
			user.save()
		return user

# class NewMenteeForm(UserCreationForm):
# 	email = forms.EmailField(required=True)

# 	class Meta(UserCreationForm.Meta):
# 		model = User
# 		fields = ("username", "first_name", "last_name", "age", "email", "password1", "password2", "professional_interests", "personal_interests")

# 	def save(self, commit=True):
# 		user = super(NewMenteeForm, self).save(commit=False)
# 		user.email = self.cleaned_data['email']
# 		user.is_mentee = True
# 		if commit:
# 			user.save()
# 		return user

# class NewMentorForm(UserCreationForm):
# 	email = forms.EmailField(required=True)

# 	class Meta(UserCreationForm.Meta):
# 		model = User
# 		fields = ("username", "first_name", "last_name", "age", "email", "password1", "password2","user_type")

# 	def save(self, commit=True):
# 		user = super(NewMentorForm, self).save(commit=False)
# 		user.email = self.cleaned_data['email']
# 		user.is_mentor = True
# 		if commit:
# 			user.save()
# 		return user

class MentorProfileForm(forms.ModelForm):
	class Meta:
		model = Mentor
		fields = ("education", "professional_experience", "mentee_limit", "mentorship_duration", "professional_interests","personal_interests")
	# class Meta2:
	# 	model = User
	# 	fields = ("professional_interests", "personal_interests")
	
	def save(self, commit=True):
		mentor = super(MentorProfileForm, self).save(commit=False)
		if commit:
			mentor.save()
		return mentor

class MenteeProfileForm(forms.ModelForm):
	class Meta:
		model = Mentee
		fields = ('goals',"professional_interests","personal_interests")
	# class Meta2:
	# 	model = User
	# 	fields = ("professional_interests", "personal_interests")
	
	def save(self, commit=True):
		mentee = super(MenteeProfileForm, self).save(commit=False)
		if commit:
			mentee.save()
		return mentee