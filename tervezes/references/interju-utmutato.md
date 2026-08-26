# Interjú-útmutató

A feladatod, hogy mindent megtudj, ami egy éles brand briefhez és oldaltérképhez kell. Stratéga vagy, nem kitöltendő űrlap — azt kérdezd, ami releváns, hagyd ki, ami nem, és kérdezz vissza a homályos válaszokra.

**Eszköz-szabály:** Minden kérdést az `AskUserQuestion` eszközzel tegyél fel. Soha ne kérdezz sima szövegként.

**Beszélgetési stílus:**
- Beszélgetős és alkalmazkodó — arra kérdezz rá, amit a felhasználó mond, ne arra, ami a forgatókönyvben következne
- Kérdezz vissza a homályos válaszokra. A „modern és letisztult" nem vizuális irány. A „mindenki" nem célcsoport
- Ha valamit már tudsz a kontextusból (mellékesen említette), ne kérdezd meg újra
- A kapcsolódó kérdéseket csoportosítsd (max. 2-3 egyszerre). Használd a józan eszed — kevesebb kérdés ott, ahol egyértelmű a helyzet, több ott, ahol tényleg bizonytalanság van
- Adj javaslatokat, ne csak opciókat sorolj: „Az alapján, amit elmondtál, X-et javasolnám, mert..."
- Ha elakad: „Írj most valami őszintét, később még csiszolhatunk rajta"

---

## 0. lépés — Új oldal vagy redesign?

Ezt kérdezd először. Ez határoz meg minden továbbit.

**Cél:** Tudni, hogy ki kell-e nyerni a meglévő arculatot, és hogy azt megtartjuk vagy újragondoljuk.

Példa kérdés: *„Tiszta lappal indulsz, vagy van egy meglévő oldalad, amit újraterveznél?"*

Felkínálandó opciók:
- **Új oldal** — üres lap
- **Redesign — arculat megtartása** — ugyanazok a színek/fontok/identitás, csak újraépítve
- **Redesign — új irány** — van oldala, de friss megjelenést szeretne

### Redesign esetén (mindkét típusnál):

Kérd el a jelenlegi oldal URL-jét, majd futtasd a brand-kinyerést:
```bash
python3 .claude/skills/tervezes/scripts/extract_brand.py [URL] -o .webprojekt/brand-extraction/
```

Olvasd be a `.webprojekt/brand-extraction/brand-identity.json` fájlt, és mutass összefoglalót:
> „Ezeket a színeket találtam: [hex kódok leírással]. Használt fontok: [lista]. Logó: [letöltve / nem található]."

- **Arculat megtartása:** Erősítsd meg, ami stimmel, kérdezz rá az esetleges finomításokra. Rögzítsd a színeket és fontokat — a szín/font felfedezést később hagyd ki.
- **Új irány:** A kinyert arculatot úgy keretezd, mint „amitől el akarsz mozdulni". A vizuális identitás szakaszt így is vedd végig.

---

## Amit meg kell tudnod

Ezeken a kategóriákon abban a sorrendben haladj végig, ami a beszélgetésből adódik. Nem kell mindenre rákérdezni — használd a józan eszed, hogy mi világos már, és hol kell tényleg több információ.

### Vállalkozás és pozicionálás

**Amire szükséged van:** Egy világos egymondatos leírás, konkrét célcsoport, elsődleges CTA, és ami megkülönbözteti a versenytársaktól.

Példa kérdések (használd, ami illik, fogalmazd át szabadon):
- *„Mivel foglalkozik a vállalkozásod — el tudod mondani egy mondatban?"*
- *„Ki az ideális ügyfeled? Konkrétumok kellenek — iparág, pozíció, cégméret, mi frusztrálja."*
- *„Mi az az EGY dolog, amit a látogatóknak csinálniuk kell az oldaladon?"*
- *„Miben vagy más, mint a versenytársaid? Ha elakadtál — még az is valódi, hogy 'személyesebb figyelmet adok', ha tényleg igaz."*

Ha már eleget tudsz: fogalmazz meg egy pozicionálási állítást, és mutasd vissza:
> „Ezt hallom ki belőle: [2-3 mondat]. Így stimmel? Min változtatnál?"

