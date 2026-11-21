# 04 – Poslovna pravila, bezbednost i podaci (MVP)

## 1. Životni ciklus klijenta
1. Registracija i potvrda emaila → **čeka odobrenje**. Trener vidi zahtev tek kad je email potvrđen.
   - Ako trener **odbije** registraciju, nalog i lični podaci se brišu (u audit logu ostaje samo zapis da je zahtev odbijen, bez ličnih podataka). Ista osoba može ponovo da se registruje istim emailom.
2. Trener odobri, dodeli paket, početak i istek članarine → **aktivan**. Pri prvoj prijavi klijent popunjava početni upitnik.
3. 3 dana pre isteka: podsetnik emailom i u aplikaciji.
4. Istek bez obnove → **istekla članarina**.
5. Trener može da **deaktivira** nalog (podaci ostaju).
6. Trener ručno **arhivira** završenu saradnju i može da je **reaktivira**.
7. Brisanje ili anonimizacija: samo ručno, po zahtevu klijenta ili odluci trenera, uz potvrdu. Nema automatskog brisanja. (Podsetnik posle 12 meseci od arhiviranja je kasnije, vidi `08_kasnije.md`.)

## 2. Članarina
- Jedna članarina traje **1 kalendarski mesec**: od datuma početka do istog datuma narednog meseca minus jedan dan (npr. 21.11.–20.12.; ako takav datum ne postoji, poslednji dan meseca, npr. 31.01.–28.02.). Aplikacija predlaže datum isteka, trener može ručno da ga promeni.
- Plaćanje je van aplikacije; trener ručno beleži uplatu: **klijent, paket, iznos (RSD), datum uplate**, opciono napomena.
- Obnovu klijent traži kroz chat; trener produžava članarinu u profilu. Isto za promenu paketa. Svaka promena ulazi u istoriju i klijent se obaveštava.
- Pristup funkcijama zavisi od paketa **i** statusa članarine (aktivna / istekla / deaktiviran / arhiviran).

## 3. Program treninga
- Sadržaj programa je raspoređen u 4 nedelje treninga. Program počinje u trenutku kad ga trener dodeli klijentu i **važi koliko i članarina** (kalendarski mesec), ne striktno 28 dana.
- Program se **zaključava** kad: (a) trener dodeli novi program, ili (b) članarina istekne bez obnove, ili (c) nalog bude deaktiviran ili arhiviran. Ako je članarina obnovljena bez prekida, stari program ostaje otvoren dok trener ne dodeli novi. Treninzi koji nisu završeni do zaključavanja dobijaju oznaku „nezavršen”.
- Klijent sam bira dane, ali mora da prati redosled treninga i ne preskače trening.
- Dodeljeni program je **verzionisan snimak**. Izmene biblioteke (uključujući deaktivaciju vežbe) ne menjaju postojeće programe. Svaka izmena dodeljenog programa od strane trenera pravi novu verziju; klijent vidi aktuelnu, istorija ostaje.
- Svaki klijent ima svoj program; izmena kod jednog ne utiče na drugog. Kopiranje je nezavisno od istorije originala.
- Nezavršeni treninzi ostaju u istoriji kao nezavršeni. Obnova članarine pokreće **novi program** koji trener dodeljuje.
- Povrede i zdravstvena ograničenja se ne analiziraju automatski; trener čita podatke iz profila i prilagođava program.

## 4. Biblioteka vežbi
- Podaci: naziv, kratak opis, primarne i sekundarne mišićne grupe, oprema, kategorija, oznake, do 3 slike (jedna podrazumevana), video-linkovi (samo odobreni), status aktivna/deaktivirana.
- Kategorije: snaga, kardio, mobilnost, istezanje, zagrevanje, aktivacija. Oznake su proširive (npr. HIIT, eksplozivnost, funkcionalni, stabilizacija, rehabilitacija).
- U nove programe ulaze samo aktivne vežbe.
- Uvoz iz CSV/Excel fajla za početno punjenje; uvezene vežbe se pregledaju pre aktiviranja.

