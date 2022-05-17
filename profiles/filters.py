import django_filters
from .models import *

class InterestFilter(django_filters.FilterSet):
    class Meta:
        model = Mentor
        fields = ('personal_interests', 'professional_interests') 
