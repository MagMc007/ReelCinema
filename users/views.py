from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm, CustomLoginForm
from django.contrib.auth.views import LoginView


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:login-view')  
    template_name = 'users/register.html'


class SingInView(LoginView):
    form_class = CustomLoginForm
    template_name = 'users/login.html'
    # no success url here, it is next_page when it comes to loggin in
    next_page = reverse_lazy('users:dummy')

""" dummy page for redirects checking """

def dummy(request):
    return render(request, "users/dummy.html")
