from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms

from django.contrib.auth.forms import AuthenticationForm


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

