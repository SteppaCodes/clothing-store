from django.shortcuts import render
from django.views import View
from .models import TeamMember

class AboutPageView(View):
    def get(self, request):
        members= TeamMember.objects.all()

        context = {"members":members}
        return render(request, 'general/about.html', context)

class ContactPageVIew(View):
    def get(self,request):
        return render(request, 'general/contact.html')
