
from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

from profiles.models import User, Mentee, Mentor

# Create your forms here

class NewMenteeForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta(UserCreationForm.Meta):
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewMenteeForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.is_mentee = True
		if commit:
			user.save()
		return user

class NewMentorForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta(UserCreationForm.Meta):
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewMentorForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.is_mentor = True
		if commit:
			user.save()
		return user
