"""
Pravi lokalnu bazu za aplikaciju (pokreće se jednom, posle instalacije PostgreSQL-a).

Pokretanje (iz foldera projekta):
    uv run python scripts/napravi_lokalnu_bazu.py

Skripta:
1. napravi fajl .env sa tajnim ključem i lozinkom za bazu aplikacije (ako ne postoji),
2. pita te za lozinku korisnika `postgres` (onu koju si uneo pri instalaciji),
3. napravi korisnika i bazu `licni_trener`.
Lozinka `postgres` se nigde ne čuva.
"""

import getpass
import secrets
import sys
from pathlib import Path

import psycopg
from psycopg import sql

KOREN = Path(__file__).resolve().parent.parent
ENV_FAJL = KOREN / ".env"
IME = "licni_trener"


def procitaj_env() -> dict[str, str]:
    vrednosti = {}
    if ENV_FAJL.exists():
        for red in ENV_FAJL.read_text(encoding="utf-8").splitlines():
            if "=" in red and not red.strip().startswith("#"):
                kljuc, vrednost = red.split("=", 1)
                vrednosti[kljuc.strip()] = vrednost.strip()
    return vrednosti


def napravi_env_ako_ne_postoji() -> dict[str, str]:
    if not ENV_FAJL.exists():
        ENV_FAJL.write_text(
            "# Lokalna podešavanja. NE šalje se na GitHub.\n"
            f"DJANGO_SECRET_KEY={secrets.token_urlsafe(50)}\n"
            f"DB_NAME={IME}\n"
            f"DB_USER={IME}\n"
            f"DB_PASSWORD={secrets.token_urlsafe(24)}\n"
            "DB_HOST=localhost\n"
            "DB_PORT=5432\n",
            encoding="utf-8",
        )
        print("Napravljen fajl .env")
    return procitaj_env()


def main() -> int:
    env = napravi_env_ako_ne_postoji()
    lozinka_postgres = getpass.getpass("Lozinka korisnika 'postgres' (unos se ne vidi): ")
    try:
        veza = psycopg.connect(
            host=env.get("DB_HOST", "localhost"),
            port=env.get("DB_PORT", "5432"),
            user="postgres",
            password=lozinka_postgres,
            dbname="postgres",
            autocommit=True,
        )
    except psycopg.OperationalError as greska:
        print(f"\nNe mogu da se povežem na PostgreSQL: {greska}")
        print("Proveri lozinku i da li je PostgreSQL pokrenut, pa pokušaj ponovo.")
        return 1

    korisnik, baza, lozinka = env["DB_USER"], env["DB_NAME"], env["DB_PASSWORD"]
    with veza:
        postoji = veza.execute("SELECT 1 FROM pg_roles WHERE rolname = %s", [korisnik]).fetchone()
        naredba = "ALTER ROLE {} WITH LOGIN CREATEDB PASSWORD {}" if postoji else \
            "CREATE ROLE {} WITH LOGIN CREATEDB PASSWORD {}"
        veza.execute(sql.SQL(naredba).format(sql.Identifier(korisnik), sql.Literal(lozinka)))
        print(f"Korisnik baze '{korisnik}' je spreman.")

        if veza.execute("SELECT 1 FROM pg_database WHERE datname = %s", [baza]).fetchone():
            print(f"Baza '{baza}' već postoji.")
        else:
            veza.execute(sql.SQL("CREATE DATABASE {} OWNER {} ENCODING 'UTF8'").format(
                sql.Identifier(baza), sql.Identifier(korisnik)))
            print(f"Baza '{baza}' je napravljena.")

    print("\nGotovo. Sledeće: uv run python manage.py migrate")
    return 0


if __name__ == "__main__":
    sys.exit(main())
