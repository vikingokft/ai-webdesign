# Koncepció brainstorm útmutató

Az interjú befejezése után dolgozz ki N koncepció irányt (N = amit a felhasználó választott: 3, 4 vagy 5).

**A legfontosabb szabály:** Minden iránynak valóban különböző döntéseket kell hoznia több kontraszt-tengely mentén. Ugyanannak a layoutnak a színvariációi NEM különböző irányok.

---

## Mi rögzített, mi szabad

**Rögzített (brand-megkötések — minden irányra ugyanaz):**
- Brand pozicionálás, hang és CTA stratégia
- A brief horgony színei és fontjai (ha a felhasználónak vannak megtartandó márkaszínei/fontjai)
- Kerülendő színek (ha meg vannak adva)

**Szabad (minden irány maga választja):**
- Színpaletta — 7 token: primary, secondary, accent, bg, surface, text, muted
- Font-párosítás — címsor + szövegtörzs font (mindkettőnek elérhetőnek kell lennie a Google Fonts-on)
- Minden a lenti kontraszt-tengelyeken

Te vagy a designer. Minden irányhoz azt a palettát és fontokat válaszd, amelyek a legjobban megtestesítik az adott koncepció személyiségét. Ne a felhasználóval választass — minden irányt kész vizuális javaslatként mutass be.

## Kontraszt-tengelyek

Ezekkel hozz létre elkülönülő irányokat. Minden iránynak legalább 4-5 tengelyen különböznie kell:

| Tengely | Opciók |
|---------|--------|
| **Layout sűrűség** | Tágas / Kiegyensúlyozott / Sűrű |
| **Tipográfiai kezelés** | Extrém méretkontraszt / Finom hierarchia / Egy domináns méret / Nagybetűs címkék / Expresszív display-vastagságok |
| **Vastagság-játék** | Vékony + félkövér kontraszt / Minden közepes / Végig vastag / Hajszálvékony + fekete párosítás |
| **Vizuális metafora** | Editorial (magazinszerű) / Stúdió (professzionális mesterség) / Térbeli (mélység, rétegek) / Minimál (a tartalom lélegezzen) / Organikus (természetes formák, textúrák) |
| **Hero kezelés** | Teljes szélességű kép / Osztott képernyő / Tipografikus / Videó / Illusztrált |
| **Szekció-ritmus** | Egységes rács / Váltakozó elrendezések / Aszimmetrikus / Moduláris blokkok |
| **Forma-nyelv** | Éles sarkok / Lekerekített sarkok / Pirula-formák / Vegyes |
| **Árnyék-stílus** | Lapos (nincs árnyék) / Finom árnyékok / Drámai árnyékok / Egymásra lógó elemek |
| **Bizonyíték-stílus** | Statisztika-központú / Vélemény-központú / Portfólió/esettanulmány-rács / Logófal |
| **Fehér tér használat** | Bőséges (luxus érzet) / Kiegyensúlyozott (professzionális) / Feszes (információ-sűrű) |

---

## Paletta- és font-választás

Minden irányhoz komplett színpalettát és font-párosítást kell választanod. Ez designdöntés — te választod, ami a legjobban működik, a felhasználó az eredményt látja.

**Folyamat (belső — ne mutasd a felhasználónak):**
1. Fontolj meg 2-3 paletta-opciót minden irányhoz
2. Válaszd azt, amelyik a legtermészetesebben illik az irány design-személyiségéhez
3. Ugyanígy a font-párosításokkal
4. Tartsd tiszteletben a brief megkötéseit (horgony színek, kötelező fontok, kerülendő színek)

**Színpaletta — 7 token irányonként:**
- `primary` — fő márka/CTA szín
- `secondary` — támogató szín
- `accent` — kiemelő/részlet szín
- `bg` — oldal háttere
- `surface` — kártya/szekció hátterek (kicsit eltér a bg-től)
- `text` — elsődleges szövegszín
- `muted` — másodlagos szöveg, feliratok

**Font-párosítás — 2 font irányonként:**
- Címsor font — h1-h6, display szövegek
- Szövegtörzs font — bekezdések, UI szövegek
- Mindkettőnek elérhetőnek kell lennie a **Google Fonts**-on ( fonts.google.com )
- **Fontos:** a fontnak támogatnia kell a magyar ékezetes karaktereket (latin-ext subset) — a legtöbb népszerű Google Font támogatja, de ellenőrizd