## 5. Planovi ishrane (Etapa 2)
- Dnevni plan: obroci, namirnice (naziv, gramaža, kalorije, proteini, ugljeni hidrati, masti), ukupne kalorije i makronutrijenti, oznake (visok sadržaj proteina, vegetarijanski, bez laktoze, bez glutena, jednostavna priprema), broj obroka.
- Nutritivne vrednosti se **unose ručno** po namirnici; aplikacija ih ne računa iz gramaže. Ukupne vrednosti obroka i dana aplikacija **sabira** iz unetih vrednosti.
- Rasporedi (nedeljni/mesečni) se sastavljaju ručno iz dnevnih planova. Isti dnevni plan se ne ponavlja u istoj nedelji; ako se ponavlja, prikazuje se upozorenje, a trener može da potvrdi.
- Dodeljeni plan je verzionisan snimak, isto kao program.
- Klijent može da otvori bilo koji datum i da evidentira pridržavanje (ispoštovan / nije ispoštovan / nije evidentirano).

## 5a. Nedeljni izveštaj i napredak
- Podaci: težina, obim struka, stomaka, kukova, jedne butine, jedne nadlaktice, napomena, opcione fotografije (spreda, sa strane, otpozadi).
- Nedelja je **ponedeljak–nedelja**. Izveštaj za proteklu nedelju se očekuje u ponedeljak.
- Klijent sme da pošalje **više izveštaja** nedeljno; svaki se čuva posebno sa datumom slanja i ulazi u grafikone.
- Podsetnik (email i u aplikaciji) ponedeljkom i utorkom ako od ponedeljka tekuće nedelje nije poslat nijedan izveštaj.
- Ispravka merenja je dozvoljena uz evidenciju izmene (staro, novo, kada) i komentar trenera.
- Fotografije napretka se ne brišu automatski, privatne su i vidi ih samo klijent i trener.

## 6. Chat sa trenerom
- Tekst, fotografije do 10 MB (uz optimizaciju) i PDF. Fotografije se automatski brišu posle 7 dana uz oznaku isteka; PDF ostaje do brisanja.
- PDF najviše 10 MB.
- Bez glasovnih poruka, bez pretrage, bez videa (MVP).
- **Pristup chatu po statusu:** aktivna članarina – da; **istekla članarina – da** (da bi klijent mogao da traži obnovu); deaktiviran – ne; arhiviran – ne.
- Nove poruke se prikazuju bez ručnog osvežavanja (provera na ~10 sekundi dok je chat otvoren).

## 7. Obaveštenja
- **Klijentu:** email (potvrda emaila, reset lozinke, odobrenje naloga, novi program, podsetnik 3 dana pre isteka, nova prijava na drugom uređaju) i u aplikaciji (na početnoj strani).
- **Treneru:** u aplikaciji (brojači na početnoj strani: nove registracije, nove poruke, novi izveštaji, članarine koje ističu); email za bezbednosne događaje (nova prijava klijenta na drugom uređaju).
- Nova poruka u chatu (za klijenta i za trenera): samo u aplikaciji (oznaka i brojač), bez emaila.
- Push obaveštenja nisu u MVP-u.

## 8. Bezbednost i podaci
- Serverske sesije, bezbedni kolačići, CSRF zaštita, ograničenje pokušaja prijave, **jedan aktivan uređaj po klijentskom nalogu**, 2FA za trenera.
- Jedan aktivan uređaj: nova prijava klijenta prekida sve ostale njegove sesije. Email klijentu i treneru (i obaveštenje u aplikaciji) šalje se samo ako je prekinuta sesija bila aktivna. **Trener** može biti prijavljen na više uređaja istovremeno.
- Zdravstveni podaci i fotografije: privatni, šifrovani u prenosu i u mirovanju (na nivou baze i skladišta kod provajdera). Fotografije bez metapodataka o lokaciji (EXIF).
- Video-linkovi vežbi su YouTube linkovi i otvaraju se u novom prozoru / YouTube aplikaciji (bez ugrađenog plejera).
- Pri registraciji: prihvatanje uslova, politike privatnosti i izričita saglasnost za obradu zdravstvenih podataka. Pravne tekstove obezbeđuje vlasnik (pregleda ih stručno lice); u aplikaciji im se obezbeđuje prikaz i evidencija datuma prihvatanja.
- Audit log (od početka u bazi): prijave, izmene podataka klijenata, članarina, programa, brisanja. Za zdravstvene podatke beleži se koje polje je promenjeno, ne i vrednost.
- Klijent vidi samo svoje podatke; svaka provera pristupa se radi na serveru.
