from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm

from .models import *



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        name = forms.CharField(label = "Username")

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user','place']

class ChangedPasswordResetForm(PasswordResetForm):
    class Meta:
        fields = '__all__'
        exclude = ['extra_context']
