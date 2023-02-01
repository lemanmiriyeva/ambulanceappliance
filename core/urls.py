from django.urls import path
from .models import *
from .views import *

urlpatterns=[
    # path('home/',home,name='home'),
    path('home/',HomeView.as_view(),name='home'),
    # path('about/',about,name='about'),
    path('about/',AboutView.as_view(),name='about'),
    path('contact/',contact,name='contact')
]