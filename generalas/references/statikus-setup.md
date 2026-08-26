# Statikus projekt felállítása

Először olvasd be a `.webprojekt/brief.md` fájlt, hogy megvannak-e a konkrét színek, fontok és a projekt neve.

A projekt tudatosan egyszerű: **statikus HTML + Tailwind CSS (Play CDN) + Google Fonts.** Nincs npm, nincs build lépés, nincs keretrendszer. Minden koncepció egy önálló HTML fájl, ami böngészőben közvetlenül megnyitható.

---

## 1. lépés: Projektstruktúra

Hozd létre ezt a struktúrát a projekt gyökerében:

```
projekt/
├── index.html                     ← koncepció-navigátor (a 3. fázis végén készül)
├── koncepcio-1-[slug].html        ← a sub-agentek írják (3. fázis)
├── koncepcio-2-[slug].html
├── koncepcio-3-[slug].html
├── images/                        ← képek (redesign esetén images/redesign/)
└── .webprojekt/                  ← state, brief.md, iranyok.json, plan.md
```

Ebben a fázisban csak az `images/` mappát és a lenti közös head-sablont kell előkészítened — a koncepció-fájlokat a sub-agentek írják, az `index.html`-t pedig te, miután végeztek.

---

## 2. lépés: Közös `<head>` sablon

Minden koncepció-fájl ugyanazt a head-szerkezetet használja, csak a saját irányának értékeivel kitöltve. Ezt a sablont adod át kitöltve a sub-agenteknek (értékek az `iranyok.json`-ból):

```html
<!doctype html>
<html lang="hu">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="[rövid leírás a briefből]">
  <title>[Irány neve] — [Vállalkozás neve]</title>

  <!-- Google Fonts — az irány font-párosítása -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="[GOOGLE_FONTS_URL az iranyok.json-ból]" rel="stylesheet">

  <!-- Tailwind CSS Play CDN -->
  <script src="https://cdn.tailwindcss.com"></script>

  <!-- Brand tokenek: Tailwind config + CSS változók -->
  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: {
            'brand-primary':   'var(--color-brand-primary)',
            'brand-secondary': 'var(--color-brand-secondary)',
            'brand-accent':    'var(--color-brand-accent)',
            'brand-bg':        'var(--color-brand-bg)',
            'brand-surface':   'var(--color-brand-surface)',
            'brand-text':      'var(--color-brand-text)',
            'brand-muted':     'var(--color-brand-muted)',
          },
          fontFamily: {
            heading: 'var(--font-heading)',
            body:    'var(--font-body)',
          },
        },
      },
    };
  </script>
  <style>
    :root {
      --color-brand-primary:   [IRANY_PRIMARY];
      --color-brand-secondary: [IRANY_SECONDARY];
      --color-brand-accent:    [IRANY_ACCENT];
      --color-brand-bg:        [IRANY_BG];
      --color-brand-surface:   [IRANY_SURFACE];
      --color-brand-text:      [IRANY_TEXT];
      --color-brand-muted:     [IRANY_MUTED];
      --font-heading: '[Irány címsor fontja]', [fallback];
      --font-body:    '[Irány szövegtörzs fontja]', [fallback];
    }
    body {
      background: var(--color-brand-bg);
      color: var(--color-brand-text);
      font-family: var(--font-body);
    }
    h1, h2, h3, h4, h5, h6 {
      font-family: var(--font-heading);
    }
  </style>
</head>
<body>
  <!-- szekciók ide -->
</body>
</html>
```

**Így minden Tailwind brand-utility (`bg-brand-primary`, `font-heading`, `text-brand-muted` stb.) az adott irány értékeire oldódik fel.**

> **Token → utility megfeleltetés:**
> `--color-brand-*` → `bg-brand-*`, `text-brand-*`, `border-brand-*`, `ring-brand-*`
> `--font-*` → `font-heading`, `font-body`

> **Szín-tippek:** A `surface` legyen kicsit eltérő a `bg`-től. A `muted` legyen középtónus a másodlagos szövegekhez.

> **Itt még nincs:** Lekerekítés, árnyékok, térköz-rendszer, komponens-osztályok (`btn-primary`, `card-surface`) — ezek azután készülnek, hogy a felhasználó irányt választott. Minden prototípus-irány önállóan dönt ezekről.

> **Megjegyzés a Play CDN-ről:** A `cdn.tailwindcss.com` script prototípusokhoz való — pontosan ez a cél itt. Az éles verziónál (miután a felhasználó irányt választott) áttérünk build-elt Tailwind CSS-re.

---

## 3. lépés: Git inicializálás

```bash
git init
```

Hozz létre egy `.gitignore` fájlt:
```
.DS_Store
```

Első commit a state-fájlokkal együtt:
```bash
git add -A
git commit -m "Projekt indítása: brief és koncepció irányok"
```

---

## 4. lépés: Ellenőrzés

A 3. fázis (sub-agentek) után minden koncepció-fájlt ellenőrizz:
1. A fájl létezik: `koncepcio-[N]-[slug].html`
2. Böngészőben megnyitva rendben megjelenik (a Browser eszközzel nyisd meg `file://` útvonalon vagy egy lokális szerverrel, és ellenőrizd)

Gyakori hibák:
1. **Nem töltődnek a fontok** — ellenőrizd a Google Fonts URL-t: a család-nevek `+`-szal írandók, és kell a `display=swap`
2. **A brand-utility osztályok nem működnek** — a `tailwind.config` scriptnek a Play CDN script UTÁN kell következnie
3. **Ékezetes karakterek hibásan jelennek meg** — ellenőrizd a `<meta charset="UTF-8">` meglétét és hogy a font tartalmazza a latin-ext subsetet
