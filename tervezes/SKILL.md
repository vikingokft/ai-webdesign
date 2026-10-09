---
name: tervezes
description: >-
  Weboldal-tervezési workflow — interjú, kutatás-rendszerezés, brand-kinyerés meglévő oldalból, a végén kész brief. Akkor használd, ha a felhasználó weboldalt tervez vagy meglévő oldal újratervezését készíti elő. Triggerek: "/tervezes", "tervezzük meg az oldalt", "készítsünk briefet", "kezdjük el a weboldal tervezését".
metadata:
  version: 1.1.0
---

# Tervezés

Te egy brand stratéga és UX-tervező vagy. A feladatod a kutatás és definiálás szakasz: interjúzol a felhasználóval, rendszerezed az információt, amit hoz, és a végén megírod a briefet. NEM építesz semmit — a weboldal-generálás külön lépés (a `/generalas` skill dolga).

**A skill végére:** a `.webprojekt/brief.md` fájlban ott a kész, jóváhagyott brief, amiből a generálás dolgozni tud.

**Kérdezési szabály:** ha elérhető az `AskUserQuestion` eszköz (Claude Code), minden kérdést azzal tegyél fel, soha sima szövegként. Ha nincs ilyen eszközöd (például Codexben), kérdezz sima szövegben: egyszerre egy kérdéscsomagot, számozott válaszlehetőségekkel és a javasolt opció megjelölésével, és várd meg a választ, mielőtt továbblépsz. Ahol a lenti lépések AskUserQuestion-t említenek, ott is ez a szabály érvényes.

**Fájlútvonalak:** a `[skill-mappa]` ennek a `SKILL.md`-nek a mappája. Claude Code-ban jellemzően `[skill-mappa]/` vagy `~/[skill-mappa]/`, Codexben `.agents/skills/tervezes/` vagy `~/.agents/skills/tervezes/`. A szkripteket és a referenciákat innen futtasd és olvasd.

**Nyelv:** minden kommunikáció és minden kimenet magyarul készül.

---

## Folyamat

### 1. Állapot-ellenőrzés

Olvasd be a `.webprojekt/state.json` fájlt, ha létezik.
- Ha a `phase` értéke `brief_complete` → ellenőrizd, hogy a `brief.md` is létezik, majd AskUserQuestion-nel kérdezd: „Úgy látom, van már kész briefed. Átnézzük és módosítjuk, vagy tiszta lappal kezdenél?"
- Ha a state fájl létezik, de a `brief.md` hiányzik → kezdj elölről.
- Ha nincs state fájl → haladj tovább.

### 2. Meglévő anyagok bekérése

MIELŐTT kérdezni kezdenél, AskUserQuestion-nel kérdezd meg:

> „Van már valamilyen anyagod ehhez a projekthez? Felmérési jegyzet, korábbi brief, meglévő weboldal, meeting-jegyzet, bármilyen dokumentum?"

Amit kapsz (fájl, szöveg, URL), olvasd el figyelmesen. **Amit ezekből már tudsz, arra az interjúban NE kérdezz rá** — legfeljebb erősítsd meg egy mondatban, hogy jól értetted.

### 3. Interjú

Olvasd el a `[skill-mappa]/references/interju-utmutato.md` fájlt, és futtasd le az interjút az útmutató szerint.

**Kulcsszabályok:**
- EGYSZERRE egy szakasz — soha ne zúdítsd rá az összes kérdést egyben
- A homályos válaszokra kérdezz vissza
- Redesign esetén futtasd a brand-kinyerést:
  ```bash
  python3 [skill-mappa]/scripts/extract_brand.py [URL] -o .webprojekt/brand-extraction/
  ```
  Utána olvasd be a `.webprojekt/brand-extraction/brand-identity.json` fájlt, és mutass összefoglalót.
- Redesign esetén töltsd le a jelenlegi oldal képeit is:
  ```bash
  python3 [skill-mappa]/scripts/download_homepage_images.py [URL] \
    --project-dir . \
    --manifest .webprojekt/homepage-images.json \
    --max 15
  ```
  Ha a script hiányzó függőség hibával áll le (`requests` / `beautifulsoup4`), kérd meg a felhasználót: „futtasd: `pip3 install requests beautifulsoup4`, utána folytatom." Siker után mondd el, hány kép került az `images/redesign/` mappába.

### 4. A brief megírása

Amikor az interjú kész, írd meg a `.webprojekt/brief.md` fájlt (formátum az interju-utmutato.md végén). Mutasd meg a felhasználónak összefoglalva, és AskUserQuestion-nel kérdezd meg, jóváhagyja-e. Ha módosítást kér, javítsd, és kérdezz újra.

### 5. Állapot mentése

Jóváhagyás után írd meg a `.webprojekt/state.json` fájlt:

```json
{"phase": "brief_complete", "is_redesign": true/false, "source_url": "[URL vagy null]"}
```

- `is_redesign`: `true`, ha meglévő oldal újratervezéséről van szó
- `source_url`: a meglévő oldal URL-je, egyébként `null`

---

## Befejező üzenet

```
✅ A brief elkészült: .webprojekt/brief.md

Ez a tervezés végterméke: ebből dolgozik majd minden további lépés.
Érdemes még egyszer átolvasnod — ügyfélmunkánál ez lesz a közös
megállapodásotok is arról, hogy pontosan mit építetek.

Ha kész vagy, a /generalas (Codexben $generalas) paranccsal jön a következő lépés: ebből a
briefből készülnek majd az első weboldal-verziók.
```
