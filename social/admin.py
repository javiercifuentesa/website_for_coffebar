from django.contrib import admin
from .models import Link

# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')

    def get_readonly_fields(self, request, obj = ...):
        if request.user.groups.filter(name='staff').exists():
            return ('key', 'name')
        else:
            return ('created_at', 'updated_at')

admin.site.register(Link, LinkAdmin)