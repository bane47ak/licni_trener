# 03 – Šta radi trener / administrator

Oznake A1–A29 odgovaraju stranama iz `05_strane.md`.

## 1. Prijava i početna
- **Prijava sa 2FA (A1)** i **podešavanje 2FA, recovery kodovi, promena lozinke (A2).**
- **Početna (A3):** jednostavan meni sa sekcijama i brojačima nepročitanog (nove registracije, nove poruke, novi nedeljni izveštaji, članarine koje uskoro ističu). Bez kartica sa statistikom, grafikona i dashboarda.

## 2. Registracije i klijenti
- **Nove registracije (A14, A15):** lista i pregled zahteva; odobravanje ili odbijanje; dodela paketa; postavljanje početka i isteka članarine.
- **Lista klijenata (A4):** pretraga i filteri: svi, aktivni, čekaju odobrenje, članarina uskoro ističe, članarina istekla, deaktivirani, arhivirani.
- **Profil klijenta (A5–A13):** pregled; izmena osnovnih, zdravstvenih podataka i ciljeva (A6); program (A7); plan ishrane (A8, Etapa 2); istorija treninga (A9); merenja i grafikoni (A10); fotografije napretka (A11); **privatne beleške koje klijent ne vidi** (A12); članarina i uplate (A13).
- **Akcije u profilu:** deaktivacija, arhiviranje završene saradnje, reaktivacija, brisanje ili anonimizacija po zahtevu klijenta (uz potvrdu; nepovratno). Nema automatskog brisanja.

## 3. Članarine i uplate
- **A13 (u profilu klijenta):** ručni unos uplate i perioda važenja, produžetak članarine, promena paketa, istorija. Svaka promena se beleži i klijent se obaveštava.
- **Lista članarina (A16):** pregled po statusu i datumu isteka (uskoro ističe, istekla).

## 4. Biblioteka vežbi
- **Biblioteka (A25)** i **dodavanje i uređivanje vežbe (A26):** naziv, opis, primarne i sekundarne mišićne grupe, oprema, kategorija, oznake, do 3 slike (jedna podrazumevana), odobreni video-linkovi, aktivna/deaktivirana. Nove oznake se dodaju direktno u formi vežbe.
- **Uvoz vežbi iz fajla (A27):** CSV/Excel za masovno punjenje početne biblioteke.

## 5. Trening programi
- **Lista (A17), pravljenje i uređivanje programa (A18), uređivanje pojedinačnog treninga (A19), pregled i dodela klijentu (A20).**
- Program ima 4 nedelje; trening sadrži vežbe sa serijama, ponavljanjima, pauzama, opterećenjem i trajanjem. Vežbe se dodaju, uklanjaju, menjaju i raspoređuju.
- Dodela klijentu je eksplicitna akcija („potvrdi i dodeli"); program počinje u tom trenutku.
- **Kopiranje** programa i pojedinačnih treninga drugom klijentu (akcija u A17/A20), nezavisno od istorije originala.
- Dodeljeni programi su **verzionisani**: izmena biblioteke ne menja postojeće programe; izmena dodeljenog programa pravi novu verziju.

## 6. Planovi ishrane (Etapa 2)
- **Lista (A21), pravljenje i uređivanje dnevnog plana (A22):** obroci, namirnice (naziv, gramaža, kalorije, proteini, ugljeni hidrati, masti), ukupne kalorije i makronutrijenti, oznake. Vrednosti se unose ručno, bez automatskog računanja iz gramaže.
- **Sastavljanje nedeljnog/mesečnog rasporeda (A23)** i **dodela klijentu (A24);** kopiranje plana drugom klijentu je akcija.
- Upozorenje kad se isti dnevni plan ponavlja u istoj nedelji; trener može da potvrdi ponavljanje.

## 7. Komunikacija
- **Lista razgovora (A28)** i **razgovor sa klijentom (A29).** Tekst, fotografije, PDF. Preko chata trener prima i rešava zahteve klijenata (obnova, promena paketa, promena programa, brisanje).
