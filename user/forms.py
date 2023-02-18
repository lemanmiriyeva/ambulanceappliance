from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.core.exceptions import ValidationError
from .models import User


class RegisterForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Confirm password'}))

    class Meta:
        model=User
        fields=(
            'first_name','last_name','email','username','password1','password2'
        )
        widgets={
            'first_name':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Your first name'}),
            'last_name':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Your last name'}),
            'email':forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Your email'}),
            'username':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Your username'})
        }
    def save(self,commit=True):
        user=super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_active=False
        if commit:
            user.save()
        return user
    

class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Your username'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Your password'}))

    def get_invalid_login_error(self):
        self.errors["username"]=[]
        return ValidationError(
            self._errors['username'].append("Username is not found")
        )
    def clean(self):
        username=self.cleaned_data.get("username")
        password=self.cleaned_data.get("password")
        return self.cleaned_data