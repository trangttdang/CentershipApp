from django.urls import path
from . import views
from django.views.generic import TemplateView  # new

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
   path('', views.site, name='site'),
   path('about/', views.about, name='about'),
   path('mentors/',views.mentors, name= 'mentors'),
   path('mentees/', views.mentees, name= 'mentees'),
   path('login/', views.login, name='login'),
   path('register/', views.signUp, name='signUp')

]
# new
urlpatterns += [
    path(r"templates.html", TemplateView.as_view(template_name="pages/templates.html", content_type='text/plain')),
    path(r"templates.html", TemplateView.as_view(template_name="profiles/templates.html", content_type='text/plain')),
]
urlpatterns += staticfiles_urlpatterns()