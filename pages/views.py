from django.shortcuts import render

# Create your views here.
def site(request):
   return render(request, 'pages/site.html')

def about(request):
   return render(request, 'pages/about.html')

def mentors(request):
   return render(request,'pages/mentors.html')

def mentees(request):
   return render(request,'pages/mentees.html')

def login(request):
   return render(request, 'pages/login.html')

def signUp(request):
   return render(request, 'pages/register.html')
