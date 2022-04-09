from django.urls import path
from . import views
from django.views.generic import TemplateView  # new


urlpatterns = [
   path('', views.index, name='site'),
   path('about/', views.index2, name='about'),
   path('mentors/',views.index3, name= 'mentors'),
   path('mentees/', views.index4, name= 'mentees')

]
# new
urlpatterns += [
    path(r"templates.html", TemplateView.as_view(template_name="pages/templates.html", content_type='text/plain')),
]


