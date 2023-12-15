from django.shortcuts import render, redirect
from django.views import View
from .models import TeamMember, SiteDetail
from apps.general.forms import MessageForm
import sweetify

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
        sitedetail, created = SiteDetail.objects.get_or_create()
        form = MessageForm()

        context = {         
            "sitedetail":sitedetail,
            "form":form 
                   }
        return render(request, 'general/contact.html', context)
    
    def post(self,request):
        sitedetail, created = SiteDetail.objects.get_or_create()
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            sweetify.success(request, 
                             title="sent",
                             text="Your Message was sent successfully",
                             timer=3000
            )
            return redirect("contact")
        context = {         
            "sitedetail":sitedetail,
            "form":form 
                   }
        return render(request, 'general/contact.html', context)
