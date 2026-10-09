---
name: generalas
description: >-
  Weboldal-generálási workflow — kész briefből N különböző kezdőoldal-koncepció készítése: irány-brainstorm, statikus HTML + Tailwind projekt, párhuzamos prototípus-építés. Akkor használd, ha a felhasználó a briefből weboldal-verziókat akar készíttetni. Triggerek: "/generalas", "generáljuk le az oldalt", "készítsük el az első verziókat", "jöhetnek a prototípusok".
metadata:
  version: 1.2.0
---

# Generálás

Te egy webes architekt és fejlesztési orkesztrátor vagy. Kész briefből indulsz, és böngészhető kezdőoldal-prototípusokig jutsz: koncepció irányokat dolgozol ki, felállítod a statikus projektet, majd párhuzamos sub-agentekkel megépíted az összes irányt.

**A skill végére:** a projektmappában N különböző kezdőoldal-dizájn van, amelyeket a felhasználó az `index.html`-t böngészőben megnyitva végig tud nézni.

**Előfeltétel:** olvasd be a `.webprojekt/brief.md` fájlt. Ha nem létezik, állj meg, és mondd: „Még nincs brief — futtasd előbb a `/tervezes` (Codexben `$tervezes`) parancsot, az készíti el."

**Kérdezési szabály:** ha elérhető az `AskUserQuestion` eszköz (Claude Code), minden kérdést azzal tegyél fel, soha sima szövegként. Ha nincs ilyen eszközöd (például Codexben), kérdezz sima szövegben: egyszerre egy kérdéscsomagot, számozott válaszlehetőségekkel és a javasolt opció megjelölésével, és várd meg a választ, mielőtt továbblépsz. Ahol a lenti lépések AskUserQuestion-t említenek, ott is ez a szabály érvényes.

**Fájlútvonalak:** a `[skill-mappa]` ennek a `SKILL.md`-nek a mappája. Claude Code-ban jellemzően `.claude/skills/generalas/` vagy `~/.claude/skills/generalas/`, Codexben `.agents/skills/generalas/` vagy `~/.agents/skills/generalas/`. A referenciákat innen olvasd.

---

## Futtatókörnyezet: Claude Code vagy Codex

A skill mindkét eszközben fut. Ahol a kettő eltér, így járj el:

| Elem | Claude Code | Codex (vagy más eszköz) |
|------|-------------|-------------------------|
| Kérdezés | `AskUserQuestion` | Sima szöveg számozott opciókkal; várd meg a választ |
| Design skill | `/frontend-design` | `$frontend-design`, ha telepítve van |
| Jóváhagyási kapu (1. fázis vége) | Plan Mode + `ExitPlanMode` | A `plan.md` összefoglalója, és kifejezett „mehet” kérése. Amíg nincs meg, ne állítsd fel a projektet |
| Prototípusok (3. fázis) | Párhuzamos sub-agentek, `opus` modellel | Párhuzamos alügynökök, ha az eszköz tudja: irányonként egy, a legerősebb elérhető modellel (Codexben ezt kifejezetten kérni kell). Ha nem tudja: egymás után, irányonként külön menetben |

**Ha a frontend-design skill nincs telepítve:** szólj egyszer a felhasználónak (telepítés: a skillcsomag README-je). Ha enélkül is tovább akar menni, dolgozz a `subagent-utasitas.md` minőségi mércéje szerint.

**Ha egymás után építed a prototípusokat:** minden irány előtt olvasd újra a briefet, az adott irányt és a sub-agent sablont, és csak a saját `koncepcio-[N]-[slug].html` fájlján dolgozz. Ne vidd át az előző irány megoldásait: a cél az, hogy az irányok tényleg különbözzenek.

**Nyelv:** minden kommunikáció magyarul történik, és a generált weboldal-szövegek is magyarul készülnek (hacsak a brief mást nem mond).

---

## A workflow áttekintése

```
1. fázis: Koncepció irányok (Plan Mode)
    → .webprojekt/iranyok.json + plan.md megírása
    → Jóváhagyás (Claude Code-ban ExitPlanMode)
    ↓ JÓVÁHAGYÁS
2. fázis: Statikus projekt felállítása
    → Projektstruktúra, git init + commit
    ↓
3. fázis: N prototípus sub-agent (párhuzamosan)
    → Irányonként egy önálló HTML fájl
    → index.html koncepció-navigátor
    ↓
4. fázis: Befejezés
    → index.html megnyitása böngészőben
```

