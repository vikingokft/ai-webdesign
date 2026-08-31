---
name: deploy-mappa
description: >-
  Publikálásra szánt mappa (alapértelmezetten public/) összeállítása statikus webprojektből — csak az éles oldalhoz szükséges fájlok kerülnek bele, a munkaanyagok (jegyzetek, briefek, prototípusok, eredeti képek) kimaradnak. Akkor használd, ha a felhasználó azt mondja "/deploy-mappa", "készíts publish mappát", "válaszd szét az éles fájlokat", "deploy mappa Netlify/Vercel-hez".
---

# Deploy-mappa

Statikus webprojektből összeállítod a publikálásra szánt mappát. A cél: a hosting (Netlify, Vercel, GitHub Pages) CSAK azt kapja meg, aminek nyilvánosan elérhetőnek kell lennie — minden munkaanyag kimarad.

**Nyelv:** kommunikálj magyarul.

## Folyamat

### 1. Az éles fájlok azonosítása

- Keresd meg a belépési pontot (`index.html` vagy amit a felhasználó mond) és a hozzá tartozó aloldalakat: kövesd a HTML-fájlok közti `href` linkeket.
- Gyűjtsd ki az éles oldalak által hivatkozott ÖSSZES eszközt: `src`/`href` attribútumok (képek, CSS, JS, fontok, favicon, videók), CSS-en belüli `url(...)` hivatkozások.
- Ami NEM kell: jegyzetek, briefek, `.webprojekt/`, prototípus-/koncepció-fájlok, eredeti (optimalizálatlan) képek, README, skillek, minden, amire az éles oldalak nem hivatkoznak.
- Ha kétséges, hogy egy fájl kell-e, kérdezd meg a felhasználót (AskUserQuestion) — inkább kérdezz, mint hogy munkaanyag kerüljön ki a netre.

### 2. A mappa összeállítása

- A célmappa alapértelmezetten `public/` (ha a felhasználó mást kér, azt használd; ha már létezik, kérdezz rá).
- Git-repóban `git mv`-vel mozgass (történet megmarad), egyébként `mv`-vel.
- A mozgatott fájlok EGYMÁS KÖZTI relatív hivatkozásai változatlanok maradnak — ellenőrizd, hogy tényleg relatívak (nem `/images/...` gyökér-abszolút és nem `file://`).
- A kint maradó munkafájlokban (pl. prototípusok) frissítsd az áthelyezett eszközökre mutató útvonalakat, hogy azok is működőképesek maradjanak.

### 3. Ellenőrzés

- Indíts lokális szervert (`python3 -m http.server`, háttérben), nyisd meg a célmappa `index.html`-jét.
- Ellenőrizd böngészőben vagy scripttel: nincs törött kép (`naturalWidth === 0`), nincs 404 a network-ben, az oldalak közti linkek működnek.
- Ellenőrizd, hogy a célmappában NINCS munkaanyag (listázd ki, és nézd át a tartalmát).

### 4. Zárás

- Git-repónál: commit (+ push, ha van remote és a projektben eddig is pusholtunk).
- Mondd el a felhasználónak: mi került a mappába, mi maradt ki, és hogy a hostingnál a publish directory a célmappa neve legyen.

## Elvek

- **Soha ne publikálj munkaanyagot:** a hosting mindent kiszolgál, ami a publish-mappában van — privát repó ettől még nem véd.
- **Mozgatás > másolás:** duplikált fájl előbb-utóbb széttart; ha a felhasználó kifejezetten másolást kér, jelezd a szinkron-kockázatot.
- **Ellenőrzés nélkül nincs kész:** a mozgatás után mindig bizonyítsd böngészőből, hogy az oldal hiánytalan.
