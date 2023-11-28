from django.shortcuts import render, redirect
from django.views import View
from .forms import RegisterForm, LoginForm


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        context = {"form":form}

        return render(request, 'accounts/register.html', context)
    
    def post(self ,request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        context= {'form':form}
        return render(request, 'accounts/register.html', context)
    

class LoginView(View):
    def get(self, request):
        form = LoginForm
        context = {"form":form}
        return render(request, 'accounts/login.html', context)

