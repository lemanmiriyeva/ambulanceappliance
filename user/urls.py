from django.urls import path
from .views import *


urlpatterns=[
    path("login/",LoginView.as_view(),name="login"),
    # path("register/",RegisterView.as_view(),name="register"),
    path('register/',register,name="register"),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',  
        activate, name='activate'),  
    path("logout/",logout,name="logout"),
  
]