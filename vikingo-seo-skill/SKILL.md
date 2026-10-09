---
name: vikingo-seo-skill
description: Elkészült weboldal SEO + GEO + AEO alapozása — nem audit-riportot ír, hanem elvégzi a belépőszintű beállításokat a kódban (title, meta description, Open Graph, favicon, schema.org, sitemap, robots.txt, alt szövegek, címsor-hierarchia), gépi ellenőrzéssel bizonyítja, hogy kész, és javaslatlistát ad arról, ami döntést vagy tartalmat igényel. Akkor használd, ha a felhasználó azt mondja "/vikingo-seo-skill", "optimalizáld az oldalt keresőre", "csináld meg a SEO alapokat", "készítsd fel az oldalt a Google-re és az AI-keresőkre", vagy egy weboldal-projekt elkészülte után a kereshetőség beállítását kéri.
metadata:
  version: 1.3.0
  utolso-frissites: 2026-08-14
---

# Vikingo SEO skill

Elkészült (statikus vagy egyszerű) weboldalon elvégzed a belépőszintű kereső- és AI-optimalizálást. A cél nem az első helyezés, hanem hogy az alapok hibátlanok legyenek: a keresők és az AI-motorok pontosan értsék, kié az oldal, miről szól, hol és mit kínál.

**Nyelv:** kommunikálj magyarul; a meta-szövegek az oldal nyelvén készülnek.

**Elv:** amit egyértelműen jó megcsinálni, azt CSINÁLD MEG; amihez döntés, új tartalom vagy külső lépés kell, az a JAVASLATOK közé megy. Ne írj hosszú audit-riportot: a végtermék a módosított kód + a zöld ellenőrzés + egy tömör összefoglaló.

**Idempotencia:** a skill többszöri futtatásra biztonságos — meglévő taget frissíts, soha ne duplikálj. Ami már jó, ahhoz ne nyúlj.

## Frissesség-védelem (a folyamat előtt, minden futáskor)

Hasonlítsd össze a mai dátumot a fenti `utolso-frissites` értékkel. **Ha több mint 3 hónap telt el**, a feltérképezés ELŐTT futtass egy rövid webes keresést: változtak-e az alapszintű SEO/GEO/AEO best practice-ek (pl. schema-típusok, AI-crawler szabályok mint a robots.txt AI-bot direktívák, meta-tag ajánlások, új kötelező elemek). Amit találsz:

- ha a lecke-szintű alapokat érinti, alkalmazd a munkában, és jelezd az összefoglalóban, hogy mi változott a skill megírása óta
- ajánld fel a felhasználónak, hogy frissíted a skillt (SKILL.md + referenciák + `utolso-frissites` dátum), hogy a következő futás már naprakészen induljon

Ha 3 hónapon belül vagy, hagyd ki ezt a lépést, ne keress fölöslegesen.

## Folyamat

### 1. Feltérképezés

- Azonosítsd az éles oldalakat (belépési pont + belső linkek), és olvasd be őket.
- Gyűjtsd össze a vállalkozás tényeit magukból az oldalakból és a projekt munkaanyagaiból (pl. brief, ha van): név, tevékenység, cím, telefon, e-mail, nyitvatartás, közösségi profilok, árak.
- Futtasd le ELŐSZÖR az ellenőrző szkriptet, hogy pontosan lásd, mi hiányzik (ez a kiinduló állapot, az összefoglalóban hivatkozhatsz rá):
  ```bash
  python3 [skill-mappa]/scripts/ellenorzes.py [oldalak mappája] --domain [domain, ha van]
  ```
- Kérdezd meg (AskUserQuestion, ha elérhető, egyébként sima szövegben; EGY körben, max 3 kérdés), ami hiányzik és kell:
  - **Végleges domain** (canonical, sitemap és og:url ehhez kötött — ha még nincs, a domain-függő elemeket jelöld TODO-kommenttel és vedd fel a javaslatok közé)
  - Hiányzó vállalkozás-adat, ha az oldalakból nem derült ki

### 2. Amit elvégzel (minden oldalon)