**Referencia-táblázat — az adott fázishoz érve olvasd el a fájlt:**

| Fázis | Olvasd el |
|-------|-----------|
| 1 — Irányok | `[skill-mappa]/references/koncepcio-brainstorm.md` |
| 2 — Projekt | `[skill-mappa]/references/statikus-setup.md` |
| 3 — Sub-agentek | `[skill-mappa]/references/subagent-utasitas.md` |

**Állapotkövetés:** `.webprojekt/state.json`. A `/tervezes` skill `brief_complete` fázissal adja át. A további fázisok:

| Érték | Mikor íródik | Folytatási teendő |
|-------|-------------|-------------------|
| `directions_complete` | Irányok jóváhagyva, iranyok.json megírva | Ugrás a jóváhagyási lépéshez (5. lépés) |
| `scaffold_complete` | Projekt felállítva, git commit kész | Ugrás a 3. fázisra |
| `prototypes_complete` | Minden prototípus kész, navigátor megírva | Ugrás a 4. fázisra |

Induláskor ellenőrizd a state-et — ha egy későbbi fázisnál tart, AskUserQuestion-nel ajánld fel a folytatást onnan.

---

## 1. fázis: Koncepció irányok (Plan Mode)

**Ne lépj a 2. fázisba, amíg a felhasználó jóvá nem hagyta a tervet.**

### 1. lépés: Design skill betöltése

Töltsd be a frontend-design skillt (Claude Code: `/frontend-design`, Codex: `$frontend-design`; lásd Futtatókörnyezet). Az elveit alkalmazd végig, különösen az irányok kidolgozásánál.

### 2. lépés: Az irányok számának megkérdezése

AskUserQuestion-nel kérdezd meg:

> „Hány design koncepció irányt szeretnél megnézni? A legtöbb esetben a **3** az ideális — elég változatos, de nem nyomasztó. Választhatsz **4**-et vagy **5**-öt is."

Alapértelmezés: 3.

### 3. lépés: Brainstorm

Olvasd el a `[skill-mappa]/references/koncepcio-brainstorm.md` fájlt, és dolgozz ki pontosan N irányt a brief alapján. Mutasd be őket a felhasználónak, mielőtt bármit építenél. Ha cserét vagy módosítást kér, dolgozd át.

### 4. lépés: Fájlok írása

Jóváhagyás után:

1. **`.webprojekt/iranyok.json`** — géppel olvasható irányok (formátum a koncepcio-brainstorm.md-ben)
2. **`.webprojekt/state.json`** — `{"phase": "directions_complete", "direction_count": N, "is_redesign": ..., "source_url": ...}` (az `is_redesign` és `source_url` értékét vedd át a meglévő state-ből)
3. **`.webprojekt/plan.md`** ezzel a szerkezettel:

```markdown
# Weboldal-generálási terv

## Brand brief összefoglaló
[Egy bekezdés a briefből: vállalkozás, ügyfél, CTA, megkülönböztető]

## Koncepció irányok
[N irány, mindegyikhez: név, paletta-összefoglaló, font-párosítás, leírás, indoklás]

## Mi készül el
- Statikus HTML projekt Tailwind CSS-sel
- [N] kezdőoldal-prototípus, önálló HTML fájlokként
- Git repó az első committal

## Hogyan nézd meg a prototípusokat
Jóváhagyás után nyisd meg az index.html-t a böngészőben —
onnan minden koncepcióra át tudsz kattintani:
[Lista: koncepcio-N-nev.html]
```

### 5. lépés: Jóváhagyás (ExitPlanMode)

Claude Code-ban hívd meg az ExitPlanMode-ot a terv összefoglalójával. Más eszközben (például Codexben) mutasd be a `plan.md` összefoglalóját, és kérj kifejezett jóváhagyást. Ha a felhasználó módosítást kér, frissítsd az `iranyok.json`-t és a `plan.md`-t, majd kérj újra jóváhagyást.

---

## 2. fázis: Statikus projekt felállítása

### 1. lépés: Design skill újratöltése

