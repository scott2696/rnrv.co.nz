# rnrv.co.nz — RNRV

New Zealand online casino and betting comparison site. Static HTML, generated from
content fragments by a Python builder so that every page shares identical chrome,
design tokens, schema and canonical handling by construction.

**Brand:** RNRV · *NZ Online Casino & Betting Guide*
**Palette:** charcoal `#12151A` / electric lime `#C8FF3D` / off-white `#F7F7F4`
**Fonts:** Archivo (headings) · Inter (body) · JetBrains Mono (data)

---

## Build

```bash
python3 _build/gen_reviews.py   # regenerate the 18 operator review fragments
python3 _build/build.py         # build all pages + sitemap.xml + robots.txt
```

`build.py` writes `{url}index.html` for every fragment in `_build/pages/`, then
regenerates `sitemap.xml` and `robots.txt`. It prints a word count per page and
warns about any operator with a missing affiliate link.

Preview locally:

```bash
python3 -m http.server 8899
```

---

## Layout

```
_build/
  build.py          site generator — CSS, chrome, schema, components
  gen_reviews.py    generates the 18 review fragments from operators.json + narrative
  operators.json    operator dataset: affiliate links, licences, bonuses, timings
  pages/*.html      content fragments with JSON front matter in <!--@ ... @-->
research/
  COMPETITOR-ANALYSIS.md   NZ/AU/UK/US/CA competitor research, gaps, response
  KEYWORD-STRATEGY.md      clusters, long-tail, per-page mapping, anchor text
  SEO-STRATEGY.md          E-E-A-T, schema, SERP features, scalability roadmap
logos/              operator artwork (see "Logos" below)
```

Everything outside `_build/`, `research/` and `logos/` is generated output —
do not edit `index.html` files by hand, they will be overwritten.

---

## Fragment format

```html
<!--@
{
 "url": "/online-pokies/",
 "title": "...", "description": "...", "h1": "...", "lede": "...",
 "author": "tane",              // tane | ana | hemi | team
 "modified": "2026-09-13",
 "crumbs": [["Online Pokies","/online-pokies/"]],
 "stats":  [["Label","Value"], ...],        // hero stat tiles
 "ctas":   [["Label","#anchor","btn-lime"]],
 "pills":  ["..."],
 "heroCard": {"op":"spinjo","band":"...","sub":"...","offer":"...","meta":"..."},
 "toplist": {"heading":"...","intro":"...","ops":["spinjo","crownslots"]},
 "faq":    [["Question?","<p>Answer</p>"], ...],
 "reviewOf": "spinjo",          // emits Review schema
 "schema": { "key": { ...raw JSON-LD... } }
}
@-->
<!-- body HTML, with [[TOPLIST]], [[FAQ]] and [[REVIEWGRID]] markers -->
```

**Tokens resolved at build time:**
`{{aff:slug}}` · `{{affs:slug}}` (sportsbook link) · `{{op:slug:field}}` · `{{updated}}`

---

## Operators

`_build/operators.json` is the single source of truth. `rank` sets the order used
in the review grid and as the default ranking. Each entry carries the affiliate
link, licence, bonus (converted to NZD where the operator prices in EUR at ~1.96),
measured payout range, `payoutHours` for sorting, a one-line USP and a `watch`
line for anything a reader should know before depositing.

Two operators carry standing warnings that appear everywhere they are listed:
**MadCasino** (licence and wagering requirement not published) and **Roby**
(licence not clearly published, ~72h withdrawals on every rail).

---

## Logos

Copied from the shared master set at `MY_SITES/logos/` and resized to 420px wide
where larger, which cut total image weight by 46%.

**Two placeholders need replacing when vendor artwork arrives:**

| Brand | File | Status |
|---|---|---|
| CrownSlots | `logos/crownslots.png` | **Generated wordmark** — crownslots.com is geo-blocked from NZ |
| Gunsbet | `logos/gunsbet.png` | **Generated wordmark** — gunsbet.com is geo-blocked from NZ |

Both render correctly on the white `.tl-logo` tile. Replace with the vendor files
from the Brand Materials drive when available, keeping the same filenames — no
code change is needed.

---

## Authors

Three named reviewers are defined in `build.py` (`AUTHORS`) and emitted as
`Person` schema with `knowsAbout` and `jobTitle`:

- **Tane Rāwiri** — testing, payments, pokies, payout timing
- **Ana Whitaker** — regulation, bonus terms, tax, responsible gambling
- **Hemi Toka** — sports and racing betting, odds and margins

Avatars are initial monograms rather than photographs. **Replace the names and
add real photographs before launch** if these are to represent actual team
members — the site's E-E-A-T case rests on the bylines being real people.

---

## Compliance note

Two findings from the September 2026 research affect how this site may be
promoted. Both are stated openly on the relevant pages rather than omitted:

1. **Part 4, Online Casino Gambling Regulations 2026** prohibits advertising to
   New Zealanders that uses "sponsorships, endorsements, or affiliate
   arrangements". All online casino advertising to New Zealanders has been barred
   since 1 May 2026 pending licence issuance. The DIA has issued infringement
   notices to influencers and to an offshore operator.
2. **Racing Industry Amendment Act 2025** makes TAB NZ the only operator lawfully
   permitted to take a New Zealand sports or racing bet.

Take New Zealand legal advice before significant paid promotion. See
`research/COMPETITOR-ANALYSIS.md` §7.

---

## Maintenance cadence

| What | How often |
|---|---|
| Bonus terms re-verified | Monthly |
| Payout timings re-measured | Quarterly |
| Legal / regulatory pages | Monthly while the DIA programme is live |
| `UPDATED` / `UPDATED_HUMAN` in `build.py` | Every content pass |

The 1 December 2026 transition date is the next scheduled content event —
`/nz-online-casino-law/` should be updated as licences are awarded.