**Minőségi mérce:** A célcsoport legyen elég konkrét ahhoz, hogy egy valódi ember ráilleszthető legyen. A megkülönböztető legyen kézzelfogható, ne „mi jobban odafigyelünk".

---

### Hangulat és vizuális irány

**Amire szükséged van:** Az érzelmi tónus, hogy minek NEM szabad tűnnie, és elég alap a design irányok brainstormjához.

Példa kérdések:
- *„Milyen érzést keltsen az oldalad az első 3 másodpercben — még mielőtt bárki egy szót elolvasna?"*
- *„Kik NEM vagytok? Néha könnyebb kontraszttal definiálni. Nem korporét? Nem vagány? Nem akadémikus?"*

Ha homályos a válasz, adj élénk példákat, amire reagálhat:
> Bizalom és tekintély / Meleg és közvetlen / Merész és kreatív / Tiszta és minimál / Prémium és luxus / Energikus és dinamikus

Reakciókat kérj, ne csak választást: *„Ha egy luxusmárka weboldalára gondolsz egy startupéhoz képest — melyik irány érződik inkább a tiédnek?"*

---

### Inspiráció

**Amire szükséged van:** 2-3 URL olyan oldalakról, amiket csodál (versenytárs vagy sem), bármilyen képernyőkép vagy brand asset.

Példa kérdések:
- *„Ossz meg 2-3 oldalt, aminek a kinézete megfog — nem kell a te iparágadból lennie."*
- *„Van képernyőképed konkrét elemekről, amiket szeretsz? Hero elrendezések, tipográfia, színhasználat?"*
- *„Van már logód vagy bármilyen brand asseted? Tölts fel mindent, amid van."*

Minden megadott URL-t tölts le és elemezz:
- Színpaletta (domináns, másodlagos, kiemelő)
- Tipográfia (serif vs. sans, vastagság-játék, címsor-skála)
- Layout sűrűség (fehér tér, rács feszessége, szekció-ritmus)
- Design irányzat (minimalista, editorial, brutalista, organikus stb.)

Szintetizálj az összes URL-ből:
> „Ezt a mintát látom: [szintézis]. A közös szál: [téma]. Ez azt mondja nekem, hogy az oldalad [fordítás] hangulatot akar."

---

### Színek és fontok

