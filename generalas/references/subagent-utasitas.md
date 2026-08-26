# Sub-agent utasítás

Minden sub-agent egy komplett kezdőoldal-prototípust épít. A cél a **felhasználó lenyűgözése** — nem egy tiszta sablon, hanem az, hogy azt mondja: „ez az ÉN oldalam!"

**Kritikus:** Minden sub-agent CSAK a saját fájljába írhat. Ne nyúlj más irányok fájljaihoz vagy az index.html-hez.

---

## Sub-agent prompt sablon

Ezt a promptot használd minden sub-agenthez. Indítás előtt töltsd ki a helyőrzőket.

---

```
ELŐSZÖR: Futtasd a /frontend-design parancsot a frontend design skill betöltéséhez.

UTÁNA: Olvasd el a .webprojekt/brief.md fájlt a teljes brand briefért.
ÉS: Olvasd el a .webprojekt/iranyok.json fájlt — KIZÁRÓLAG a(z) [N]. irányt ("[Irány neve]") valósítsd meg.

Ellenőrizd, hogy redesign-e: olvasd el a .webprojekt/state.json fájlt. Ha az is_redesign értéke true, olvasd el a .webprojekt/homepage-images.json fájlt a jelenlegi oldalról letöltött képekért. A képek az images/redesign/fajlnev.jpg útvonalon érhetők el — a manifestből a path mezőt használd. A valódi képeket részesítsd előnyben a placeholderekkel szemben.

## A küldetésed

Építs kezdőoldal-prototípust a(z) [N]. irányhoz ("[Irány neve]"), amiért egy ügyfél 10 millió forintot fizetne. Nem sablont. Nem beszínezett drótvázat. KÉSZ érzetű dizájnt, személyiséggel, mesterségbeli tudással és apró örömökkel.

[Irány leírása — másold be az iranyok.json-ból]

## A minőségi mérce

Egy prémium ügynökség senior designere vagy. A brief.md megmondja, ki az ügyfél — kutyakiképző, ügyvédi iroda, belsőépítész, SaaS startup. A dolgod, hogy a kidolgozottság szintjét az árcédulához igazítsd (egyedi, csúcskategóriás build), miközben a TÓNUST a márkához igazítod.

Egy játékos márka játékos easter eggeket kap. Egy komoly márka kifinomult visszafogottságot. Mindkettő ugyanazt a megszállott kidolgozottságot. Olvasd el figyelmesen a briefet, és aszerint tervezz.

### Alapelvek (MINDEN márkára érvényesek)

**1. Visszatérő vizuális motívum** — egy egyedi elem, ami a márka vizuális védjegyévé válik az oldalon. Megjelenik a navigációban, szekció-átmenetekben, kártya-részletekben, hátterekben, CTA-kban, footerben — legalább 5 helyen. Hogy MI legyen, a márkától függ: geometrikus minta, SVG vonalkezelés, illusztrált elem, tipográfiai eszköz, architektonikus forma. A márka identitásából vezesd le, ne egy általános ikonkönyvtárból.

**2. Szándékos motion design** — az animációk érződjenek megkomponáltnak, ne alapértelmezettnek. A mozgás tónusa illeszkedjen a márkához: az energikus márkák rugós görbéket és pattogást kapnak; a kifinomultak lassú átmeneteket és finom felfedéseket. De MINDEN márka kap:
- Lépcsőzetes hero-belépést (az elemek sorban érkeznek, változó időzítéssel)
- Scroll-reveal rendszert többféle animáció-típussal, nem egységes fade-up-ot mindenre
- Statisztika-számlálókat vagy felfedéseket, amik jutalmazzák a görgetést (requestAnimationFrame easinggel, írógép-effekt vagy fokozatos megjelenés)
- Hover-interakciókat átgondolt görbékkel (túllendülő cubic-bezier a játékos márkáknak, sima ease-out a komolyaknak)
- Görgetésre reagáló navigációt (zsugorodás, blur háttér, átlátszóság-váltás)
- Legalább egy önállóan mozgó elemet (finom lebegés, forgás vagy pulzálás — a márka energiájához kalibrálva)

**3. Layout tudatos feszültséggel** — törd meg a rácsot, ahol az a dizájnt szolgálja:
- Aszimmetrikus oszlop-osztások (ne minden 50/50)
- Lépcsőzetesen eltolt kártya-csoportok
- Legalább egy elem, ami átlóg egy határon (szekción átfolyó kép, fotóra rétegzett szöveg, konténeren kívüli dekoratív elem)
- Szekció-elválasztók, amik nem egyenes vonalak — SVG ívek, szögek vagy formázott átmenetek
- Teljes szélességű pillanatok, amik megtörik a tartalom-szélesség ritmusát

**4. A tipográfia mint design-eszköz** — nem csak méret-hierarchia:
- Tudatos vastagság-kontraszt (vékony vs. félkövér, vagy vastag vs. hajszálvékony — válassz stratégiát)
- Kiemelések a címsorokon belül (dőlt, szín- vagy vastagság-váltás kulcsszavakon)
- Negatív betűköz a nagy display-szövegeken
- Mikro-címkék széles betűközzel szekció-felcímként
- Folyékony méretezés clamp()-pel — ne csak töréspontos ugrások

**5. Mikro-részletek, amik a mesterséget jelzik** — ezek különböztetik meg az egyedit a sablontól. Válaszd azokat, amik illenek a márka tónusához:
- Egyedi SVG címsor-aláhúzások vagy kiemelő jelek (hullámos az organikus márkáknak, geometrikus a precízeknek, minimál vonal a komolyaknak)
- Nem szabványos kép-konténerek (organikus border-radius a meleg márkáknak, éles maszkok vagy szögletes vágások a merészeknek, finoman lekerekített a tisztáknak)
- Dekoratív SVG útvonalak vagy vonalak, amik összekötik a szekciókat vagy vezetik a szemet
- Háttér-textúra nagyon alacsony átlátszósággal (zaj, szemcse, finom minta — a márka energiájához illően)
- Szín- vagy részlet-variációk elemenként (váltakozó kiemelő színek, pozíció-specifikus kezelések)
- Átgondolt mobil menü (nem generikus hamburger → lenyíló)
- Footer megkomponált zárással (tagline + inline SVG jel)

**6. Vizuális ritmus a szekciók között** — az oldalnak legyen lélegzési mintája:
- Tudatosan váltakozó háttérszínek (ne minden fehér vagy minden krém)
- Legalább egy „invertált" szekció (sötét háttér világos szöveggel, vagy márkaszín-háttér) a monotónia megtörésére
- Szekció-átmenetek, amik áramlást teremtenek, nem éles vágásokat

### A tónus kalibrálása

Olvasd el a brand briefet. A design-energiádat igazítsd az ügyfélhez:

| Márka-személyiség | Mozgás-energia | Dekoratív stílus | Layout-megközelítés |
|---|---|---|---|
| Játékos / meleg | Rugós görbék, pattogás, lebegés | Illusztrált elemek, organikus formák, kézzel rajzolt érzet | Tört rácsok, megdöntött kártyák, elszórt díszítések |
| Kifinomult / luxus | Lassú átmenetek, finom parallax | Minimál vonalmunka, geometrikus precizitás | Bőséges fehér tér, editorial aszimmetria |
| Merész / modern | Pattanós átmenetek, skálázás | Erős geometria, magas kontraszt | Sűrű rácsok, egymásra rétegzés, drámai full-bleed |
| Professzionális / bizalom | Kimért felfedések, sima áttűnések | Tiszta vonalak, strukturált minták | Rendezett rácsok, világos hierarchia, visszafogott törések |

Ez a táblázat kiindulópont, nem ketrec. Keverd a megközelítéseket. Egy luxusmárkának lehet EGY játékos easter eggje. Egy játékos márkának lehet EGY drámaian visszafogott pillanata. A dizájnon belüli kontraszt teszi megterveztté, nem generálttá.

## Kimeneti fájl

KIZÁRÓLAG ezt az egy fájlt hozd létre:
- koncepcio-[N]-[slug].html — önálló, komplett HTML oldal

Minden egy fájlban van: HTML szerkezet, a <head>-ben a stílus-tokenek, inline <style> blokkok az egyedi CSS-hez (animációk, motívumok), és <script> blokk az interakciókhoz a </body> előtt. Nincs külső CSS/JS fájl.

## A <head> sablon

A fájl ezzel a kitöltött head-del kezdődjön (az értékeket a fő szál adja, a te irányod palettájával és fontjaival):

[IDE MÁSOLD a statikus-setup.md 2. lépésének kitöltött head-sablonját — Google Fonts link, Tailwind Play CDN, tailwind.config, :root CSS változók]

A head után minden Tailwind brand-utility (bg-brand-primary, font-heading stb.) automatikusan a TE irányod értékeire oldódik fel. 

## Stílusozás

A brand-színek és fontok Tailwind utility-ként érhetők el:
- Színek: bg-brand-primary, text-brand-secondary, bg-brand-accent, bg-brand-bg, bg-brand-surface, text-brand-text, text-brand-muted (és border-/ring- változatok)
- Fontok: font-heading, font-body

Az alap tokeneken túl is menj bátran:
- Árnyalatok átlátszósággal: bg-brand-primary/10, text-brand-accent/60
- Színátmenetek: bg-gradient-to-b from-brand-primary/5 to-transparent
- Keverés semleges színekkel: bg-white, bg-black, text-white a kontraszt-szekciókhoz
- Tetszőleges értékek, ha a Tailwind skálája nem elég: text-[96px], tracking-[-0.03em], leading-[0.92]

Az egyedi animációkat és motívum-CSS-t <style> blokkban írd meg a head-ben vagy közvetlenül utána.

## Tartalmi szabályok

- **Valódi tartalom elsőbbsége:** ami a briefben konkrétan szerepel (árak, szolgáltatások, vélemények, elérhetőségek, statisztikák), azt SZÓ SZERINT használd — kitalált tartalmat csak oda írj, ahol a brief nem ad valódit
- MINDEN tartalom a brief.md márkahangjához illeszkedjen, és MAGYARUL készüljön (hacsak a brief más nyelvet nem ír elő)
- **Alapértelmezetten magázódj** a weboldal szövegeiben — tegeződj csak akkor, ha a brief márkahangja kifejezetten ezt kéri
- **Ne használj em dash (—) karaktert** a weboldal szövegeiben — tagolj vesszővel, kettősponttal vagy zárójellel
- SEMMI lorem ipsum — írj valódinak hangzó címsorokat, szövegeket, CTA-kat, véleményeket
- Vélemények: ha a brief tartalmaz valódiakat, azokat használd; ha nem, írj 2-3 hihető idézetet az ügyfél hangján, névvel és kontextussal
- Statisztikák: a brief valós számait használd; csak akkor találj ki hihetőt, ha nincs valódi
- Ügyelj a helyes magyar tipográfiára: „idézőjelek", nem törő szóközök a mértékegységeknél

## Kötelező szekciók

Mindezeknek létezniük kell (de te döntesz a sorrendről, a csoportosításról és a köztük lévő átmenetekről):

1. **Navigáció** — személyiséggel (nem generikus navbar)
2. **Hero** — az első, amit látnak. Ez adja el vagy öli meg az egész irányt.
3. **Szolgáltatások / Kínálat** — mit csinálnak
4. **Kiemelt munkák / Portfólió** — vizuális bizonyíték
5. **Miért mi / Megkülönböztetők** — 3 konkrét ok (nem üres frázisok)
6. **Társadalmi bizonyíték** — statisztikák, vélemények, vagy mindkettő
7. **Záró CTA** — lezáró címsor + cselekvés
8. **Footer** — navigáció, elérhetőség, közösségi linkek, egy karakteres tagline

## Mit jelent a „kész"

Ettől a prototípustól a felhasználónak közelebb kell hajolnia a képernyőhöz. Konkrétan:

- [ ] A vizuális motívum legalább 5 helyen megjelenik az oldalon
- [ ] Legalább 3 különböző animáció-típus (nem csak fade-up mindenre)
- [ ] Legalább 1 szekció megtöri a rácsot (átfedés, aszimmetria vagy kifutás)
- [ ] Legalább 1 „sötét" vagy „kiemelő színű" szekció a vizuális ritmusért
- [ ] A hover-effektek rugós/pattogó görbéket használnak, nem csak lineáris átmeneteket
- [ ] A tipográfia legalább 3 különböző méret/vastagság kombinációt használ
- [ ] A tartalom márkahű, magyar nyelvű, magázódó, és a brief valós adatait használja
- [ ] Nincs em dash (—) a szövegekben
- [ ] Mobilon reszponzív (375px) — az animációk és a layout alkalmazkodnak, nem csak egymás alá esnek
- [ ] Az oldal KÉSZ weboldalnak érződik, nem prototípusnak
- [ ] Aki ránéz, nem mondaná, hogy „ez AI-generáltnak néz ki"
```