- **Title:** egyedi, ~50-60 karakter, kulcsszó + márkanév szerkezet. Ha jó, hagyd.
- **Meta description:** egyedi, ~150-160 karakter, az oldal nyelvén, cselekvésre hívó zárással.
- **Open Graph:** og:title, og:description, og:image (a legjobb meglévő fotó, lehetőleg fekvő), og:url (domain-függő), og:type, og:locale. Twitter card: summary_large_image.
- **Favicon:** ha nincs, készíts egyszerűt a márka színeivel (SVG vagy a monogram), és kösd be.
- **Canonical tag** minden oldalra (domain-függő).
- **Schema.org JSON-LD:** olvasd be a `references/schema-sablonok.md` fájlt, és abból dolgozz — a vállalkozás típusához illő entitás (altípus-választó táblázat a referenciában), a valós adatokkal kitöltve. Aloldalakon kiegészítő típus, ha indokolt (Person a Rólam oldalon, FAQPage ha van látható GYIK).
- **Címsor-hierarchia:** oldalanként pontosan egy H1; kilógó szintek javítása.
- **Alt szövegek:** hiányzók pótlása leíró, kulcsszó-releváns szöveggel; díszítő elemeknél üres alt.
- **`lang` attribútum, viewport** ellenőrzése.
- **Képek:** hajtás alatti képekre `loading="lazy"`; kirívóan nagy fájlok jelzése.
- **sitemap.xml + robots.txt** létrehozása (domain-függő; a robots.txt hivatkozza a sitemapet).

### 3. Gépi ellenőrzés — enélkül nincs kész

Futtasd újra az ellenőrző szkriptet:

```bash
python3 [skill-mappa]/scripts/ellenorzes.py [oldalak mappája] --domain [domain, ha van]
```

**Addig javíts és futtasd újra, amíg minden HIBA el nem tűnik.** (A FIGYELEM szintű jelzéseket mérlegeld: javítsd, vagy indokold az összefoglalóban.) Ezen felül:

- Lokális szerver + böngésző: az oldalak változatlanul jól jelennek meg, semmi nem tört el.
- Git-repónál: commit (+ push, ha a projektben szokás).

### 4. Összefoglaló + javaslatok

Zárásként add át tömören:

**Elvégezve:** felsorolás, mi került be melyik oldalra + az ellenőrző szkript kiinduló és záró eredménye (hány hiba volt, mennyi maradt: 0).

**Javaslatok** (ezekről a felhasználó dönt, ne csináld meg kérdés nélkül):
- GYIK-szekció vagy -oldal a gyakori vevői kérdésekkel + FAQ schema (a legjobb AEO-lépés)
- Saját, márkázott domain, ha még teszt-címen fut az oldal
- Google Search Console: sitemap beküldése; Google Business Profile helyi vállalkozásnál. (Az ellenőrző szkript FIGYELEM szinten jelzi, ha nem talál GSC-hitelesítési nyomot — meta tag vagy google*.html — az oldalban; a hiánya nem hiba, mert a hitelesítés DNS-sel vagy hosting-integrációval is történhetett, ami a kódban nem látszik.)
- Kérdés-formátumú címsorok / tömör válasz-bekezdések, ahol a tartalom kínálja
- Élesített oldalnál: Google Rich Results Test a schema ellenőrzésére, Core Web Vitals méréshez pagespeed.web.dev

## Ne csináld

- Ne írd át a látható szövegeket a felhasználó engedélye nélkül (a meta-tagek nem láthatók, azok szabadon írhatók)
- Semmi kulcsszó-halmozás, rejtett szöveg vagy egyéb trükk — csak tiszta, a tartalommal egyező jelek
- A schema-ba CSAK az oldalon láthatóan szereplő adat kerülhet
- Ne ígérj helyezést — az elvárás-kezelést mondd ki (lásd lent)

## Elvárás-kezelés (mondd is ki a felhasználónak)

Ez belépőszint: attól, hogy az alapok hibátlanok, az oldal még nem lesz első a Google-ben, és az AI-válaszokba sem garantált a bekerülés. Az alapok azt biztosítják, hogy amikor a kereső vagy az AI az oldalhoz nyúl, mindent pontosan értsen — a helyezés a tartalmon, az említéseken és az időn múlik.
