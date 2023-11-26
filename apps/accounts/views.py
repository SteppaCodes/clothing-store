from django.shortcuts import render
from django.views import View
from .forms import RegisterForm, LoginForm


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        context = {"form":form}

        return render(request, 'accounts/register.html', context)

class LoginView(View):
    def get(self, request):
        form = LoginForm
        context = {"form":form}
        return render(request, 'accounts/login.html', context)
