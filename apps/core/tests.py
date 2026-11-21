import datetime

from django.conf import settings
from django.test import TestCase
from django.urls import reverse
from django.utils import formats, translation


class PocetnaStranaTest(TestCase):
    def test_pocetna_se_otvara(self):
        odgovor = self.client.get(reverse("pocetna"))
        self.assertEqual(odgovor.status_code, 200)
        self.assertContains(odgovor, "Lični trener")
        self.assertContains(odgovor, 'lang="sr-Latn"')

    def test_zastitna_zaglavlja(self):
        odgovor = self.client.get(reverse("pocetna"))
        self.assertEqual(odgovor.headers["X-Frame-Options"], "DENY")
        self.assertEqual(odgovor.headers["X-Content-Type-Options"], "nosniff")


class PodesavanjaTest(TestCase):
    def test_vremenska_zona_i_jezik(self):
        self.assertEqual(settings.TIME_ZONE, "Europe/Belgrade")
        self.assertEqual(settings.LANGUAGE_CODE, "sr-latn")

    def test_format_datuma_dd_mm_gggg(self):
        with translation.override("sr-latn"):
            tekst = formats.date_format(datetime.date(2026, 11, 21), "SHORT_DATE_FORMAT")
        self.assertEqual(tekst, "21.11.2026")

    def test_baza_je_postgresql(self):
        self.assertEqual(
            settings.DATABASES["default"]["ENGINE"], "django.db.backends.postgresql"
        )

    def test_lozinka_mora_imati_najmanje_10_znakova(self):
        from django.contrib.auth.password_validation import validate_password
        from django.core.exceptions import ValidationError

        with self.assertRaises(ValidationError):
            validate_password("Kr4tka!x")  # 8 znakova
        validate_password("Dovoljno-Duga-Lozinka-27")  # ne sme da prijavi grešku

    def test_lozinke_se_cuvaju_argon2_postupkom(self):
        from config.settings import base

        self.assertIn("Argon2", base.PASSWORD_HASHERS[0])
