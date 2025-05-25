from django import template
from pages.models import Page


register = template.Library()

@register.simple_tag
def get_pages():
    return Page.objects.all()