**Hagyd ki, ha a redesign-kinyerésből már rögzítve van („arculat megtartása" útvonal).**

Te vagy a designer — a palettát és a fontokat te választod minden koncepció irányhoz a brainstorm során. Itt csak azt kell tudnod, van-e a felhasználónak megkötése.

**Amire szükséged van:** Bármilyen kemény követelmény vagy kizáró tényező. Ennyi.

Kérdezz röviden:
- *„Vannak meglévő márkaszíneid, amiket meg kell tartani? Ha igen, mik a hex kódok?"*
- *„Van szín, amit kerülni szeretnél?"*
- *„Van kötelező márka-fontod? Ha nincs, én választok minden koncepcióhoz illő fontokat."*

Ha vannak konkrét hex kódok vagy fontok → rögzítsd **horgony színekként/fontokként**, amiket minden iránynak tiszteletben kell tartania.
Ha nincs semmi → lépj tovább. A brainstorm során te választod, ami az adott koncepcióhoz a legjobb.

Itt NE javasolj palettákat vagy font-párosításokat. Az koncepciónként történik a brainstorm fázisban.

---

### Oldalstruktúra

**Amire szükséged van:** Mely oldalak indulnak az első napon, melyek várnak a v2-re, és mi kerül a kezdőoldalra.

Az oldalakról — példa kérdések:
- *„Milyen oldalak kellenek az induláskor? A kezdőoldal adott."* (Gyakori: Rólunk, Szolgáltatások, Portfólió, Kapcsolat, Árak, Blog, GYIK)
- Ha 6+ oldalt sorol: *„Ezek közül melyik tényleg indulás-kritikus? Melyik jöhet 3 hónappal később, amikor több tartalmad lesz?"*

Konkrétan a kezdőoldalról — ez épül meg, ezért értsd meg alaposan:
- *„Mit KELL látnia a látogatónak görgetés előtt, a hajtás felett?"*
- *„Milyen bizonyítékod van MOST — nem az, amit tervezel megszerezni?"* (Vélemények, logók, esettanulmányok, statisztikák, sajtó)
- *„Mi az elsődleges és a másodlagos CTA-d?"*

**Kritikus szabály:** Arra építs, amije VAN, ne arra, amit szeretne. 2 vélemény → 2-vel tervezz. Ne hozz létre üres szekciókat.

---

### Tartalom

**Amire szükséged van:** Mi van készen, mit kell megírni, mi eshet ki a scope-ból.

Csak akkor kérdezd, ha releváns — egyszerű bemutatkozó oldalaknál hagyd ki:
- *„Van blogod, vagy tervezel tartalmat publikálni? Milyen gyakran?"*
- *„Van átköltöztetendő meglévő tartalom — posztok, letöltések, anyagok?"*
- *„Van lead magneted? Valami, amit a látogatók az email-címükért cserébe kapnak?"*

---

## Mikor tudsz eleget

Akkor van elég információd, ha ezekre mind tudsz válaszolni:
- [ ] Mit csinál ez a vállalkozás? (egy mondat)
- [ ] Ki a konkrét célcsoport?
- [ ] Mi az elsődleges CTA?
- [ ] Mi különbözteti meg őket?
- [ ] Milyen érzelmi hangulata/tónusa legyen az oldalnak?
- [ ] Van-e kötelező márkaszín vagy kerülendő szín?
- [ ] Van-e kötelező márka-font?
- [ ] Mely oldalak indulnak az első napon?
- [ ] Milyen kezdőoldal-szekciók lesznek + milyen tartalom van készen?

NEM kell mindenre explicit rákérdezned, ha a kontextusból már világos. Használd a józan eszed.

---

## A brief kimeneti formátuma

Írd meg a `.webprojekt/brief.md` fájlt ezzel a szerkezettel:

```markdown
# Brand brief

## Pozicionálás
- **Vállalkozás:** [egymondatos leírás]
- **Ideális ügyfél:** [konkrét leírás]
- **Elsődleges CTA:** [az egyetlen cselekvés]
- **Megkülönböztető:** [amiben mások]
- **Pozicionálási állítás:** [2-3 mondatos szintézis]

## Márkahang és tónus
- **Személyiség:** [2-3 melléknév]
- **Tónus:** [hogyan kommunikálnak]
- **Ilyenek vagyunk:** [lista]
- **Ilyenek NEM vagyunk:** [lista]

## Vizuális identitás

### Szín-megkötések
[Csak ha a felhasználónak konkrét követelménye van. Egyébként: „Nincs — koncepciónként a designer választ."]
- **Horgony színek:** [megtartandó hex kódok, ha vannak]
- **Kerülendő:** [kerülendő színek vagy tónusok, ha vannak]

### Font-megkötések
[Csak ha a felhasználónak van márka-fontja. Egyébként: „Nincs — koncepciónként a designer választ."]
- **Kötelező font:** [font neve, ha van]

> A végleges paletta és a fontok koncepció-irányonként dőlnek el a brainstorm során.

### Vizuális stílus
- **Kulcsszavak:** [3-5 szó]
- **Inspirációs minták:** [szintézis az elemzett URL-ekből]
- **Csináld:** [konkrét iránymutatás]
- **Ne csináld:** [konkrét anti-minták]

# Oldaltérkép

## Oldalak (v1 — indulás)
[Minden oldalhoz:]
### [Oldal neve]
- **Célja:** [egy mondat]
- **Szekciók:** [sorrendezett lista rövid leírásokkal]
- **Tartalom állapota:** [Kész / Megírandó / Placeholder mehet]

## Oldalak (v2 — később)
[Elhalasztott oldalak listája rövid megjegyzésekkel]

## Kezdőoldal szekció-bontás
| Szekció | Szükséges tartalom | CTA | Tartalom állapota |
|---------|-------------------|-----|-------------------|
[Szekciónként egy sor]

## Tartalom-leltár
- **Használatra kész:** [lista]
- **Elkészítendő:** [lista]
- **Meglévő assetek:** [logó, portréfotó, ügyfél-logók, fotók stb.]

## CTA stratégia
- **Elsődleges CTA:** [szöveg + cél]
- **Másodlagos CTA:** [szöveg + cél]
- **CTA elhelyezés:** [hol jelenik meg az oldalon]
```
