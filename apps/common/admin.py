from django.contrib import admin
from django.utils.safestring import mark_safe #Helps to render HTMl text in your django app


admin.site.site_header= mark_safe('<strong>C.S ADMIN</strong>')
