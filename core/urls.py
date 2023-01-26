from django.urls import path
from .models import *
from .views import *

urlpatterns=[
    path('home/',home,name='home'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact')
]