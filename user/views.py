from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponse  
from django.shortcuts import render, redirect  
from django.contrib.auth import login, authenticate  
from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_bytes,force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.template.loader import render_to_string  
from .tokens import account_activation_token  
from django.contrib.auth.models import User  
from django.core.mail import EmailMessage  
from django.contrib.messages.views import SuccessMessageMixin

from django.contrib.auth.views import PasswordResetView  

# Create your views here.

# class RegisterView(CreateView):
#     form_class=RegisterForm
#     template_name="register.html"
#     success_url=reverse_lazy("login")

#     def form_valid(self,form):
#         result=super().form_valid(form)
#         return result

class ResetPasswordView(SuccessMessageMixin,PasswordResetView):
    template_name="password_reset.html"
    email_template_name="password_reset_email.html"
    subject_template_name="password_reset_subject.txt"
    success_message="We've emailed you instructions for setting your password," \
    "if an account exists with email you entered.You should receive thm shortly."\
    "if you dont receive an email"\
    "please make sure you've entered the address you registered with,and check your spam folder."
    success_url=reverse_lazy("home")
    



def register(request):  
    if request.method == 'POST':  
        form = RegisterForm(request.POST)  
        if form.is_valid():  
            # save form in the memory not in database  
            user = form.save(commit=False)  
            user.is_active = False  
            user.save()  
            # to get the domain of the current site  
            current_site = get_current_site(request)  
            mail_subject = 'Activation link has been sent to your email id'  
            message = render_to_string('acc_activate_email.html', {  
                'user': user,  
                'domain': current_site.domain,  
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
                'token':account_activation_token.make_token(user),  
            })  
            to_email = form.cleaned_data.get('email')  
            email = EmailMessage(  
                        mail_subject, message, to=[to_email]  
            )  
            email.send()  
            return HttpResponse('Please confirm your email address to complete the registration')  
    else:  
        form = RegisterForm()  
    return render(request, 'register.html', {'form': form})  


def activate(request, uidb64, token):  
    User = get_user_model()  
    try:  
        uid = force_str(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)
        print(user)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save()  
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')  
    else:  
        return HttpResponse('Activation link is invalid!')  
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