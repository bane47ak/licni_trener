# Lični trener – projekat

Privatna web aplikacija (mobile-first) za individualni online fitness coaching. Vlasnik je trener, nije programer.

Kompletna specifikacija je u folderu `docs/`. Pročitaj je pre svakog većeg zadatka:
- `docs/01_pregled_i_obim.md` – šta je aplikacija, uloge, paketi, etape, ograničenja
- `docs/02_klijent.md` – šta radi klijent
- `docs/03_trener.md` – šta radi trener/administrator
- `docs/04_pravila.md` – poslovna pravila, bezbednost, podaci
- `docs/05_strane.md` – spisak strana po etapama
- `docs/06_odluke_i_ogranicenja.md` – donete odluke, ograničenja, početne liste
- `docs/07_dizajn.md` – naziv, boje, pravila dizajna
- `docs/08_kasnije.md` – šta se NE gradi sada, ali baza i arhitektura moraju da ga predvide
- `docs/09_plan_izrade.md` – odobreni plan: tehnologije, pristup, šema baze, koraci izrade

## Pravila rada
- Radi po etapama i koracima iz odobrenog plana; ne prelazi na sledeći korak bez potvrde vlasnika.
- Ne dodaj funkcije koje nisu u specifikaciji bez pitanja.
- Posle svakog koraka: pokreni testove, objasni vlasniku jednostavnim jezikom kako da isproba rezultat, napravi git commit.
- Svaku promenu šeme baze radi kroz migraciju.
- Piši na srpskom (komunikacija sa vlasnikom i tekstovi u interfejsu).
- Kad se nešto u specifikaciji promeni, ažuriraj odgovarajući fajl u `docs/`.
- Odluke o tehnologijama i hostingu upiši ovde (odeljak ispod) kad ih vlasnik odobri.

## Odobrene tehnološke odluke
Odobreno 21.11.2026. Detalji i obrazloženja u `docs/09_plan_izrade.md`.

- **Backend i strane:** Python + Django 6.1 (u aprilu 2027. prelaz na 6.2 LTS kao poseban korak). Strane se generišu na serveru (Django šabloni) + HTMX. Bez frontend „build” alata.
- **Prijava i 2FA:** django-allauth (registracija, potvrda emaila, reset lozinke, ograničenje pokušaja, TOTP + recovery kodovi). Serverske sesije, Argon2 za lozinke.
- **Ostale biblioteke:** Pillow (slike, uklanjanje EXIF), openpyxl (uvoz iz Excela), Chart.js (grafikoni). JS/CSS biblioteke se čuvaju u projektu (`static/`), ne učitavaju se sa CDN-a. Sistemski fontovi.
- **Baza:** PostgreSQL, lokalno i na internetu. Sve promene šeme kroz Django migracije.
- **Python i paketi:** uv (Python 3.13). Kod u privatnom GitHub repozitorijumu.
- **Razvoj:** prvo sve lokalno (localhost). Email se lokalno snima kao fajl u `lokalni_emailovi/`; fajlovi se čuvaju u privatnom lokalnom folderu i služe samo preko provere prava (kroz Django storage, da se kasnije samo promeni podešavanje); zakazani poslovi su Django komande.
- **Objavljivanje (preliminarno, potvrđuje se u Etapi P):** Render (Frankfurt) za aplikaciju i bazu, Cloudflare R2 (EU) za fajlove, Brevo za email, domen .rs. Pre otvaranja naloga ponovo proveriti cene.
- **Bezbednost:** šifrovanje u mirovanju na nivou provajdera (bez šifrovanja pojedinačnih polja); audit log ne čuva vrednosti zdravstvenih podataka; tehnički Django admin nije dostupan na internetu.
