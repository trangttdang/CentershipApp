from django.shortcuts import render

# Create your views here.
def index(request):
   return render(request, 'pages/site.html')

def index2(request):
   return render(request, 'pages/about.html')

def index3(request):
   return render(request,'pages/mentors.html')

def index4(request):
   return render(request,'pages/mentees.html')