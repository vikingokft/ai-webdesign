# Schema.org JSON-LD sablonok

Kész minták a leggyakoribb vállalkozás-típusokhoz. A blokk a `<head>`-be kerül:

```html
<script type="application/ld+json">
{ ... }
</script>
```

**Szabályok:**
- Csak olyan adatot tegyél bele, ami az oldalon LÁTHATÓAN is szerepel (a Google bünteti a láthatatlan schema-adatot)
- A `url` és `image` mindig abszolút URL legyen (domainnel) — ha még nincs domain, jelöld TODO-val
- A típust a vállalkozáshoz illeszd: https://schema.org/LocalBusiness altípusai a hivatkozási alap
- Egy oldalon több blokk is lehet (pl. LocalBusiness + FAQPage), de ugyanaz az entitás csak egyszer szerepeljen

## Gyakori altípus-választó

| Vállalkozás | @type |
|---|---|
| Fodrász, szépségszalon | HairSalon / BeautySalon |
| Étterem, kávézó | Restaurant / CafeOrCoffeeShop |
| Fogorvos, orvosi rendelő | Dentist / MedicalClinic |
| Ügyvéd | Attorney |
| Könyvelő, pénzügyi szolgáltató | AccountingService |
| Építőipar, lakásfelújítás | HomeAndConstructionBusiness |
| Autószerelő | AutoRepair |
| Edzőterem, személyi edző | ExerciseGym / HealthClub |
| Fotós, kreatív szolgáltató | ProfessionalService |
| Webshop | Organization + Product oldalanként |
| Nem helyhez kötött cég/szolgáltató | Organization vagy ProfessionalService |

## Helyi vállalkozás (teljes minta — fodrász példával)

```json
{
  "@context": "https://schema.org",
  "@type": "HairSalon",
  "name": "Példa Szalon",
  "description": "Balayage, airtouch és hajvágás Budapesten.",
  "url": "https://PELDA.hu/",
  "image": "https://PELDA.hu/images/hero.webp",
  "telephone": "+36301234567",
  "email": "info@pelda.hu",
  "priceRange": "4000-40000 HUF",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Minta utca 1.",
    "addressLocality": "Budapest",
    "postalCode": "1111",
    "addressCountry": "HU"
  },
  "geo": { "@type": "GeoCoordinates", "latitude": 0.0, "longitude": 0.0 },
  "openingHoursSpecification": [
    { "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
      "opens": "09:00", "closes": "19:00" },
    { "@type": "OpeningHoursSpecification",
      "dayOfWeek": "Saturday", "opens": "08:00", "closes": "14:00" }
  ],
  "sameAs": ["https://instagram.com/pelda", "https://facebook.com/pelda"]
}
```

Megjegyzések:
- `geo`: csak ha ismert a koordináta — ne találd ki; enélkül is érvényes
- `openingHoursSpecification`: az "előjegyzéssel" jellegű megkötést a látható szöveg kezeli, a schema a tényleges nyitva tartást adja
- `priceRange`: lehet egyszerűen "$$" formátum is, de a konkrét sáv informatívabb

## Organization (nem helyhez kötött)

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Cégnév",
  "url": "https://PELDA.hu/",
  "logo": "https://PELDA.hu/images/logo.png",
  "email": "info@pelda.hu",
  "sameAs": ["https://linkedin.com/company/pelda"]
}
```

## Személyes márka kiegészítő (Rólam oldalra)

```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Példa Panna",
  "jobTitle": "mesterfodrász",
  "worksFor": { "@type": "HairSalon", "name": "Példa Szalon" },
  "award": "Országos II. helyezés, alkalmi frizura kategória (2017)",
  "sameAs": ["https://instagram.com/pelda"]
}
```

## FAQPage (CSAK ha van látható GYIK az oldalon)

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Mennyi ideig tart egy balayage?",
      "acceptedAnswer": { "@type": "Answer", "text": "Általában 3-4 óra, a haj hosszától és sűrűségétől függően." }
    }
  ]
}
```

A kérdés-válasz szövegének SZÓ SZERINT egyeznie kell az oldalon láthatóval.

## Ellenőrzés

- Szintaxis: a skill `scripts/ellenorzes.py` szkriptje validálja
- Tartalmi teszt: https://validator.schema.org/ és a Google Rich Results Test (https://search.google.com/test/rich-results) — élesített oldalnál ajánld a felhasználónak
