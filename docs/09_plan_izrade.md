# 09 – Odobreni plan izrade

Status: **ODOBREN** 21.11.2026. Tehnološke odluke su upisane i u `CLAUDE.md`.
Poslovna pravila koja su dogovorena uz plan upisana su u `02_klijent.md`, `04_pravila.md` i `06_odluke_i_ogranicenja.md`.

---

## 1. Tehnologije

| Oblast | Odluka |
|---|---|
| Jezik i okvir | **Python + Django** (6.1; u aprilu 2027. prelaz na 6.2 sa dugoročnom podrškom, kao poseban korak) |
| Prijava, 2FA, emailovi naloga | **django-allauth** (registracija, potvrda emaila, reset lozinke, promena emaila, ograničenje pokušaja, TOTP 2FA + recovery kodovi) |
| Izgled | Django šabloni (strane se prave na serveru) + **HTMX** za delove strane bez osvežavanja; ručno pisan CSS sa bojama iz `07_dizajn.md`; bez alata za „build” |
| Grafikoni | **Chart.js** (fajl je u projektu, ne učitava se sa tuđeg servera) |
| Slike | **Pillow** – smanjivanje i uklanjanje EXIF podataka |
| Uvoz iz Excela | **openpyxl** |
| Baza | **PostgreSQL** (i lokalno i na internetu) |
| Upravljanje Python verzijom i paketima | **uv** |
| Kod | Git + privatni GitHub repozitorijum |

### Razvoj prvo lokalno
Aplikacija se pravi i isprobava **na tvom računaru** (localhost). Izbor hostinga se potvrđuje kad Etapa 1 bude gotova.
Do tada:
- **Email**: ne šalje se stvarno; svaki email se snima kao fajl u folder `lokalni_emailovi/` (otvaraš ga duplim klikom).
- **Fajlovi** (slike, PDF): čuvaju se u privatnom folderu na disku, nikad direktno dostupni – isto kao kasnije na internetu, preko provere prava. Prelaz na skladište u oblaku je samo promena podešavanja.
- **Zakazani poslovi** (podsetnici, brisanje slika iz chata posle 7 dana): pokreću se komandom; na internetu ih pokreće cron.

### Preliminarni izbor za objavljivanje (najjeftinija dovoljna varijanta)
| Oblast | Izbor | Okvirno |
|---|---|---|
| Hosting + baza | Render, Frankfurt | ~14 $/mes |
| Fajlovi | Cloudflare R2, EU lokacija | 0 $ do 10 GB |
| Email | Brevo | 0 € (300 dnevno) |
| Domen | .rs (naziv se bira pred objavljivanje) | ~10–25 €/god |
Pre otvaranja naloga cene i uslovi se ponovo proveravaju.

---

## 2. Bezbednost i rezervne kopije
- Lozinke: Argon2, najmanje 10 znakova, provera protiv čestih lozinki.
- Kolačići samo preko HTTPS-a, nedostupni JavaScript-u; sesija ističe posle neaktivnosti.
- CSRF zaštita, ograničenje pokušaja prijave i reseta lozinke, bezbednosna zaglavlja (HSTS, CSP, zabrana ugrađivanja).
- Svaka provera pristupa na serveru; svaki upit za podatke klijenta vezan je za prijavljenog korisnika.
- Fajlovi privatni; pristup samo posle provere prava (na internetu: link koji važi nekoliko minuta).
- Slike: smanjivanje i brisanje EXIF podataka pri otpremanju.
- Šifrovanje u mirovanju: na nivou baze i skladišta (provajder). Bez dodatnog šifrovanja pojedinačnih polja (rizik gubitka ključa).
- Audit log od prvog dana. Za zdravstvene podatke beleži se **koje polje je promenjeno**, ne vrednost.
- Tehnički Django admin nije dostupan na internetu.
- Rezervne kopije (na internetu): automatske kopije baze kod provajdera + nedeljni izvoz baze u posebno privatno skladište (8 nedelja) + nedeljna kopija fotografija napretka i slika vežbi + probno vraćanje pre puštanja u rad. Uputstvo u `docs/odrzavanje.md`.

---

## 3. Uloge, prijava i pristup

