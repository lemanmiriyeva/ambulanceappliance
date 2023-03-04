from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns=[
    path("login/",LoginView.as_view(),name="login"),
    # path("register/",RegisterView.as_view(),name="register"),
    path('register/',register,name="register"),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',  
        activate, name='activate'),  
    path("logout/",logout,name="logout"),
    path("password-reset/",ResetPasswordView.as_view(),name="password_reset"),
    path("password-reset-confirm/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"),name="password_reset_confirm"),
    path("password-reset-complete/",auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"),name="password_reset_complete"),
  
]