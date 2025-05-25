from .models import Link

def ctx_dict(request):
    ctx = {}
    ctx['links'] = Link.objects.all()
    for link in ctx['links']:
        ctx[link.key] = link.url
    return ctx