from django.shortcuts import render
from django.views import View
from .models import TeamMember, SiteDetail

class AboutPageView(View):
    def get(self, request):
        sitedetail, created = SiteDetail.objects.get_or_create()
        members= TeamMember.objects.all()

        context = {
            "sitedetail":sitedetail, 
            "members":members
                   }
        return render(request, 'general/about.html', context)

class ContactPageVIew(View):
    def get(self,request):
        return render(request, 'general/contact.html')