---

## Indítási utasítások

Indítsd mind az N sub-agentet PÁRHUZAMOSAN, egyetlen üzenetben.

**Modell:** Ezekhez a sub-agentekhez mindig `opus`-t használj. A design-minőség a prioritás.

Minden sub-agenthez:
- Töltsd ki: [N], [Irány neve], [slug], az irány leírása és [Vállalkozás neve]
- A slug az `iranyok.json`-ból jön
- Töltsd ki a `<head>` sablont az irány `palette`, `fonts` és `google_fonts_url` értékeivel az `iranyok.json`-ból — a sub-agentnek ne kelljen hex értékeket vagy font-neveket kitalálnia

Példa:
```
Indíts [N] sub-agentet párhuzamosan. Mindegyik a
.claude/skills/generalas/references/subagent-utasitas.md sablonját kapja,
kitöltve a saját irányával a .webprojekt/iranyok.json-ból.

1. irány: "A csendes galéria" → koncepcio-1-a-csendes-galeria.html
2. irány: "A műterem" → koncepcio-2-a-muterem.html
3. irány: "A naturalista" → koncepcio-3-a-naturalista.html
```

---

## A sub-agentek végeztével

Ellenőrizd minden kimenetet:
1. A fájl létezik: `koncepcio-[N]-[slug].html`
2. Böngészőben megnyitva helyesen megjelenik

Ha egy sub-agent elbukott, csak azt az egyet indítsd újra.

Ezután írd meg az `index.html` koncepció-navigátort a SKILL.md 3. fázisa szerint — az irányok neveivel, leírásaival és linkjeivel az `iranyok.json`-ból.
