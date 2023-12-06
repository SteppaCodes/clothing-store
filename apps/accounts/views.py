from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.views import View
from .forms import RegisterForm, LoginForm


class RegisterView(View):

    def get_form(self, data=None):
        return RegisterForm(data=data)

    def get(self, request):
        form = self.get_form()
        context = {"form":form}

        return render(request, 'accounts/register.html', context)
    
    def post(self ,request):
        form = self.get_form(data=request.POST)
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

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(request, username=email, password=password)

            if not user:
                messages.error(request, 'Invalid Credentials')
                return redirect('login')
            else:
                login(request, user)
                messages.success(request, 'Login Successful')
                return redirect('home')
            
        context ={'form':form}
        return render(request, 'accounts/login.html', context)

# class LogoutView(View):
#     def get(self, request):
#         user = request.user
#         print(user)
#         #logout(user)
#         return redirect('home')
