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
python3 _build/build.py         # build all pages + sitemap.xml + robots.txt + redirect stubs
```

`{{month}}` in any title, H1, description or body resolves to the current month
and year at build time (`MONTH_YEAR` in `build.py`), so "September 2026" in a
title refreshes on rebuild rather than going stale in place. Rebuild monthly.

### Title width

Google truncates SERP titles on **pixel width**, not character count. The build
measures every title against `TITLE_PX_LIMIT` (580px) using exact Arial 20px
advance widths embedded in `build.py`, and prints either a pass line or a list
of offenders:

```
titles: all within 580px (widest 565.0px)
```

Titles use a bracket suffix — `Online Casinos NZ: Best Real Money Sites [September 2026]`.
Widths are measured with "September" substituted because it is the longest
month name, so a title that passes cannot overflow later in the year.

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
images/authors/     author portraits, 1x and 2x
```

### URL map

| URL | Role |
|---|---|
| `/` | Brand hub — routes to every cluster |
| `/online-casinos/` | **Head money page** |
| `/licensed-online-casinos/` | Licensing, legality, the 1 Dec 2026 transition |
| `/new-casinos-nz/` | Running list of new and newly licensed casinos |
| `/online-pokies/` · `/live-casino/` · `/crypto-casinos-nz/` | Product clusters |
| `/casino-bonus/` · `/no-deposit-bonus/` | Bonus clusters, kept separate to avoid cannibalising |
| `/casino-payout-percentages/` · `/fast-payout-casinos/` | Payout clusters (return vs speed) |
| `/casino-payment-methods/` | Banking |
| `/online-betting/` · `/best-sports-betting-sites/` | Betting |
| `/how-we-rate-casinos/` · `/authors/` · `/about/` · `/contact/` | Trust |
| `/casino-reviews/` + 18 children | Operator reviews |
| `/instant-withdrawals/` | Redirect stub → `/fast-payout-casinos/` |

**Redirect stubs are meta-refresh + canonical, not true 301s.** Static hosting
cannot emit a 301. If the host supports real redirects (Cloudflare rules,
Netlify `_redirects`, nginx), configure the 301 there and delete the stub
directory. `REDIRECTS` in `build.py` is the source of truth for these.

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

| Brand | File | Source |
|---|---|---|
| CrownSlots | `logos/crownslots.png` | Real artwork, taken from `11woodward.co.nz/logos/norm/` |
| CrownSlots | `logos/crownslots-white.png` | Reversed variant, for dark backgrounds only |
| Gunsbet | `logos/gunsbet.png` | **Generated wordmark** — no vendor artwork found on this machine |

Per the master README convention, the file used on the white `.tl-logo` tile must
be the **dark** artwork. CrownSlots' `-rev` variant sets "crown" in white and
disappears on the tile, so `norm` is the one installed. Both CrownSlots files were
trimmed of transparent padding, resized to 420px wide and palette-quantised
(60KB → 8.6KB with no visible loss).

**Gunsbet is still a placeholder.** It is not in the shared master set and no copy
exists in any sibling site; gunsbet.com is geo-blocked from New Zealand. Drop the
vendor file in at `logos/gunsbet.png` when it arrives — no code change is needed.

Neither CrownSlots nor Gunsbet is in `MY_SITES/logos/` (the master set). Worth
adding CrownSlots there so the other sites can pick it up.

---

## Authors

Three named reviewers are defined in `build.py` (`AUTHORS`) and emitted as
`Person` schema with `knowsAbout` and `jobTitle`:

- **Claire Morrison** — testing, payments, pokies, payout timing
- **Elizabeth King** — regulation, bonus terms, tax, responsible gambling
- **Claire Morrison** — sports and racing betting, odds and margins

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
`/licensed-online-casinos/` should be updated as licences are awarded.

### Sitemap and schema

`sitemap.xml` is regenerated on every build from each fragment's `modified`,
`priority` and `changefreq`. **Bump `modified` when you change a page** — a
`lastmod` that does not move is worse than none, because it trains crawlers to
ignore it.

Schema is emitted per page from `head_html()` in `build.py`: `Organization`,
`WebSite`, the page type (`WebPage` / `CollectionPage` / `AboutPage` /
`ContactPage`, set via `pageType` in front matter), `Person` for both the author
and the fact-checker, `BreadcrumbList`, `FAQPage`, `ItemList` for toplists and
the review grid, and `Review` with `positiveNotes` / `negativeNotes` on operator
reviews.
