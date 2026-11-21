# 06 – Donete odluke, ograničenja i početne liste

## 1. Donete odluke
- Naziv aplikacije: **Lični trener** (privremeno).
- MVP sadrži samo pakete **Vođeno** i **Vođeno i ishrana**. Samostalni paketi, generatori i AI trener su kasnije (`08_kasnije.md`).
- Razvoj u dve etape: Etapa 1 (jezgro), Etapa 2 (ishrana).
- Članarina traje 1 kalendarski mesec; plaćanje van aplikacije, ručna evidencija (klijent, paket, iznos u RSD, datum).
- Program ima 4 nedelje treninga, počinje kad ga trener dodeli i važi koliko i članarina; zaključava se dodelom novog programa ili istekom članarine.
- Nezavršeni treninzi ostaju u istoriji kao nezavršeni; obnova članarine pokreće novi program koji trener dodeljuje.
- Zahtevi (obnova, promena paketa, promena programa, brisanje podataka) idu kroz chat; nema poseban sistem zahteva u MVP-u.
- Web aplikacija u pregledaču, mobile-first, bez PWA instalacije i offline režima. Klijent pristupa preko web adrese.
- Jedan trener, obavezna 2FA.
- Nova poruka u chatu se prikazuje samo u aplikaciji, bez emaila.
- Video-link vežbe je vidljiv direktno u prikazu treninga (K11).
- Sadržaj (vežbe, programi, planovi ishrane) trener unosi kroz administraciju kad je aplikacija spremna; tokom razvoja Claude Code koristi probne podatke koji se uklanjaju pre stvarnog korišćenja.
- Budžet minimalan; oko 10 klijenata na početku (oko 40 za godinu dana); klijenti u Srbiji; vlasnik sam održava aplikaciju.
- Tehnologije su odobrene 21.11.2026: Django + PostgreSQL, razvoj prvo lokalno; hosting se potvrđuje pred objavljivanje (vidi `09_plan_izrade.md` i `CLAUDE.md`).
- Domen: .rs (naziv se bira pred objavljivanje).

### Odluke donete uz plan (21.11.2026)
- Chat je dostupan i kad članarina istekne; deaktiviran i arhiviran nalog nema chat.
- Nedeljni izveštaj: nedelja ponedeljak–nedelja, šalje se u ponedeljak, dozvoljeno više izveštaja nedeljno.
- Odbijena registracija se briše; ista osoba može ponovo da se registruje istim emailom.
- Video-linkovi su YouTube linkovi i otvaraju se van aplikacije.
- Trener može biti prijavljen na više uređaja; klijent samo na jednom.
- PDF u chatu najviše 10 MB.
- Ukupne kalorije i makronutrijenti dnevnog plana se sabiraju iz ručno unetih vrednosti namirnica.

## 2. Početne liste (mogu da se menjaju u administraciji gde je to predviđeno)
- **Ciljevi (upitnik K7):** smanjenje masnog tkiva, izgradnja mišićne mase, povećanje snage, opšta kondicija i zdravlje, oblikovanje tela, drugo (slobodan opis).
- **Nivo iskustva:** početnik, srednji, napredni.
- **Mišićne grupe:** grudi, leđa, ramena, biceps, triceps, podlaktice, kvadriceps, zadnja loža, gluteus, listovi, trbušni mišići i core, celo telo.
- **Oprema:** bez opreme, bučice, šipka i tegovi, klupa, girja, elastične trake, vratilo, sprave u teretani, sprave za kardio.
- **Kategorije vežbi:** snaga, kardio, mobilnost, istezanje, zagrevanje, aktivacija.
- **Oznake vežbi (proširive):** HIIT, eksplozivnost, funkcionalni trening, stabilizacija, rehabilitacija.
- **Oznake planova ishrane:** visok sadržaj proteina, vegetarijanski, bez laktoze, bez glutena, jednostavna priprema. Plan ima i broj obroka i ukupne kalorije.

## 3. Šta obezbeđuje vlasnik (ne Claude Code)
- Pravne tekstove: uslovi korišćenja, politika privatnosti, saglasnost za obradu zdravstvenih podataka (pregleda ih stručno lice). Do tada koristiti jasne privremene tekstove označene kao nacrt.
- Sadržaj biblioteke: vežbe (uvoz iz fajla) i dnevni planovi ishrane. Claude Code može da predloži format fajla za uvoz i primere.
- Naziv domena, logo i konačan naziv (ako se promeni).
- Nalog kod izabranog hosting i email servisa (Claude Code vodi korak po korak).

## 4. Šta Claude Code predlaže i pita pre izrade
- Tehnologije, hosting, baza, skladište fajlova, servis za email, rezervne kopije (sa okvirnim cenama i preporukom).
- Šemu baze za celu viziju, strukturu projekta i model pristupa.
- Plan izrade po koracima koji se mogu završiti i testirati u jednoj sesiji.
- Svaku nejasnoću ili kontradikciju u dokumentima: pitati vlasnika, najviše 10 pitanja odjednom.
