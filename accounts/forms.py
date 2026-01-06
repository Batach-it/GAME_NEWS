from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile




class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={
            'class': 'form-control rounded-input text-center',
            'placeholder': 'Enter username'
        })
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={
            'class': 'form-control rounded-input text-center',
            'placeholder': 'Enter email'
        })
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control rounded-input text-center',
            'placeholder': 'Enter password'
        })
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control rounded-input text-center',
            'placeholder': 'Confirm password'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']






class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={
            'class': 'form-control text-center',  # центр тексту
            'placeholder': 'Enter username'
        })
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control text-center',  # центр тексту
            'placeholder': 'Enter your password'
        })
    )





class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']