# AI Webdesign — Claude Code skillek

A Vikingo AI webdesign kurzus skilljei. Mindegyik egy önálló, Claude Code-ban használható munkafolyamat — együtt egy teljes weboldal-készítési ívet fednek le a tervezéstől a keresőoptimalizálásig.

| Skill | Mit csinál | Indítás |
|---|---|---|
| **tervezes** | Kutatás és definiálás: interjú, meglévő oldal brand-kinyerése (színek, fontok, logó), a végén kész brief (`.webprojekt/brief.md`) | `/tervezes` |
| **generalas** | A briefből N különböző kezdőoldal-koncepció: irány-brainstorm, statikus HTML + Tailwind projekt, párhuzamos prototípus-építés | `/generalas` |
| **vikingo-seo-skill** | Elkészült oldal SEO + GEO + AEO alapozása: meta-tagek, Open Graph, schema.org, sitemap, robots.txt — gépi ellenőrzéssel | `/vikingo-seo-skill` |

## Telepítés

**Minden skill, minden projektedhez** (felhasználói szint):

```bash
git clone https://github.com/vikingokft/ai-webdesign.git /tmp/ai-webdesign
cp -R /tmp/ai-webdesign/tervezes /tmp/ai-webdesign/generalas /tmp/ai-webdesign/vikingo-seo-skill ~/.claude/skills/
rm -rf /tmp/ai-webdesign
```

**Csak egy projekthez** (projekt-szint): ugyanez, csak a célmappa a projekted `.claude/skills/` mappája. Így a skill a projekt repójával együtt utazik, és aki klónozza, automatikusan megkapja.

Telepítés után új Claude Code munkamenetben a skillek `/névvel` hívhatók, vagy természetes nyelven is aktiválódnak („tervezzük meg az oldalt", „optimalizáld keresőre").

## A javasolt sorrend

1. `/tervezes` — interjú és brief (ügyfélmunkánál ez a közös megállapodás is)
2. `/generalas` — koncepció-irányok és böngészhető prototípusok a briefből
3. Irányválasztás, finomítás, aloldalak — a kurzus leckéi szerint
4. `/vikingo-seo-skill` — amikor az oldal kész és éles domainen fut

## Követelmények

- [Claude Code](https://claude.com/claude-code)
- Python 3 a segédszkriptekhez; a `tervezes` brand-kinyerőjéhez: `pip3 install requests beautifulsoup4`

---

Vikingo Kft. · a skillek a kurzussal együtt frissülnek
