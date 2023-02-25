from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

class RegisterView(CreateView):
    form_class=RegisterForm
    template_name="register.html"
    success_url=reverse_lazy("login")

    def form_valid(self,form):
        result=super().form_valid(form)
        return result

class LoginView(LoginView):
    form_class=LoginForm
    template_name="login.html"
    success_url=reverse_lazy("home")
    
    def get_success_url(self):
        return reverse_lazy("home")


@login_required
def logout(request):
    logout(request)
    return redirect(reverse_lazy("login"))


def social_login(request):
    
    return render(request,'social_login.html')