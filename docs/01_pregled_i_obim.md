# 01 – Pregled proizvoda i obim prve verzije (MVP)

## 1. Šta je aplikacija
**Lični trener** je privatna web aplikacija za **individualni online fitness coaching**. Trener (vlasnik) vodi klijente koji plaćaju saradnju. Nije prodavnica gotovih programa. Plaćanje je **van aplikacije**; trener ručno evidentira uplate i periode važenja članarine.

Radi u pregledaču na telefonu (prioritet), tabletu i računaru. Dizajn je **mobile-first**. Klijent pristupa preko web adrese, uz sopstveni nalog. Ne objavljuje se u prodavnicama aplikacija. Interfejs je na srpskom (latinica), vremenska zona Europe/Belgrade, datumi dd.mm.gggg.

## 2. Uloge
| Uloga | Opis |
|---|---|
| Klijent | Vidi samo svoje podatke i samo funkcije koje dozvoljava njegov paket i status članarine. |
| Trener / Administrator | Jedan nalog u MVP-u, obavezna 2FA (authenticator aplikacija + recovery kodovi). Upravlja svime. |

Podaci se projektuju tako da kasnije može da se doda više trenera (npr. klijent ima vezu ka treneru), ali to se **ne gradi** u MVP-u.

## 3. Paketi
U MVP-u postoje **dva paketa**, oba vođena. Samostalni paketi dolaze kasnije, ali šema baze i pravila pristupa po paketu moraju da ih od početka predvide (vidi `08_kasnije.md`).

| Funkcija | Vođeno | Vođeno i ishrana | Samostalno (kasnije) | Samostalno i ishrana (kasnije) |
|---|:-:|:-:|:-:|:-:|
| Trening program (trener ručno pravi i dodeljuje) | ✓ | ✓ | – | – |
| Generator treninga | kasnije | kasnije | kasnije | kasnije |
| Plan ishrane (trener ručno pravi i dodeljuje) | – | ✓ | – | – |
| Generator ishrane | – | kasnije | – | kasnije |
| Praćenje napretka | ✓ | ✓ | ✓ | ✓ |
| Privatni chat sa trenerom | ✓ | ✓ | – | – |
| AI trener | kasnije | kasnije | kasnije | kasnije |

Zahtevi za obnovu članarine, promenu paketa, promenu programa i brisanje podataka u MVP-u idu **kroz chat**; trener ručno menja članarinu, paket i program. Poseban sistem zahteva je kasnije.

## 4. Obim i redosled razvoja
- **Etapa 1 – Jezgro (paket Vođeno):** registracija i odobravanje, prijava, 2FA za trenera, klijenti i članarine, biblioteka vežbi (uz uvoz iz fajla), ručno pravljenje i dodela trening programa, klijentski tok treninga i rezultata, nedeljni izveštaji sa merenjima i fotografijama, privatni chat (tekst, slike, PDF), obaveštenja u aplikaciji i emailom, arhiviranje i posebna stanja naloga.
- **Etapa 2 – Ishrana (paket Vođeno i ishrana):** biblioteka dnevnih planova, nedeljni/mesečni rasporedi, dodela klijentima, klijentski pregled i evidencija pridržavanja plana.

Spisak strana po etapama je u `05_strane.md`. Šta ne ulazi u MVP je u `08_kasnije.md`.

## 5. Princip: projektuj za celu viziju, gradi po etapama
Šema baze, uloge, paketi i pravila pristupa projektuju se za celu viziju (samostalni paketi, generatori, AI trener), a grade se samo funkcije tekuće etape. Paketi i njihove mogućnosti treba da su podešavanje (npr. oznake funkcija po paketu), ne tvrdo ukucana pravila.

## 6. Ograničenja i okolnosti vlasnika
- **Budžet:** minimalan za početak. Birati najjeftinija rešenja koja su dovoljna; navesti okvirne cene (proveriti aktuelne).
- **Obim:** oko 10 klijenata na početku, možda oko 40 za godinu dana. Mali obim, nema potrebe za složenom infrastrukturom.
- **Održavanje:** vlasnik sam održava aplikaciju i nije programer. Birati **upravljane servise** (hosting koji sam pravi rezervne kopije baze i objavljuje iz git-a), jednostavnu tehnologiju i jasnu dokumentaciju održavanja.
- **Klijenti su u Srbiji.** Podatke čuvati na serverima u Evropi. Zbog zdravstvenih podataka i fotografija bezbednost i privatnost imaju prednost nad cenom i pogodnošću.

## 7. Tehnologije
**Odobreno 21.11.2026:** Django + PostgreSQL, razvoj prvo lokalno, hosting se potvrđuje pred objavljivanje. Detalji u `09_plan_izrade.md` i `CLAUDE.md`. Tekst ispod je prvobitni zahtev.

Nisu zaključane. Claude Code treba da predloži najbolja rešenja (jezik i okvir, frontend pristup, baza, hosting, skladište fajlova, servis za email) uz obrazloženje, 2–3 opcije po većoj odluci i jasnu preporuku. Pre izbora proveriti aktuelne verzije, cene i uslove na internetu. Početni predlog vlasnika iz ranije verzije opisa (Python/FastAPI, PostgreSQL, vanilla JavaScript, serverske sesije, S3-kompatibilno skladište) je samo ideja i može da se zameni.

Kriterijumi, po važnosti: bezbednost i privatnost, jednostavno održavanje bez programera, niska cena, odlično iskustvo na telefonu, mogućnost rasta.

## 8. Nefunkcionalni zahtevi
- Stroga izolacija podataka: klijent nikada ne vidi tuđe podatke.
- Fotografije i fajlovi nisu javni; pristup samo uz proveru prava.
- HTTPS, bezbedne sesije, CSRF zaštita, ograničenje pokušaja prijave, jaka pravila za lozinke.
- Sve izmene šeme baze kroz migracije.
- Automatske rezervne kopije baze i fajlova, uz proveru da se mogu vratiti.
- Evidencija bezbednosnih događaja i promena (audit log) se **beleži od početka**, iako strana za pregled dolazi kasnije.
- U razvoju email i obaveštenja rade kroz lokalni „mock" režim.
- Automatski testovi za ključna pravila: pristup po paketu i članarini, izolacija podataka, redosled treninga, verzionisanje programa.
