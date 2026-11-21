# 05 – Spisak strana (MVP)

Oznake: **E1** Etapa 1 (jezgro), **E2** Etapa 2 (ishrana). Kolona „Iz originala" je veza ka prvobitnom spisku strana vlasnika (za proveru da ništa nije izgubljeno).

## Klijentske strane (22)
| # | Strana | Etapa | Iz originala |
|---|---|---|---|
| K1 | Prijava | E1 | 1 |
| K2 | Registracija (sa saglasnostima) | E1 | 2 |
| K3 | Potvrda email adrese | E1 | 3 |
| K4 | Zaboravljena lozinka | E1 | 4 |
| K5 | Postavljanje nove lozinke | E1 | 5 |
| K6 | Čekanje odobrenja registracije | E1 | 6 |
| K7 | Početni upitnik (cilj, iskustvo, zdravstveni podaci, alergije) – nova | E1 | – |
| K8 | Uslovi korišćenja i politika privatnosti – nova | E1 | – |
| K9 | Početna (prečice, poslednji trening, podsetnici i obaveštenja) | E1 | 7 |
| K10 | Moj program (4 nedelje, lista treninga po redosledu) | E1 | 8, 9 |
| K11 | Detalji pojedinačnog treninga | E1 | 10 |
| K12 | Detalji pojedinačne vežbe | E1 | 11 |
| K13 | Unos rezultata treninga | E1 | 12 |
| K14 | Istorija treninga | E1 | 13 |
| K15 | Ishrana – pregled plana (kalendar) | E2 | 14 |
| K16 | Dnevni plan ishrane i evidencija pridržavanja | E2 | 15, 16 |
| K17 | Napredak (pregled, merenja i istorija, galerija fotografija) | E1 | 17, 19, 20 |
| K18 | Unos nedeljnog izveštaja | E1 | 18 |
| K19 | Moj trener – chat | E1 | 22 |
| K20 | Moj profil i podešavanja (podaci, lozinka, obaveštenja) | E1 | 26, 27, 32, 33 |
| K21 | Članarina i paket | E1 | 28 |
| K22 | Ograničen pristup (istekla članarina / deaktiviran / arhiviran) | E1 | 34, 35, 36 |

## Strane trenera / administratora (29)
| # | Strana | Etapa | Iz originala |
|---|---|---|---|
| A1 | Prijava trenera sa 2FA – nova | E1 | – |
| A2 | Podešavanje 2FA, recovery kodovi, promena lozinke – nova | E1 | – |
| A3 | Početna admin panela (meni i brojači) | E1 | 1 |
| A4 | Lista klijenata (pretraga, filteri, uključujući arhivirane) | E1 | 2, 56 |
| A5 | Profil klijenta – pregled i akcije (deaktivacija, arhiviranje, reaktivacija, brisanje/anonimizacija) | E1 | 3, 57, 58, 61 |
| A6 | Izmena podataka, zdravstvenih podataka i ciljeva klijenta | E1 | 4, 5, 6 |
| A7 | Program klijenta (pregled dodeljenih programa i verzija) | E1 | 7 |
| A8 | Plan ishrane klijenta | E2 | 8 |
| A9 | Istorija treninga klijenta | E1 | 9 |
| A10 | Napredak klijenta – merenja i grafikoni | E1 | 10 |
| A11 | Fotografije napretka klijenta | E1 | 11 |
| A12 | Privatne beleške trenera o klijentu | E1 | 12 |
| A13 | Članarina i uplate klijenta (unos uplate, produžetak, promena paketa, istorija) | E1 | 13, 50, 51, 52, 53, 55 |
| A14 | Lista novih registracija | E1 | 14 |
| A15 | Pregled i odobravanje registracije, dodela paketa i članarine | E1 | 15, 16 |
| A16 | Lista članarina (uskoro ističe, istekla) | E1 | 49 |
| A17 | Lista trening programa (uključuje kopiranje) | E1 | 17, 24 |
| A18 | Kreiranje i uređivanje trening programa | E1 | 18, 19, 20 |
| A19 | Uređivanje pojedinačnog treninga (vežbe, serije, ponavljanja, pauze, opterećenje, trajanje) | E1 | 21, 22 |
| A20 | Pregled i dodela programa klijentu | E1 | 23 |
| A21 | Lista planova ishrane | E2 | 25 |
| A22 | Kreiranje i uređivanje dnevnog plana ishrane | E2 | 26, 27, 28 |
| A23 | Sastavljanje nedeljnog/mesečnog rasporeda | E2 | 29 |
| A24 | Dodela rasporeda klijentu (uključuje kopiranje) | E2 | 30, 31 |
| A25 | Biblioteka vežbi (lista, filteri) | E1 | 32, 36 |
| A26 | Dodavanje i uređivanje vežbe (uključuje detalje) | E1 | 33, 34, 35 |
| A27 | Uvoz vežbi iz fajla – nova | E1 | – |
| A28 | Lista privatnih razgovora | E1 | 37 |
| A29 | Razgovor sa klijentom | E1 | 38 |

## Šta nije u ovom spisku i zašto
Strane iz originalnog spiska koje se ne grade u MVP-u (zahtevi klijenata, podešavanja AI trenera, grupne poruke, poređenje fotografija, AI trener, izbor kriterijuma za generisanje, podešavanja aplikacije i pregled bezbednosnog loga, tok brisanja posle 12 meseci) opisane su u `08_kasnije.md`.
