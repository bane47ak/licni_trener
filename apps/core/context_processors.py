from django.conf import settings


def app(request):
    """Podaci dostupni u svim šablonima."""
    return {"APP_NAME": settings.APP_NAME}
