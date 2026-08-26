#!/usr/bin/env python3
"""SEO/GEO/AEO alap-ellenorzes statikus HTML oldalakon.

Hasznalat:
    python3 ellenorzes.py [mappa] [--domain https://pelda.hu]

Vegigmegy a mappa .html fajljain (a koncepcio-* fajlokat kihagyja),
es minden oldalon leellenorzi a belepoészintu checklistet.
Kilepesi kod: 0 = minden zold, 1 = van hiba.
Csak stdlib-et hasznal.
"""
import json
import re
import sys
from pathlib import Path

OK, WARN, FAIL = "OK", "FIGYELEM", "HIBA"

def get(pattern, html, flags=re.I | re.S):
    m = re.search(pattern, html)
    return m.group(1).strip() if m else None

def check_page(path, domain):
    html = path.read_text(encoding="utf-8", errors="replace")
    results = []
    def add(name, status, note=""):
        results.append((name, status, note))

    # title
    title = get(r"<title[^>]*>([^<]*)</title>", html)
    if not title:
        add("title", FAIL, "hianyzik")
    elif not (30 <= len(title) <= 65):
        add("title", WARN, f"{len(title)} karakter (ajanlott: 30-65)")
    else:
        add("title", OK, f"{len(title)} kar.")

    # meta description
    desc = get(r'<meta\s+name="description"\s+content="([^"]*)"', html) or \
           get(r'<meta\s+content="([^"]*)"\s+name="description"', html)
    if not desc:
        add("meta description", FAIL, "hianyzik")
    elif not (70 <= len(desc) <= 170):
        add("meta description", WARN, f"{len(desc)} karakter (ajanlott: 70-170)")
    else:
        add("meta description", OK, f"{len(desc)} kar.")

    # Open Graph
    og_required = ["og:title", "og:description", "og:image", "og:url", "og:type"]
    og_missing = [t for t in og_required
                  if not re.search(rf'property="{re.escape(t)}"', html, re.I)]
    if og_missing:
        add("Open Graph", FAIL, "hianyzo: " + ", ".join(og_missing))
    else:
        add("Open Graph", OK)
    if not re.search(r'name="twitter:card"', html, re.I):
        add("twitter:card", WARN, "hianyzik")
    else:
        add("twitter:card", OK)

    # canonical
    canon = get(r'<link\s+rel="canonical"\s+href="([^"]*)"', html) or \
            get(r'<link\s+href="([^"]*)"\s+rel="canonical"', html)
    if not canon:
        add("canonical", FAIL, "hianyzik")
    elif domain and not canon.startswith(domain):
        add("canonical", WARN, f"nem a megadott domainre mutat: {canon}")
    else:
        add("canonical", OK)

    # favicon
    if re.search(r'<link[^>]+rel="(?:shortcut )?icon"', html, re.I):
        add("favicon", OK)
    else:
        add("favicon", FAIL, "hianyzik")

    # lang + viewport
    add("lang attributum", OK if re.search(r"<html[^>]+lang=", html, re.I) else FAIL)
    add("viewport", OK if re.search(r'name="viewport"', html, re.I) else FAIL)

    # H1 count
    h1_count = len(re.findall(r"<h1[\s>]", html, re.I))
    if h1_count == 1:
        add("H1", OK)
    else:
        add("H1", FAIL, f"{h1_count} db (pontosan 1 kell)")

    # img alt
    imgs = re.findall(r"<img\b[^>]*>", html, re.I)
    no_alt = [i for i in imgs if not re.search(r'alt="[^"]+"|alt=""', i)]
    if not imgs:
        add("kep alt szovegek", OK, "nincs kep")
    elif no_alt:
        add("kep alt szovegek", FAIL, f"{len(no_alt)}/{len(imgs)} kepen nincs alt")
    else:
        add("kep alt szovegek", OK, f"{len(imgs)} kep")

    # JSON-LD
    blocks = re.findall(
        r'<script[^>]+type="application/ld\+json"[^>]*>(.*?)</script>', html, re.I | re.S)
    if not blocks:
        add("schema.org JSON-LD", FAIL, "hianyzik")
    else:
        try:
            types = []
            for b in blocks:
                data = json.loads(b)
                items = data if isinstance(data, list) else [data]
                types += [str(i.get("@type", "?")) for i in items if isinstance(i, dict)]
            add("schema.org JSON-LD", OK, "tipus: " + ", ".join(types))
        except json.JSONDecodeError as e:
            add("schema.org JSON-LD", FAIL, f"ervenytelen JSON: {e}")

    return title, desc, results


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    domain = None
    for a in sys.argv[1:]:
        if a.startswith("--domain"):
            domain = a.split("=", 1)[1] if "=" in a else None
    if domain is None and "--domain" in sys.argv:
        i = sys.argv.index("--domain")
        if i + 1 < len(sys.argv):
            domain = sys.argv[i + 1]
    root = Path(args[0]) if args and Path(args[0]).is_dir() else Path(".")

    pages = sorted(p for p in root.glob("*.html") if not p.name.startswith("koncepcio"))
    if not pages:
        print(f"Nincs .html fajl itt: {root.resolve()}")
        sys.exit(1)

    failed = False
    titles, descs = {}, {}

    for page in pages:
        title, desc, results = check_page(page, domain)
        if title:
            titles.setdefault(title, []).append(page.name)
        if desc:
            descs.setdefault(desc, []).append(page.name)
        print(f"\n=== {page.name}")
        for name, status, note in results:
            mark = {"OK": "  [ok]  ", "FIGYELEM": "  [figy]", "HIBA": "  [HIBA]"}[status]
            print(f"{mark} {name}" + (f" - {note}" if note else ""))
            if status == FAIL:
                failed = True

    # uniqueness across pages
    print("\n=== Oldalak kozotti egyediseg")
    for label, store in (("title", titles), ("meta description", descs)):
        dups = {k: v for k, v in store.items() if len(v) > 1}
        if dups:
            failed = True
            for text, files in dups.items():
                print(f"  [HIBA] duplikalt {label}: \"{text[:60]}...\" -> {', '.join(files)}")
        else:
            print(f"  [ok]   minden {label} egyedi")

    # sitemap + robots
    print("\n=== Technikai fajlok")
    for fname in ("sitemap.xml", "robots.txt"):
        if (root / fname).exists():
            print(f"  [ok]   {fname} letezik")
        else:
            failed = True
            print(f"  [HIBA] {fname} hianyzik")
    if (root / "robots.txt").exists():
        robots = (root / "robots.txt").read_text(encoding="utf-8", errors="replace")
        if "sitemap" not in robots.lower():
            print("  [figy] a robots.txt nem hivatkozik a sitemapre")

    # Google Search Console nyomok (csak jelzes, nem hiba: DNS-hitelesites nem latszik a kodban)
    print("\n=== Google Search Console")
    gsc_meta = any(re.search(r'name="google-site-verification"',
                             p.read_text(encoding="utf-8", errors="replace"), re.I)
                   for p in pages)
    gsc_file = any(root.glob("google*.html"))
    if gsc_meta or gsc_file:
        forras = "meta tag" if gsc_meta else "hitelesito fajl"
        print(f"  [ok]   GSC-hitelesitesi nyom talalva ({forras})")
    else:
        print("  [figy] nincs GSC-hitelesitesi nyom az oldalban - ha meg nincs Search Console,")
        print("         erdemes beallitani; ha DNS-sel vagy hosting-integracioval hitelesitettel,")
        print("         ez a jelzes figyelmen kivul hagyhato")

    print("\n" + ("EREDMENY: HIBAK VANNAK - javits es futtasd ujra." if failed
                  else "EREDMENY: minden ellenorzes zold."))
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