- **Uloge**: `klijent`, `trener`. Svaki klijent ima vezu ka treneru (priprema za više trenera).
- **Status naloga klijenta**: čeka potvrdu emaila → čeka odobrenje → aktivan → deaktiviran / arhiviran; uz to anonimizovan. Odbijena registracija se briše (vidi `04_pravila.md`).
- **„Istekla članarina”** nije status nego se računa iz datuma članarine.
- **Paketi su podešavanje**: tabela paketa, tabela funkcija (`trening_program`, `plan_ishrane`, `napredak`, `chat`; kasnije `generator_treninga`, `generator_ishrane`, `ai_trener`) i veza paket ↔ funkcija.
- **Jedno pravilo pristupa** (na jednom mestu u kodu): nalog aktivan **i** danas unutar perioda članarine **i** paket sadrži funkciju. Izuzeci kad je članarina istekla: prijava, osnovni profil, K21 i **chat** ostaju dostupni. Deaktiviran i arhiviran: bez chata.
- **Klijent**: email + lozinka, email mora biti potvrđen. **Jedan aktivan uređaj**: nova prijava prekida ostale sesije; ako je prekinuta zaista aktivna sesija, email klijentu i treneru + obaveštenje u aplikaciji + audit.
- **Trener**: email + lozinka + obavezan kod iz authenticator aplikacije, 10 recovery kodova; bez podešene 2FA vidi samo podešavanje 2FA. Može biti prijavljen na više uređaja. Nalog se pravi komandom.
- Automatski testovi: pravilo pristupa, izolacija podataka, redosled treninga, verzionisanje.

---

## 4. Struktura projekta

```
licni_trener/
├─ CLAUDE.md, README.md
├─ docs/                    specifikacija, plan, odrzavanje.md, format_uvoza_vezbi.md
├─ config/                  podešavanja (razvoj / test / produkcija), adrese
├─ apps/
│  ├─ core/                 šifarnici, pravilo pristupa, zajednički izgled
│  ├─ accounts/             korisnici, uloge, saglasnosti, sesije/uređaji, 2FA
│  ├─ clients/              profil klijenta, upitnik, statusi, beleške trenera
│  ├─ memberships/          paketi, funkcije, članarine, uplate
│  ├─ exercises/            biblioteka vežbi, slike, video-linkovi, uvoz
│  ├─ training/             šabloni, dodela, verzije, treninzi, rezultati
│  ├─ nutrition/            (Etapa 2) dnevni planovi, rasporedi, dodela, pridržavanje
│  ├─ progress/             nedeljni izveštaji, fotografije, ispravke merenja
│  ├─ chat/                 razgovori, poruke, prilozi
│  ├─ notifications/        obaveštenja u aplikaciji, email, podsetnici
│  ├─ files/                otpremanje, obrada slika, privatni pristup
│  └─ audit/                evidencija događaja
│  (kasnije: requests/, generators/, ai_coach/)
├─ templates/  klijent/, trener/, email/, zajedničko
├─ static/     css/, js/ (htmx, chart.js)
└─ tests/
```

---

## 5. Šema baze (cela vizija)

**[E1]** Etapa 1, **[E2]** Etapa 2, **[K]** kasnije (tabela se pravi kad zatreba; postojeće tabele su oblikovane da to dozvole).

**Korisnici i pristup**
- User [E1] – email, ime, prezime, uloga, aktivan, datum kreiranja.
- TrainerProfile [E1].
- ClientProfile [E1] – korisnik, trener, status naloga, datum promene statusa, datum završetka upitnika, datum rođenja, visina, cilj (+ „drugo”), nivo iskustva, zdravstveni podaci, povrede, alergije, namirnice koje izbegava, datum arhiviranja.
- LegalDocument [E1] – vrsta, verzija, tekst, datum objave. ConsentAcceptance [E1] – korisnik, dokument+verzija, vreme prihvatanja.
- UserSession [E1] – korisnik, sesija, pregledač, IP, početak, kraj, razlog kraja.
- 2FA tabele [E1] – iz django-allauth.

**Šifarnici** – Goal, ExperienceLevel, MuscleGroup, Equipment, ExerciseCategory, ExerciseTag [E1], MealPlanTag [E2]: naziv, redosled, aktivan.

**Paketi i članarine**
- Package [E1] – kod, naziv, samostalni da/ne, aktivan. Feature [E1]. PackageFeature [E1].
- Membership [E1] – klijent, paket, početak, kraj, ko je uneo, napomena. Svaki period = novi red (istorija).
- Payment [E1] – klijent, članarina (koja nosi paket), datum uplate, iznos (RSD), napomena, ko je uneo.

