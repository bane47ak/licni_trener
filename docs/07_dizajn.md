# 07 – Dizajn

Naziv: **Lični trener**. Za sada tekstualni logo; stil je miran, čist i jasan, prilagođen telefonu.

## 1. Boje (definisati kao CSS promenljive / tokene)
| Namena | Boja |
|---|---|
| Glavna pozadina aplikacije | `#F8FAFC` |
| Kartice, forme, modalni prozori | `#FFFFFF` |
| Sekundarna površina (zaglavlja tabela, sporedni blokovi) | `#F1F5F9` |
| Tanke ivice i linije razdvajanja | `#E2E8F0` |
| Glavni tekst i naslovi | `#0F172A` |
| Sekundarni tekst i opisi | `#475569` |
| Pomoćne labele i placeholder tekst | `#94A3B8` |
| Glavna akcentna boja (glavna dugmad, aktivni tabovi, fokus) | `#0F766E` |
| Hover i pritisnuto stanje glavnog dugmeta | `#115E59` |
| Blaga pozadina istaknutih blokova i aktivnih stavki | `#F0FDFA` |
| Uspeh: tekst / pozadina | `#15803D` / `#DCFCE7` |
| Upozorenje: tekst / pozadina | `#B45309` / `#FEF3C7` |
| Greška: tekst / pozadina | `#B91C1C` / `#FEE2E2` |
| Informacija: tekst / pozadina | `#1D4ED8` / `#DBEAFE` |

## 2. Značenje boja po stanjima
- **Uspeh (zeleno):** završen trening, ispoštovan plan ishrane, aktivna članarina, odobreno.
- **Upozorenje (žuto):** na čekanju odobrenja, članarina uskoro ističe, upozorenje o ponavljanju plana.
- **Greška (crveno):** istekla članarina, odbijeno, greške u formama.
- **Informacija (plavo):** podsetnici (nedeljni izveštaj), obaveštenja, oznaka isteka fotografije u chatu.
- Stanje se nikada ne prikazuje samo bojom: uz boju uvek ide tekst ili ikona.

## 3. Pristupačnost
- `#94A3B8` na beloj pozadini ima nizak kontrast (oko 2,6:1). Koristiti ga samo za placeholder i nebitne labele; sve što klijent mora da pročita ide u `#475569` ili `#0F172A`.
- Bela slova na `#0F766E` dugmetu imaju dovoljan kontrast.
- Vidljiv fokus (akcentna boja) na svim interaktivnim elementima.

## 4. Raspored i ponašanje (mobile-first)
- Projektuje se prvo za telefon (širina oko 360–400 px), pa se proširuje na tablet i računar.
- Klijent: donja navigacija sa najviše 5 stavki (Početna, Program, Ishrana ako je u paketu, Napredak, Trener). Ostalo (profil, članarina) u meniju.
- Trener: jednostavan meni; na računaru bočni meni, na telefonu skriveni meni. Bez dashboarda i grafikona na početnoj.
- Dugmad i polja dovoljno velika za prst (najmanje oko 44 px visine), osnovna veličina teksta 16 px, forme u jednoj koloni.
- Unos rezultata treninga mora da bude brz: veliki brojčani unosi, jasno koja je serija i sledeća vežba.
- Sistemski fontovi (bez spoljnih fontova), radi brzine i privatnosti.
- Bez tamne teme u MVP-u.
- Jasne poruke o greškama i praznim stanjima na srpskom (npr. „Još nema unetih treninga").
