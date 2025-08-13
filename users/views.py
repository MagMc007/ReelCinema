from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import (
    CustomUserCreationForm,
    CustomLoginForm, 
    CustomUserChangeForm)
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("users:login-view")
    template_name = "users/register.html"


class SingInView(LoginView):
    form_class = CustomLoginForm
    template_name = "users/login.html"
    # no success url here, it is next_page when it comes to loggin in
    next_page = reverse_lazy("users:dummy")


def dummy(request):
    """dummy page for redirects checking"""
    return render(request, "users/dummy.html")


class SignOutView(LogoutView, LoginRequiredMixin):
    """log a user out and redirect to log in page"""

    next_page = "users:login-view"


@login_required
def userChangeView(request):
    """a view for changing credential"""
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("users:dummy")
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(
        request,
        "users/edit_user.html",
        {
            "form": CustomUserChangeForm,
        },
    )