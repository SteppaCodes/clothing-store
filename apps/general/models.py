from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.common.models import BaseModel


class SiteDetail(BaseModel):
    name = models.CharField(max_length=200)
    desc = models.TextField(_("description"), null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, null =True)
    address = models.CharField(max_length=500, null=True)
    work_hours = models.CharField(max_length=200, null=True)

    fb = models.URLField(verbose_name=_("Facebook"), default="https://www.facebook.com")
    ig = models.URLField(
        verbose_name=_("Instagram"), default="https://www.instagram.com/"
    )
    tw = models.URLField(verbose_name=_("Twitter"), default="https://www.twitter.com/")
    ln = models.URLField(
        verbose_name=_("Linkedin"), default="https://www.linkedin.com/"
    )

    def __str__(self):
        return self.name
    
ROLE_CHOICES = (
    ("CO-Founder", "CO-Founder"),
    ("Product Expert", "Product Expert"),
    ("Chief Marketing", "Chief Marketing"),
    ("Product Specialist", "Product Specialist"),
    ("Product Photographer", "Product Photographer"),
    ("General Manager", "General Manager"),
)

class TeamMember(BaseModel):
    name= models.CharField(max_length=100)
    role = models.CharField(max_length=200, choices=ROLE_CHOICES)
    desc= models.CharField(_("description") ,max_length=300)
    avatar= models.ImageField(upload_to='team/')
    
    fb = models.URLField(verbose_name=_("Facebook"), default="https://www.facebook.com")
    ig = models.URLField(
        verbose_name=_("Instagram"), default="https://www.instagram.com/"
    )
    tw = models.URLField(verbose_name=_("Twitter"), default="https://www.twitter.com/")
    ln = models.URLField(
        verbose_name=_("Linkedin"), default="https://www.linkedin.com/"
    )

    def __str__(self):
        return self.name
    
    @property
    def get_avatar(self):
        try:
            url=self.avatar.url
        except:
            url=''
        return url


class Message(BaseModel):
    name=models.CharField(max_length=300)
    email=models.EmailField()
    subject= models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.name

