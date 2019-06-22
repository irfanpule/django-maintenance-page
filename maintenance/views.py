from django.shortcuts import render
from django.conf import settings


def index(request):
    title = "We'll be back soon!"
    description = "Sorry for the inconvenience but we&rsquo;re performing some maintenance at the moment." \
        "If you need to you can always contact us, otherwise we&rsquo;ll be back online shortly!"
    signature = "The Team"

    if hasattr(settings, 'MAINTENANCE_TEMPLATE_DATA'):
        title = settings.MAINTENANCE_TEMPLATE_DATA.get('title', title)
        description = settings.MAINTENANCE_TEMPLATE_DATA.get('description', description)
        signature = settings.MAINTENANCE_TEMPLATE_DATA.get('signature', signature)

    context = {
        "title": title,
        "description": description,
        "signature": signature
    }
    return render(request, 'maintenance/index.html', context)
