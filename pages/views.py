from django.shortcuts import render
#<<<<<<< HEAD
from django.views.generic import TemplateView

# Create your views here.
def index(request):
   return render(request, 'pages/site.html', {})

#=======

# Create your views here.
#>>>>>>> bbdcc41e33e8a206af92713278f7fd54f2edef41
