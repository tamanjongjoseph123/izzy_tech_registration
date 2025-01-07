from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter Full name',
            'class': 'form-input',    
        })
    )
  
    stack = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter Your Stack',
            'class': 'form-input'
        })
    )
    highest_certificate = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter Highest Certificate',
            'class': 'form-input'
        })
    )
    phone = forms.CharField(
        widget =forms.NumberInput(attrs={
            'placeholder': 'Phone Number',
            'class': 'form-input'
        })
    )
    email = forms.CharField(
        widget= forms.EmailInput(attrs={
            'placeholder': 'Enter Email',
            'class': 'form-input'
        })
    )
    certificate = forms.FileInput(
        required=True,
        widget = forms.FileInput(
            attrs={
                'placeholder': 'upload certificate not more than 2mb',
                'class': 'form-input'
            }
        )
    )