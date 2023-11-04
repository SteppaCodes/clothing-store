from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from . models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'is_email_verified', 'created_at')
    # For Search options
    list_filter = list_display
    fieldsets=(
        (
            _('Login Credientials'), 
            {'fields': ('email', 'password')}
        ),
        (
            _('Personal Information'),
            {'fields':('first_name', "last_name", 'avatar')}
        ),
        (
            _("Permissions & Groups"),
            {"fields":("is_email_verified", "is_active", "is_staff", "is_superuser" ,"groups","user_permissions")}
        ),
        (
            _('Important Dates'),
            {"fields":("created_at", "updated_at", "last_login" )}
        )

    )#Never repeat any field
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(User, UserAdmin)