**Minőségi szabályok:**
- Az irányok palettái legyenek **jól láthatóan különbözőek** — nem ugyanazok a színek kicsit eltolva
- Minden paletta érződjön NATÍVNAK az irány személyiségéhez (egy meleg organikus irány meleg földszíneket kap, egy merész modern irány erős kontrasztot)
- A font-párosítás erősítse az irány vizuális metaforáját (editorial = serif címsorok, modern = geometrikus sans stb.)
- Ha a briefben vannak horgony színek, sződd bele minden irány palettájába — de a támogató színek eltérhetnek

---

## Az irányok bemutatási formátuma

A brainstorm után mutasd be az irányokat a felhasználónak, MIELŐTT építenél. Formátum:

```
## 1. irány: [Név]

**Paletta:** [Primary név #hex] · [Secondary név #hex] · [Accent név #hex] — háttér: [#hex]
**Fontok:** [Címsor font] + [Szövegtörzs font]
**Vizuális megközelítés:** [2-3 mondat a designról. Említsd: layout stílus, hero kezelés, térköz-érzet, forma-nyelv, tipográfiai kezelés, szín-hangulat, összbenyomás]

**Miért illik a márkádhoz:** [1-2 mondat, ami az irányt a konkrét briefhez köti]
```

Minden irány komplett vizuális javaslat — paletta, fontok és layout együtt. A felhasználó a teljes csomagot választja.

Példa irányok (egy budapesti öko belsőépítész stúdióhoz — meleg, editorial, prémium):

```
## 1. irány: A csendes galéria

Paletta: Dió #8B6F47 · Grafit #3D3D3D · Meleg arany #C4956A — háttér: Krém #FAF7F2
Fontok: DM Serif Display + Jost

Bőséges fehér tér, teljes szélességű fotós hero-val. A serif címsorok
editorial tekintélyt adnak, a vékony Jost szövegtörzs levegős marad.
Krém és len hátterek meleg dió CTA-kkal — semmi vizuális zaj, csak a
munkák beszélnek magukért.

Miért illik: A portfóliód a bizonyítékod. Ez az irány teljesen azt állítja
középpontba: minden projektfotó teret kap, a meleg földszínek pedig a
természetes, átgondolt esztétikát erősítik.

## 2. irány: A műterem

Paletta: Mélyzöld #2D3B2D · Pala #4A4A4A · Réz #B87333 — háttér: Pergamen #F5F0E8
Fontok: Playfair Display + Inter

Aszimmetrikus rács egymásra lógó elemekkel — egy projektfotó kifut a
szélre, miközben a szöveg rárétegződik. A vastagabb serif címsorok
kontrasztban állnak a tiszta geometrikus szövegtörzzsel. Mélyzöld szekciók
váltakoznak a meleg pergamennel, ritmust és vizuális érdekességet teremtve.
Pirula formájú réz CTA-k adnak meleget.

Miért illik: A „műterem" keretezés azt üzeni, hogy ez egy határozott
látásmódú stúdió, nem csak egy szolgáltatás. Az egymásra rétegzett layout
és a réz kiemelések adják azt a kifinomultságot, amit a prémium
pozicionálás megkövetel.

## 3. irány: A naturalista

Paletta: Olíva #6B7F3B · Meleg agyag #A0785A · Borostyán #D4A84B — háttér: Len #F8F4EF
Fontok: Fraunces + DM Sans

Organikus szekció-formák (finom SVG hullámok a szekció-váltásoknál), meleg
olíva és borostyán kiemelések puha len alapon. Lekerekített sarkok mindenhol —
kártyák, képek, gombok. A változó optikai méretű címsor-font természetesen
vált display és szöveg-vastagság között. A statisztika-szekció nagy számokat
használ vizuális horgonyként.

Miért illik: Ez az irány az öko-tudatos identitást helyezi előtérbe — minden
vizuális döntés a természetben gyökerezik. Melegebb és közvetlenebb, mint az
1. irány, de továbbra is prémium.
```

---

## Elkerülendő buktatók

**Túl hasonló:**
- „Az 1. irány minimál, a 2. irány is minimál, csak más fonttal" — nem
- Három irány, ami ugyanazt a hero-kezelést használja — nem
- Ha csak a szín az érdemi különbség — nem

**Túl általános:**
- „Merész és modern" — ez az AI-generált weboldalak 90%-át leírja
- „Letisztult és professzionális" — semmitmondó
- „Minimalista" konkrétumok nélkül — milyen minimalizmus?

