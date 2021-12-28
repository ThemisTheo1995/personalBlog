from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserSignUpForm, CustomUserUpdateForm

class SignUpView(generic.CreateView):
    form_class = CustomUserSignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
