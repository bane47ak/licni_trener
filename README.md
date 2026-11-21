# Lični trener

Privatna web aplikacija za individualni online fitness coaching.
Specifikacija i plan su u folderu [`docs/`](docs/), pravila rada u [`CLAUDE.md`](CLAUDE.md).

## Šta treba da bude instalirano (jednom)
- **Git**
- **uv** – upravlja Python-om i paketima (`winget install astral-sh.uv`)
- **PostgreSQL 17** – baza (pri instalaciji zapiši lozinku korisnika `postgres`)

## Prvo pokretanje (jednom)
Sve komande se kucaju u PowerShell-u, u folderu projekta.

1. Napravi lokalnu bazu (pitaće te lozinku korisnika `postgres`):
   ```powershell
   uv run python scripts/napravi_lokalnu_bazu.py
   ```
2. Pripremi tabele u bazi:
   ```powershell
   uv run python manage.py migrate
   ```

## Svakodnevno
- **Pokreni aplikaciju:**
  ```powershell
  uv run python manage.py runserver
  ```
  Zatim u pregledaču otvori <http://localhost:8000>. Zaustavljanje: `Ctrl+C` u prozoru PowerShell-a.
- **Pokreni automatske testove:**
  ```powershell
  uv run python manage.py test
  ```
- **Emailovi** (lokalno se ne šalju): pojavljuju se kao fajlovi u folderu `lokalni_emailovi/`.

## Važni fajlovi i folderi
| Šta | Gde |
|---|---|
| Podešavanja | `config/settings/` (`base.py` zajedničko, `local.py` tvoj računar, `test.py` testovi) |
| Tajne vrednosti (ključ, lozinka baze) | `.env` – **nikad se ne šalje na GitHub** |
| Boje dizajna | `static/css/tokens.css` |
| Delovi aplikacije | `apps/` |
| Izgled strana | `templates/` i `apps/*/templates/` |
