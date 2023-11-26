from django import forms 
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm

from .models import User

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={"placeholder": "Enter your first name"}),
    )
    last_name= forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={"placeholder": "Enter Your Last Name"})
    )
    email = forms.EmailField(
       widget=forms.EmailInput(attrs={"placeholder": "Enter your email"})
    )

    password1 = forms.CharField(
        label= "Password",
        widget=forms.PasswordInput(attrs={"placeholder": "Enter Your Password"})
    )
    password2 = forms.CharField(
        label= "Confirm Password",
        widget=forms.PasswordInput(attrs={"placeholder": "Confirm Your Password"})
    )

    terms_agreement = forms.BooleanField(
        label="I agree to the terms and conditions",
    )

    class Meta:
        model= User
        fields = [
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
            "terms_agreement"
        ]



class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Enter your email address"}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Enter your password"}),
    )