# AI Webdesign — skillek Claude Code-hoz és Codexhez

A Vikingo AI webdesign kurzus skilljei. Mindegyik egy önálló munkafolyamat, ami Claude Code-ban és Codexben is használható — együtt egy teljes weboldal-készítési ívet fednek le a tervezéstől a keresőoptimalizálásig.

| Skill | Mit csinál | Indítás (Claude Code / Codex) |
|---|---|---|
| **tervezes** | Kutatás és definiálás: interjú, meglévő oldal brand-kinyerése (színek, fontok, logó), a végén kész brief (`.webprojekt/brief.md`) | `/tervezes` / `$tervezes` |
| **generalas** | A briefből N különböző kezdőoldal-koncepció: irány-brainstorm, statikus HTML + Tailwind projekt, párhuzamos prototípus-építés | `/generalas` / `$generalas` |
| **deploy-mappa** | Publikálásra szánt mappa (public/) összeállítása: csak az éles fájlok kerülnek ki, a munkaanyagok nem | `/deploy-mappa` / `$deploy-mappa` |
| **vikingo-seo-skill** | Elkészült oldal SEO + GEO + AEO alapozása: meta-tagek, Open Graph, schema.org, sitemap, robots.txt — gépi ellenőrzéssel | `/vikingo-seo-skill` / `$vikingo-seo-skill` |

## Telepítés — Claude Code

**Minden skill, minden projektedhez** (felhasználói szint):

```bash
git clone https://github.com/vikingokft/ai-webdesign.git /tmp/ai-webdesign
cp -R /tmp/ai-webdesign/tervezes /tmp/ai-webdesign/generalas /tmp/ai-webdesign/deploy-mappa /tmp/ai-webdesign/vikingo-seo-skill ~/.claude/skills/
rm -rf /tmp/ai-webdesign
```

**Csak egy projekthez** (projekt-szint): ugyanez, csak a célmappa a projekted `.claude/skills/` mappája. Így a skill a projekt repójával együtt utazik, és aki klónozza, automatikusan megkapja.

Telepítés után új Claude Code munkamenetben a skillek `/névvel` hívhatók, vagy természetes nyelven is aktiválódnak („tervezzük meg az oldalt", „optimalizáld keresőre").

## Telepítés — Codex

Ugyanazok a skillek, csak más mappába kerülnek:

```bash
git clone https://github.com/vikingokft/ai-webdesign.git /tmp/ai-webdesign
mkdir -p ~/.agents/skills
cp -R /tmp/ai-webdesign/tervezes /tmp/ai-webdesign/generalas /tmp/ai-webdesign/deploy-mappa /tmp/ai-webdesign/vikingo-seo-skill ~/.agents/skills/
rm -rf /tmp/ai-webdesign
```

Csak egy projekthez: a célmappa a projekted `.agents/skills/` mappája. Telepítés után indítsd újra a Codexet. A skillek `$névvel` hívhatók (például `$tervezes`), a `/skills` paranccsal listázhatók, vagy természetes nyelven is aktiválódnak.

**Különbségek Codexben:**
- A kérdéseket a skill sima szövegben, számozott opciókkal teszi fel (a Claude Code-os kérdés-ablak helyett).
- A `/generalas` által használt **frontend-design** skill az Anthropic Claude Code-pluginja. Codexben ezt külön kell bemásolni: a [plugin repójából](https://github.com/anthropics/claude-code/tree/main/plugins/frontend-design/skills/frontend-design) a `frontend-design` mappát tedd a `~/.agents/skills/` alá. Enélkül is lefut a generálás, de a design-réteg gyengébb lesz.
- A generálás párhuzamos alügynökökkel építi a koncepciókat, ha a Codex-verziód ezt engedi. Ha nem, egymás után készülnek el (lassabb, de ugyanaz az eredmény).

## A javasolt sorrend

1. `/tervezes` (Codexben `$tervezes`) — interjú és brief (ügyfélmunkánál ez a közös megállapodás is)
2. `/generalas` (`$generalas`) — koncepció-irányok és böngészhető prototípusok a briefből
3. Irányválasztás, finomítás, aloldalak — a kurzus leckéi szerint
4. `/deploy-mappa` — élesítés előtt: az éles fájlok szétválasztása a munkaanyagoktól
5. `/vikingo-seo-skill` — amikor az oldal kész és éles domainen fut

## Követelmények

- [Claude Code](https://claude.com/claude-code) vagy [Codex](https://developers.openai.com/codex)
- Python 3 a segédszkriptekhez; a `tervezes` brand-kinyerőjéhez: `pip3 install requests beautifulsoup4`

---

Vikingo Kft. · a skillek a kurzussal együtt frissülnek
