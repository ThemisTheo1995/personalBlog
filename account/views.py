from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserSignUpForm, CustomUserUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .choices import avatar_choices

class SignUpView(generic.CreateView):
    form_class = CustomUserSignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['avatars'] = avatar_choices
        return context
    
    def form_valid(self, form):
        user = form.save(commit = False)
        avatar = self.request.POST.get('avatar','')
        user.avatar = avatar
        user.save()
        return super(SignUpView, self).form_valid(form)
    
class UpdateUserView(LoginRequiredMixin, generic.UpdateView):
    
    form_class = CustomUserUpdateForm
    success_url = reverse_lazy('blog:posts')
    template_name = 'registration/updateUser.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['avatars'] = avatar_choices
        return context
    
    def form_valid(self, form):
        user = form.save(commit = False)
        avatar = self.request.POST.get('avatar','')
        user.avatar = avatar
        user.save()
        return super(UpdateUserView, self).form_valid(form)
    
    def get_object(self, queryset=None): 
        return self.request.user