**Vežbe**
- Exercise [E1] – naziv, opis, kategorija, primarne/sekundarne mišićne grupe, oprema, oznake, status (nacrt iz uvoza / aktivna / deaktivirana). Ne briše se, samo deaktivira.
- ExerciseImage [E1] (najviše 3, jedna podrazumevana), ExerciseVideoLink [E1] (link, naslov, odobren, izvor, ko je odobrio), ExerciseImportBatch [E1].

**Trening**
- ProgramTemplate, TemplateWorkout, TemplateWorkoutExercise [E1] – šabloni (serije, ponavljanja, pauza, opterećenje, trajanje, napomena, redosled; izvor: ručno / kopija / kasnije generator).
- ProgramAssignment [E1] – klijent, trener, vreme dodele (= početak), status (aktivan / zaključan), vreme i razlog zaključavanja (nov program / istekla članarina / deaktivacija / arhiviranje).
- ProgramVersion [E1] – broj verzije, datum, autor, napomena, aktuelna.
- ProgramWorkout, ProgramWorkoutExercise [E1] – **snimak** podataka u trenutku dodele/izmene (naziv, opis, video-linkovi) + veza ka vežbi radi slika.
- WorkoutSession [E1] – klijent, dodela, trening, redni broj, status (u toku / završen / nezavršen), datum završetka.
- ExerciseResult [E1] – sesija, vežba, broj serije (prazno = cela vežba), težina, ponavljanja, napomena.

**Ishrana**
- DayPlan, DayPlanMeal, DayPlanItem [E2] – obroci i namirnice (naziv, gramaža, kcal, proteini, UH, masti); ukupno se **sabira** iz unetih vrednosti.
- ScheduleTemplate, ScheduleTemplateDay [E2] – raspored, dan → dnevni plan, potvrđeno ponavljanje.
- NutritionAssignment, NutritionVersion, NutritionDay [E2] – dodela, verzije, dan sa snimkom plana.
- NutritionAdherence [E2] – klijent, datum, ispoštovan / nije (bez reda = nije evidentirano).
- CalorieRange [K].

**Napredak**
- WeeklyReport [E1] – klijent, vreme slanja, težina, struk, stomak, kukovi, butina, nadlaktica, napomena (više izveštaja nedeljno je dozvoljeno).
- ProgressPhoto [E1] – izveštaj, ugao, fajl. MeasurementCorrection [E1] – polje, staro, novo, kada, komentar trenera.

**Chat**
- Conversation [E1] (vrsta: privatni; kasnije grupni), Message [E1], Attachment [E1] (slika / PDF; kasnije video; ističe; obrisano), ReadMarker [E1].

**Obaveštenja, beleške, audit**
- Notification [E1] (primalac, vrsta, tekst, link, pročitano, ključ protiv duplikata), NotificationPreference [E1], EmailOutbox [E1], TrainerNote [E1], AuditEvent [E1].

**Kasnije [K]**: ClientRequest, GenerationCriteria, GenerationRun, AiCoachSettings, AiConversation, AiMessage, AiSummary, PushSubscription, AppSetting.

---

## 6. Koraci izrade

Posle **svakog koraka**: automatski testovi, uputstvo vlasniku kako da isproba, git commit, čeka se potvrda pre sledećeg koraka.

### Etapa 0 – Priprema (lokalno)
| Korak | Sadržaj | Strane |
|---|---|---|
| 0.1 | Instalacija uv (i preko njega Python 3.13) i PostgreSQL-a; git repozitorijum; povezivanje sa privatnim GitHub repozitorijumom; prazan Django projekat; boje i osnovni izgled; prvi test; README sa komandama za pokretanje. | – |