**Töltsd be most újra a frontend-design skillt.** Ez frissen tölti be a design elveket a projekt-felállítás és a sub-agent orkesztráció fázisaihoz. Ne hagyd ki.

### 2. lépés: A projekt felállítása

Olvasd el a `[skill-mappa]/references/statikus-setup.md` fájlt, és pontosan kövesd: projektstruktúra, közös head-sablon előkészítése, git init + első commit.

**Redesign esetén** (ellenőrizd az `is_redesign` mezőt): a képeknek már az `images/redesign/` mappában kell lenniük (a `/tervezes` töltötte le őket, manifest: `.webprojekt/homepage-images.json`). Ha a manifest hiányzik, jelezd a felhasználónak, hogy a `/tervezes` skill képletöltő lépését érdemes pótolni, de placeholder képekkel is tovább tudsz menni.

### 3. lépés: Állapot mentése

`{"phase": "scaffold_complete", ...}` — a többi mező változatlan.

---

## 3. fázis: Prototípus sub-agentek

Olvasd el a `[skill-mappa]/references/subagent-utasitas.md` fájlt. Ez tartalmazza a pontos sub-agent prompt sablont.

Indíts N sub-agentet **párhuzamosan**, irányonként egyet: Claude Code-ban mindegyik `opus` modellel, Codexben a legerősebb elérhető modellel. Ha az eszközöd nem tud párhuzamos alügynököt indítani, építsd meg az irányokat egymás után a Futtatókörnyezet szakasz szerint.

Amikor minden sub-agent végzett:

1. Ellenőrizd, hogy minden `koncepcio-[N]-[slug].html` létezik és böngészőben megjelenik. Ha egy sub-agent elbukott, csak azt az egyet indítsd újra.
2. **Írd meg az `index.html`-t** — a koncepció-navigátort, ez a felhasználó belépési pontja. Az adatokat az `iranyok.json`-ból vedd.

   Sablon-szerkezet (töltsd ki valós adatokkal):
   ```html
   <!doctype html>
   <html lang="hu">
   <head>
     <meta charset="UTF-8">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <title>Kezdőoldal koncepciók</title>
     <script src="https://cdn.tailwindcss.com"></script>
   </head>
   <body class="bg-white text-gray-900">
     <main class="max-w-2xl mx-auto px-6 py-16">
       <h1 class="text-3xl font-bold mb-2">Kezdőoldal koncepciók</h1>
       <p class="text-gray-500 mb-12">Kattints az irányokra az előnézethez. Görgesd végig mindet, mielőtt döntesz.</p>
       <div class="flex flex-col gap-4">
         <!-- Irányonként egy kártya: -->
         <a href="koncepcio-1-[slug].html" class="block p-6 border border-gray-200 rounded-xl hover:border-gray-400 transition-colors">
           <div class="text-xs font-semibold text-gray-400 uppercase tracking-wider mb-1">1. irány</div>
           <div class="text-lg font-bold mb-1">[Név]</div>
           <div class="text-gray-600 text-sm leading-relaxed">[Egymondatos leírás az iranyok.json-ból]</div>
         </a>
       </div>
     </main>
   </body>
   </html>
   ```

3. Állapot mentése: `{"phase": "prototypes_complete", ...}`

---

## 4. fázis: Befejező üzenet

```
✅ A prototípusok elkészültek.

Megtekintés:
1. Nyisd meg az index.html fájlt a böngésződben (dupla kattintás)
2. Ott minden koncepciót látsz listázva — kattints rájuk egyenként.

Mire figyelj:
Görgesd végig mindegyiket teljesen, elemzés nélkül. Csak figyeld, mit érzel.
• Melyiknél hajolsz közelebb a képernyőhöz?
• Melyik néz ki úgy, mintha a TE márkád lenne?
• Melyiket küldenéd el büszkén egy ügyfélnek?

Jegyzetelj — valahogy így:
„Az 1-es hero-ja tetszik, a 2-es tipográfiája, a 3-as színvilága"

Hogyan tovább:
Gyere vissza, és mondd el, mit szeretsz az egyes irányokból. A
visszajelzésedből megépítem a végleges kezdőoldalt, és rögzítek egy
design rendszert — így minden további oldal automatikusan egységes marad.
```
