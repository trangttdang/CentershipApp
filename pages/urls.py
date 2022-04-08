from django.urls import path
from . import views
from django.views.generic import TemplateView  # new


urlpatterns = [
   path('', views.index, name='site'),
  
]

# new
urlpatterns += [
    path(r"templates.html", TemplateView.as_view(template_name="pages/templates.html", content_type='text/plain')),
]


