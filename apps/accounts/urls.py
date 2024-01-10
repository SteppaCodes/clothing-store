from django.urls import path
from . views import (RegisterView, 
                     LoginView, VerifyEmail, ResendVerificationEmail)#, LogoutView


urlpatterns =[
    path("register/", RegisterView.as_view() , name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('verify-email/<uidb64>/<token>/<user_id>', VerifyEmail.as_view(), name='verify-email'),
    path('resend-verification-email', ResendVerificationEmail.as_view(), name='resend-verification-email'),
]