### Etapa 1 – Jezgro (paket Vođeno)
| Korak | Sadržaj | Strane |
|---|---|---|
| 1.1 | Sopstveni model korisnika (prijava emailom) – lokalna baza se zbog toga pravi iznova (još je prazna). Korisnici, uloge, rasporedi (klijent: donja navigacija; trener: bočni/skriveni meni), strane grešaka, osnova audit loga, lokalni emailovi u folderu. | – |
| 1.2 | Registracija sa saglasnostima, privremeni pravni tekstovi („NACRT”), potvrda emaila, prijava, zaboravljena i nova lozinka, ograničenje pokušaja. | K1, K2, K3, K4, K5, K8 |
| 1.3 | Prijava trenera sa obaveznom 2FA, recovery kodovi, promena lozinke. | A1, A2 |
| 1.4 | Jedan aktivan uređaj po klijentu + obaveštenja o prekinutoj sesiji. | (K1) |
| 1.5 | Paketi, funkcije, članarine, pravilo pristupa + testovi; strane čekanja i ograničenog pristupa. | K6, K22 |
| 1.6 | Nove registracije: lista, pregled, odobravanje/odbijanje, dodela paketa i perioda, email o odobrenju; početna trenera (prvi brojači). | A14, A15, A3 |
| 1.7 | Početni upitnik; moj profil i podešavanja; obaveštenje treneru o promeni cilja/zdravlja. | K7, K20 |
| 1.8 | Lista klijenata, profil, izmena podataka, privatne beleške, deaktivacija / arhiviranje / reaktivacija / brisanje i anonimizacija. | A4, A5, A6, A12 |
| 1.9 | Članarine i uplate, lista članarina, „Članarina i paket”, podsetnik 3 dana pre isteka. | A13, A16, K21 |
| 1.10 | Biblioteka vežbi: lista, filteri, dodavanje/izmena, do 3 slike, YouTube linkovi, oznake u formi; detalji vežbe za klijenta. | A25, A26, K12 |
| 1.11 | Uvoz vežbi iz CSV/Excel fajla sa pregledom pre aktiviranja + primer fajla. | A27 |
| 1.12 | Šabloni trening programa: lista, pravljenje, uređivanje treninga, kopiranje. | A17, A18, A19 |
| 1.13 | Pregled i dodela programa („potvrdi i dodeli”), zaključavanje starog programa, verzionisanje, program klijenta i verzije, email „novi program”, kopiranje drugom klijentu. | A20, A7 |
| 1.14 | Klijent: moj program, detalji treninga (slika + video odmah vidljivi), pravilo redosleda; početna klijenta (prečice, poslednji trening). | K10, K11, K9 |
| 1.15 | Brz unos rezultata, završetak treninga, istorija treninga kod klijenta i trenera. | K13, K14, A9 |
| 1.16 | Nedeljni izveštaj sa merenjima i fotografijama; podsetnici ponedeljkom i utorkom. | K18 |
| 1.17 | Napredak: grafikoni, istorija merenja sa ispravkama, galerija; kod trenera merenja, grafikoni, fotografije, komentar na ispravku. | K17, A10, A11 |
| 1.18 | Chat – tekst, lista razgovora, brojači nepročitanog (osvežavanje na ~10 s dok je chat otvoren). | K19, A28, A29 |
| 1.19 | Chat – slike do 10 MB (smanjivanje, bez EXIF-a), PDF do 10 MB, brisanje slika posle 7 dana uz oznaku isteka. | K19, A29 |
| 1.20 | Obaveštenja u aplikaciji – dovršetak, svi brojači kod trenera, podešavanja obaveštenja. | K9, A3, K20 |
| 1.21 | Bezbednosni pregled, kompletno lokalno testiranje celog toka, `docs/odrzavanje.md` (lokalni deo). | – |

### Etapa P – Objavljivanje na internetu (kad vlasnik odluči: posle Etape 1 ili posle Etape 2)
| Korak | Sadržaj |
|---|---|
| P.1 | Ponovna provera cena; konačan izbor hostinga; kupovina .rs domena; nalozi (Render, Cloudflare, Brevo) uz vođenje korak po korak. |
| P.2 | Prvo objavljivanje, HTTPS, prebacivanje fajlova i emaila na servise u oblaku, cron poslovi. |
| P.3 | Rezervne kopije, probno vraćanje, uputstvo za održavanje (deo za internet). |
| P.4 | Pravni tekstovi vlasnika, uklanjanje probnih podataka, trenerski nalog, unos vežbi, probni rad sa 1–2 klijenta. |

### Etapa 2 – Ishrana (paket Vođeno i ishrana)
| Korak | Sadržaj | Strane |
|---|---|---|
| 2.1 | Oznake planova; lista i pravljenje/uređivanje dnevnog plana, kopiranje. | A21, A22 |
| 2.2 | Sastavljanje nedeljnog/mesečnog rasporeda sa upozorenjem na ponavljanje. | A23 |
| 2.3 | Dodela rasporeda klijentu, verzionisanje, kopiranje; plan ishrane u profilu klijenta. | A24, A8 |
| 2.4 | Klijent: kalendar, dnevni plan, evidencija pridržavanja; „Ishrana” u navigaciji samo ako je u paketu. | K15, K16, A8 |
| 2.5 | Završna provera, testovi, ažuriranje uputstva. | – |
