from django.contrib import admin
from .models import Info


class InfoAdmin(admin.ModelAdmin):
    list_display = ('info_icon', 'info_text')


admin.site.register(Info, InfoAdmin)

# Register your models here.
