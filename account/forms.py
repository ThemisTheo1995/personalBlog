# accounts/forms
from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser

class CustomUserSignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')
        
class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email','first_name', 'last_name')