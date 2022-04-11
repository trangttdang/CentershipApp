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