**Nem a briefben gyökerezik:**
- Sötét, komor irány egy gyerekmárkának — nem
- Korporét kék irány egy wellness cégnek — nem
- Minden iránynak hihetőnek kell lennie EHHEZ a márkához

**Paletta/font problémák:**
- Ugyanaz a paletta apró árnyalat-eltérésekkel az irányok között — minden iránynak határozottan más szín-hangulat kell
- Nem létező font — mindig ellenőrizd, hogy a font tényleg elérhető a Google Fonts-on, és támogatja a latin-ext (magyar ékezetes) karaktereket
- Horgony-megkötések figyelmen kívül hagyása — ha a briefben kötelező színek vagy fontok vannak, minden iránynak tiszteletben kell tartania

---

## iranyok.json formátum

Miután a felhasználó jóváhagyta (vagy módosította) az irányokat, írd meg ezt a fájlt:

```json
{
  "directions": [
    {
      "id": 1,
      "slug": "a-csendes-galeria",
      "name": "A csendes galéria",
      "description": "Bőséges fehér tér teljes szélességű fotós hero-val. A serif címsorok editorial tekintélyt adnak, a vékony szövegtörzs levegős marad. Krém és len hátterek meleg dió CTA-kkal.",
      "rationale": "A portfóliód a bizonyítékod. Ez az irány teljesen azt állítja középpontba.",
      "palette": {
        "primary": "#8B6F47",
        "secondary": "#3D3D3D",
        "accent": "#C4956A",
        "bg": "#FAF7F2",
        "surface": "#F0EBE3",
        "text": "#2C2C2C",
        "muted": "#8A8A8A"
      },
      "fonts": {
        "heading": { "family": "DM Serif Display", "fallback": "Georgia, serif" },
        "body": { "family": "Jost", "fallback": "system-ui, sans-serif" },
        "google_fonts_url": "https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Jost:wght@300..700&display=swap"
      },
      "contrast_axes": {
        "density": "spacious",
        "typography": "transitional-serif + humanist-sans",
        "hero": "full-bleed-image",
        "visual_metaphor": "editorial"
      }
    },
    {
      "id": 2,
      "slug": "a-muterem",
      "name": "A műterem",
      "description": "Aszimmetrikus rács egymásra lógó elemekkel. Vastagabb serif címsorok kontrasztban a tiszta geometrikus szövegtörzzsel. Mélyzöld szekciók váltakoznak meleg pergamennel.",
      "rationale": "A műterem keretezés határozott látásmódú stúdiót üzen, nem csak szolgáltatást.",
      "palette": {
        "primary": "#2D3B2D",
        "secondary": "#4A4A4A",
        "accent": "#B87333",
        "bg": "#F5F0E8",
        "surface": "#EBE5DA",
        "text": "#1A1A1A",
        "muted": "#7A7A7A"
      },
      "fonts": {
        "heading": { "family": "Playfair Display", "fallback": "Georgia, serif" },
        "body": { "family": "Inter", "fallback": "system-ui, sans-serif" },
        "google_fonts_url": "https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400..900&family=Inter:wght@300..700&display=swap"
      },
      "contrast_axes": {
        "density": "balanced",
        "typography": "display-serif + geometric-sans",
        "hero": "split-screen",
        "visual_metaphor": "studio"
      }
    }
  ],
  "total": 2
}
```

A `slug` mező a fájlnevekhez kell: `koncepcio-1-a-csendes-galeria.html`. A slug ékezet nélküli, kisbetűs, kötőjeles.

A `google_fonts_url` a kész Google Fonts embed URL — mindkét fonttal, a szükséges vastagságokkal és `display=swap` paraméterrel. A sub-agentek ezt teszik be a `<head>`-be.

---

## Irány-elnevezési konvenció

Az irányok nevei legyenek:
- Kifejezőek és megjegyezhetőek („A műterem", „A naturalista", „Meleg tekintély")
- Soha ne általánosak („A irány", „1. opció", „Minimál")
- A design-metaforát tükrözzék, ne csak a vizuális stílust
- Maximum 2-4 szó

Jó: A csendes galéria, Meleg tekintély, A műterem, Terepnapló, Műteremfény, Merész mesterség
Rossz: Minimalista, Modern, Letisztult professzionális, 1. opció, Sötét téma
