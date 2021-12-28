# accounts/forms
from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser

class CustomUserSignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')
    
    # def __init__(self, *args, **kwargs):
    #     super(CustomUserSignUpForm, self).__init__(*args, **kwargs)
    #     for visible in self.visible_fields():
    #         visible.field.widget.attrs['class'] = 'outline-none border-0'
        
class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email','first_name', 'last_name')