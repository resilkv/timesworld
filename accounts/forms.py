from django import forms
from .models import Users
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Users
        fields = ['name', 'email', 'country', 'nationality', 'mobile', 'password','role']
