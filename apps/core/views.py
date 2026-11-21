from django.shortcuts import render
from django.utils import timezone


def pocetna(request):
    """Privremena početna strana (korak 0.1): prikaz izgleda i boja."""
    return render(request, "core/pocetna.html", {"danas": timezone.localdate()})
