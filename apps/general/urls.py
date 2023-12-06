from django.urls import path
from .views import AboutPageView, ContactPageVIew


urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact-us/', ContactPageVIew.as_view(), name='contact'),
]
