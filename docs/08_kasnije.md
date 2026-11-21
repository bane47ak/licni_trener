# 08 – Šta se NE gradi u MVP-u, ali arhitektura mora da ga predvidi

Ništa iz ovog fajla se ne implementira u Etapama 1 i 2 bez izričitog zahteva vlasnika. Šema baze, uloge, paketi i pristup podacima treba da se dizajniraju tako da se ovo doda bez prepravljanja.

## 1. Samostalni paketi
- **Samostalno:** klijent bira kriterijume, generator pravi trening program, bez plana ishrane i bez chata sa trenerom.
- **Samostalno i ishrana:** sve iz Samostalno + izbor kriterijuma ishrane i automatski mesečni raspored.
- Jedno generisanje treninga i jedno rasporeda ishrane po periodu članarine (1 mesec). Posle generisanja kriterijumi su zaključani do sledećeg perioda; trener može da otključa.
- Program se dodeljuje bez odobrenja trenera. Klijent vidi upozorenje da sam vodi računa o zdravstvenim ograničenjima.
- Nove klijentske strane: izbor kriterijuma za trening i za ishranu.

## 2. Generator treninga
- Za 4 nedelje, samo iz aktivnih vežbi biblioteke; nikada ne izmišlja vežbe niti koristi opremu koju klijent nema. Određuje serije, ponavljanja, pauze, opterećenje i trajanje.
- **Kriterijumi:** cilj, broj treninga nedeljno, nivo iskustva, oprema (ne čuva se trajno u profilu), trajanje treninga (predlog: 20, 30, 45, 60, 90 min), mišićne grupe, tip treninga (predlog: jedan izbor – snaga, kardio ili kombinovano; zagrevanje i istezanje dodaju se automatski).
- U vođenim paketima generator pravi početni program, a trener pregleda, menja, potvrđuje i dodeljuje. Ako nema dovoljno vežbi: jasna poruka, bez nepotpunog programa.
- **Polazni predlog algoritma** (trener pregleda): podela po broju treninga (2 → celo telo A/B; 3 → celo telo ili gornji/donji/celo telo; 4 → gornji/donji; 5–6 → podela po mišićnim grupama); struktura: zagrevanje → glavni deo → opciono kardio/core → istezanje; parametri po cilju (snaga 3–5 serija, 3–6 ponavljanja, pauza 2–3 min; mišićna masa 3–4 serije, 8–12 ponavljanja, pauza 60–90 s; mršavljenje/kondicija 2–3 serije, 12–15 ponavljanja, pauza 30–60 s uz kardio); nivo iskustva menja zapreminu i složenost; postepeno napredovanje kroz 4 nedelje, lakša četvrta nedelja; raznolikost bez ponavljanja iste vežbe unutar nedelje gde ima alternative.

## 3. Generator ishrane
- Klijent bira kalorijski raspon i filtere (visok sadržaj proteina, vegetarijanski, bez laktoze, bez glutena, jednostavna priprema, broj obroka). Predlog kalorijskih raspona za početak: 3–4 raspona (npr. 1400–1700, 1700–2000, 2000–2400, 2400–2800 kcal).
- Bira gotove dnevne planove iz biblioteke koji imaju sve izabrane oznake i pravi mesečni raspored. Isti dnevni plan se ne ponavlja u istoj nedelji; ako je neizbežno, upozorenje, a trener može da odobri.
- Ako nema dovoljno planova: upozorenje, bez nepotpunog rasporeda ili rasporeda sa nedozvoljenim ponavljanjem. Samostalni paket: klijent ne može da nastavi dok se biblioteka ne dopuni. Vođeni paket: trener dopunjuje.
- Posledica: za svaki ponuđeni raspon (uz filtere) treba najmanje 7 različitih dnevnih planova.

## 4. AI trener
- Dostupan u sva četiri paketa. Samo tekst, na srpskom. Odgovara samo na pitanje klijenta; ne šalje samostalne poruke, upozorenja ni motivaciju.
- Koristi samo podatke tog klijenta koje backend izabere da prosledi (lični podaci relevantni za pitanje, ciljevi, paket, aktivni program, plan ishrane, istorija treninga, merenja, relevantni zdravstveni podaci, prethodni razgovori). Nikada podatke drugih klijenata.
- Može: objašnjavati vežbe i tehniku, plan ishrane i makronutrijente, predlagati zamenu vežbe ili namirnice uz približnu procenu, objašnjavati napredak. Demonstracioni video-linkovi prvo iz odobrenih linkova biblioteke, pa pretraga interneta; pronađeni link ne postaje deo biblioteke bez odobrenja trenera.
- Ne sme: dijagnoze, tvrdnje o lečenju, garancije rezultata, samostalne izmene programa ili ishrane, ignorisanje alergija i namirnica koje klijent izbegava, pristup tuđim podacima. Kod bola ili povrede upućuje klijenta treneru ili zdravstvenom stručnjaku.
- Zamena vežbe ide preko zahteva treneru; ako trener odobri, program dobija novu verziju.
- Podešavanja iz admin panela: stil, ton, pravila za trening i ishranu, internet pretraga, bezbednosna ograničenja.
- Tehnički: poziv samo sa servera, ključ nikad ne ide klijentu, poslednjih 15 razmena u kontekstu, stariji se sažimaju; početni limiti (ulaz oko 10.000, odgovor oko 1.500 tokena) su predlog. Pre izbora provajdera uporediti kvalitet na srpskom, cenu i način čuvanja podataka; minimizovati osetljive podatke (npr. bez imena i prezimena).

## 5. Ostalo kasnije
- **Sistem zahteva:** formalni zahtevi klijenata (promena treninga/vežbe, ishrane, paketa, obnova, brisanje) sa statusima i odobravanjem; admin strane za listu i odluku.
- **Grupne poruke** (slanje i upravljanje).
- **Poređenje fotografija** napretka kroz vreme.
- **Push obaveštenja** (uz dozvolu klijenta).
- **Video u chatu** (do 100 MB, najviše 2 minuta; briše se posle 7 dana).
- **Podsetnik posle 12 meseci** od arhiviranja za potvrdu brisanja ili anonimizacije.
- **Admin strane:** opšta podešavanja aplikacije, upravljanje paketima i mogućnostima, podešavanja obaveštenja, pregled bezbednosnih aktivnosti i evidencije promena (podaci se beleže od početka).
- **Van dometa za sada:** offline režim i PWA instalacija, više trenera, izvoz u Excel i PDF, glasovne poruke, pretraga chata, AI unos biblioteke, automatsko prepoznavanje povreda i zdravstveno filtriranje vežbi, automatizovana naplata, složena pravila bodovanja, napredni dashboardi.
