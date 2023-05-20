from django import forms
from .models import Profile
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['phone_number', 'family', 'birth_date']
        labels = {'phone_number': 'Phone Number', 'family': 'Family', 'birth_date': 'Birth Date'}

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']
        labels = {'username': 'Username', 'email': 'Email', 'password': 'Password', 'first_name': 'First Name', 'last_name': 'Last Name'}