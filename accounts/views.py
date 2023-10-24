from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from .models import CustomUser
from django.views.generic import UpdateView
from .forms import SignUpForm, EditProfileForm
from django.contrib.auth.views import (
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView,
    PasswordChangeDoneView, PasswordChangeView, LoginView)


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    fields = '__all__'
    # if user is authenticated , they shouldn't be allowed on this page
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('blog:index')


class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, "accounts/signup.html", {"form": form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:login")
        messages = 'Invalid data'
        return render(request, "accounts/signup.html", {"form": form, "messages": messages})


class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/change_password.html'
    redirect_authenticated_user = False
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('accounts:password_change_done')


class CustomPasswordChangeDone(PasswordChangeDoneView):
    template_name = 'accounts/password_change_done.html'


class CustomPasswordResetView(PasswordResetView):
    template_name = "accounts/reset_password.html"

    def get_success_url(self):
        return reverse_lazy('accounts:password_reset_done')


class CustomPasswordResetDone(PasswordResetDoneView):
    template_name = "accounts/reset_password_done.html"


class CustomPasswordResetConfirm(PasswordResetConfirmView):
    template_name = "accounts/reset_password_confirm.html"
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('accounts:password_reset_complete')


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "accounts/reset_password_complete.html"


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("blog:index")
    return redirect("blog:index")


class EditProfileView(UpdateView):
    form_class = EditProfileForm
    template_name = "accounts/edit_profile.html"
    success_url = reverse_lazy("blog:index")

    def get_object(self, queryset=None):
        return self.request.user
