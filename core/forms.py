from django import forms
from .models import *

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length = 7,
        min_length = 5,
        widget=forms.TextInput(attrs={
            'class':'form-control mb-4',
            'placeholder':'Your full name',
            })
    )
    class Meta:
        model=Contact
        fields=('first_name','last_name','email','phone','message')
        widgets={
           
            'last_name': forms.TextInput(attrs={
            'class':'form-control mb-4',
            'placeholder':'Your last name'
            }),
            'email': forms.EmailInput(attrs={
            'class':'form-control mb-4',
            'placeholder':'Your email'
            }),
            'phone': forms.TextInput(attrs={
            'class':'form-control mb-4',
            'placeholder':'Your phone number'
            }),
            'message': forms.Textarea(attrs={
            'class':'form-control mb-4 w-100',
            'rows':5,

            'placeholder':'Your email'
            })
        }


class QuoteForm(forms.ModelForm):
    class Meta:
        model=Quotes
        fields=('name','phone','email','address','zip_code')
        widgets={
            'name': forms.TextInput(attrs={
            'class':'form-control py-3',
            'placeholder':'Your full name',
            }),
            'phone': forms.TextInput(attrs={
            'class':'form-control py-3',
            'placeholder':'Your phone number'
            }),
            'email': forms.EmailInput(attrs={
            'class':'form-control py-3',
            'placeholder':'Your email'
            }),
            'address': forms.TextInput(attrs={
            'class':'form-control py-3',
            'placeholder':'Your address'
            }),
            'zip_code': forms.TextInput(attrs={
            'class':'form-control py-3',
            'placeholder':'Zip code'
            }),

        }

