from django.contrib import admin
from .models import Services

# Register your models here.
class ServicesAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('title', 'subtitle')

admin.site.register(Services, ServicesAdmin)