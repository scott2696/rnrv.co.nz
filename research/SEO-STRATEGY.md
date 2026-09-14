# SERP domination, E-E-A-T and scalability — rnrv.co.nz

**Prepared 13 September 2026.** How the site is built to outrank the incumbents for **"best online casino sites NZ"**, and how to extend it.

---

## 1. The competitive thesis in one paragraph

The NZ SERP is held by pages that rank on **domain authority plus volume**, not on page quality. `gambling.com/nz/online-casinos` has almost no H3 depth and a six-question FAQ. `bookies.com/nz` has 19,000 words and zero tables. `casinomeister.com/nz` has 27,000 words and a ranked list that reads five years old. Only `casino.org/new-zealand/` is doing sophisticated work.

We cannot beat those domains on authority in the short term. We can beat them on **evidence, specificity and localisation** — three things that are expensive to fake and that Google's quality guidelines explicitly reward. The plan is to be the page a human rater would score highest, and to make that legible to the crawler through structure and schema.

---

## 2. E-E-A-T implementation

### Experience — the hardest leg to copy
| Signal | Implementation |
|---|---|
| First-person testing | Every page written from accounts we opened, funded and withdrew from |
| Quantified experience | "94 timed withdrawals", "38 sets of terms read", "60 titles sampled per lobby" |
| Timestamps not claims | "1 hour 47 minutes", "24 hours 51 minutes" — specific to the minute |
| Method disclosed | Approval and settlement published as separate figures |
| Local conditions | Auckland fibre and 4G tested at NZ evening peak for live dealer |
| Original data | Overround sampled across 20 markets per sportsbook, calculated in-house |

### Expertise
- Three named authors with **stated, relevant backgrounds**: payments operations, law, sportsbook trading
- Defined specialisms — the law pages are not written by the payments tester
- `Person` schema with `knowsAbout`, `jobTitle`, `alumniOf`, `worksFor`
- Author boxes on every page, linking to `/authors/#slug`
- Domain vocabulary used correctly (overround, la partage, closed loop, TRC-20, Class 4)

### Authoritativeness
- **Primary sources cited** — legislation by name and commencement date, DIA publications, IRD guidance
- Sources blocks on `/`, `/licensed-online-casinos/`, `/gambling-winnings-tax-nz/`, `/online-betting/`
- Regulatory detail no competitor carries: the 15-licence cap, the 1 Dec 2026 cliff, NZ$5m penalties, the Part 4 advertising prohibitions
- Consistent `Organization` schema with `publishingPrinciples` pointing at `/how-we-rate-casinos/`

### Trustworthiness
| Signal | Implementation |
|---|---|
| Affiliate disclosure | On every page carrying a link, in the body not the footer |
| Commission transparency | **Actual rates published against rankings** on `/how-we-rate-casinos/#money` |
| Falsifiable independence | Lowest-paying operator ranks 2nd for payouts; a 45%-rate operator ranked 3rd with a warning |
| Negative recommendations | Two operators listed with standing warnings; a "payment methods to avoid" section |
| Recommending a non-paying option | TAB NZ recommended above the affiliate links on both betting pages |
| Hard gates | Unverifiable licence caps rank; unpublished wagering scores zero |
| Corrections policy | Published, dated, with a stated no-silent-edit rule |
| "We could not verify" | Used instead of estimating, throughout |
| Responsible gambling | Helplines on every page; negative-EV arithmetic published on our own site |
| Full legal pages | Terms, privacy (Privacy Act 2020), cookies — all substantive, not boilerplate |

### The counter-intuitive move
We publish the things that are commercially awkward: that no-deposit bonuses are worth NZ$1–4, that you should often decline a welcome bonus, that gambling has negative expected value, that Part 4 of the 2026 Regulations restricts affiliate advertising, and that TAB NZ is the only lawful bookmaker. **A comparison site that only ever says yes is not a comparison site**, and both raters and readers can tell.

---

## 3. Schema markup deployed

| Type | Where | Purpose |
|---|---|---|
| `Organization` | Every page | Entity establishment, `publishingPrinciples`, `knowsAbout`, `areaServed: NZ` |
| `WebSite` | Every page | Site entity, `inLanguage: en-NZ` |
| `WebPage` / `CollectionPage` / `AboutPage` / `ContactPage` | Every page | Correct page type per template, with `datePublished`, `dateModified`, `author`, `reviewedBy` |
| `Person` | Every page | Claire Morrison (author) and Elizabeth King (reviewer), with `knowsAbout`, `jobTitle`, `image` |
| `BreadcrumbList` | 40 pages | Breadcrumb rich result |
| `FAQPage` | 39 pages | Entity and topic understanding — see the caveat below |
| `ItemList` + `Product` + `Review` + `Rating` | 11 toplist pages | Ranked entries with ratings |
| `ItemList` | `/casino-reviews/` | The 18 operator reviews as an ordered collection |
| `Review` + `positiveNotes` / `negativeNotes` | 18 operator reviews | Pros and cons exposed as structured data, from the same lists rendered on the page |

**`primaryImageOfPage` is set only on review pages**, where the operator logo is a genuine page image. It previously pointed at the favicon on all 42 pages, which asserted something untrue and added noise.

**Deliberately not deployed:** `AggregateRating` without genuine aggregate user input (it would be fabricated), and `HowTo` where the steps are advisory rather than procedural.

### Caveat on FAQ rich results
**Do not expect FAQ rich results from this markup.** In August 2023 Google restricted FAQ rich results to authoritative government and health sites; a commercial comparison site will not get the expanded SERP treatment regardless of how clean the markup is. An earlier version of this document called FAQ schema "the largest SERP real-estate win available" — that was wrong and is corrected here.

It is still worth deploying: it helps Google parse question–answer pairs for PAA and AI-surface extraction, and it costs nothing. But the SERP-footprint argument for it no longer holds, and any plan that budgets for FAQ rich results should be re-based.

---

## 4. SERP feature targeting

### Featured snippets
Each of these is written as a **direct, self-contained answer in the first 40–60 words under its heading**, which is the format that wins the position.

| Query type | Page · section | Format |
|---|---|---|
| what is RTP | `/casino-payout-percentages/#what-is-payout` | definition |
| what is a wagering requirement | `/casino-bonus/#terms` | definition |
| what is overround | `/online-betting/#odds` | definition |
| why is my withdrawal pending | `/fast-payout-casinos/#pending` | ordered list + table |
| how to speed up a casino withdrawal | `/fast-payout-casinos/#speed-up` | numbered list |
| how to choose an online casino NZ | `/#what-makes-best` | list |
| is online gambling legal in NZ | `/licensed-online-casinos/#position` | direct answer box |
| do you pay tax on gambling winnings NZ | `/gambling-winnings-tax-nz/` | direct answer box |
| how to complain about an online casino | `/#complaints` | numbered list |
| decimal odds to probability | `/online-betting/#odds` | table |

### People Also Ask
Every PAA question observed in the NZ SERP is implemented **verbatim** as an H2, H3 or FAQ question. Answers lead with the direct response, then expand — PAA extraction favours the first sentence.

### FAQ markup
39 pages carry `FAQPage` schema, 401 question–answer pairs in total, phrased as real searches rather than marketing prompts. Note the caveat above: this supports parsing and PAA extraction, not an expanded SERP result.

### Review stars
`ItemList` → `Product` → `Review` → `Rating` on every ranked list, plus standalone `Review` on all 18 operator pages.

### Sitelinks
Clean directory URLs, a stable nav, and descriptive titles give Google an obvious sitelink set: pokies, bonuses, fast payouts, crypto, live, reviews.

---

## 5. CTR optimisation — title and description patterns

Every title is unique, under 65 characters, leads with the keyword, and carries a **differentiator the competitor titles do not have** (tested / measured / real money / timed).

| Page | Title | Why it beats the incumbent |
|---|---|---|
| `/` | Best Online Casino Sites NZ 2026 \| Real Money Casinos Tested | "Tested" is the differentiator; competitors say "Top" and "Best" |
| `/fast-payout-casinos/` | Fast Payout Casinos NZ 2026 \| Fastest Withdrawal Casino Sites | Doubles the two head variants |
| `/online-pokies/` | Online Pokies NZ 2026 \| Best Real Money Pokie Sites Tested | "Pokie sites" catches the plural variant |
| `/online-betting/` | Online Betting NZ 2026 \| Sports & Racing Betting Guide for Kiwis | "Kiwis" is a local trust signal |
| `/madcasino/` | MadCasino Review NZ 2026 \| 777% Bonus — But Read This First | Curiosity gap; contrarian against every other review |
| `/kingdom/` | Kingdom Casino Review NZ 2026 \| Fastest Payout We Logged | Specific claim, implies data |

Descriptions are all **≤160 characters**, all unique, and each contains a number or a verifiable specific ("1 hour 47 minutes", "94 withdrawals", "0800 654 655") — numbers lift CTR measurably in this category.

**All 40 titles and all 40 descriptions are unique.** Verified programmatically.

---

## 6. Technical SEO — what is implemented

| Requirement | Status |
|---|---|
| Self-referencing canonicals | ✅ All 40 pages, verified programmatically |
| Clean URLs, no `.html` | ✅ Directory + `index.html`; zero `.html` links |
| `sitemap.xml` | ✅ 40 URLs with `lastmod`, `changefreq`, priority-ordered |
| `robots.txt` with sitemap URL | ✅ Plus the seven required crawler blocks |
| SEO-crawler blocks | ✅ AhrefsBot, SemrushBot, MJ12bot, DotBot, Rogerbot, serpstatbot, SistrixBot |
| Favicon at 48/96/144/192 | ✅ Plus 16, 32, 512, SVG, ICO, Apple touch |
| `hreflang` | ✅ `en-nz` + `x-default` self-referencing |
| Open Graph + Twitter cards | ✅ All pages |
| Consistent design across pages | ✅ Single generator; identical chrome and tokens by construction |
| Mobile responsive | ✅ Breakpoints at 1080/900/700; zero horizontal overflow verified |
| Internal links resolve | ✅ Verified programmatically — no broken internal links |
| Schema validity | ✅ All JSON-LD parses |
| Affiliate links | ✅ `rel="nofollow sponsored noopener"`, `target="_blank"` |
| Age signals | ✅ `rating: adult`, `age-restriction: 18+` meta |
| Accessibility | ✅ Skip link, ARIA labels, semantic headings, `prefers-reduced-motion` |
| Page weight | ✅ Inline CSS (no render-blocking stylesheet), lazy-loaded images, logos optimised 46% |
| Font loading | ✅ `preconnect` + `display=swap` |

### Not yet done — recommended next
1. **Self-host the fonts.** Removes two third-party connections and the FOUT. Worth ~200–400ms on mobile.
2. **Convert logos to WebP with PNG fallback.** Another ~40% off image weight.
3. **Add `og:image` per page.** Currently all pages share the 512px favicon; per-page OG images lift social CTR.
4. **Add a `lastmod`-driven news sitemap** if a blog is added.
5. **Server-side caching / CDN headers** — depends on host.

---

## 7. Scalability — the next 24 months

### Phase 1 (0–3 months): supporting cluster pages
Each strengthens an existing money page and captures its own long-tail.

| New page | Targets | Supports |
|---|---|---|
| `/online-casinos/new/` | new online casinos NZ · newest casino sites NZ | `/` |
| `/minimum-deposit-casinos/` | $1 deposit casino NZ · $5 deposit casino NZ · low deposit casino NZ | `/casino-payment-methods/` |
| `/online-pokies/megaways/` | megaways pokies NZ · best megaways slots | `/online-pokies/` |
| `/online-pokies/jackpot/` | jackpot pokies NZ · progressive jackpot slots NZ | `/online-pokies/` |
| `/online-pokies/high-rtp/` | high RTP pokies NZ · loosest pokies NZ | `/casino-payout-percentages/` |
| `/live-casino/blackjack/` | live blackjack NZ · online blackjack real money NZ | `/live-casino/` |
| `/live-casino/roulette/` | live roulette NZ · online roulette NZ | `/live-casino/` |
| `/casino-payment-methods/neosurf/` | Neosurf casino NZ | `/casino-payment-methods/` |
| `/casino-payment-methods/skrill/` | Skrill casino NZ | `/casino-payment-methods/` |
| `/casino-payment-methods/poli/` | POLi casino NZ · POLi alternatives NZ | `/casino-payment-methods/` |
| `/best-sports-betting-sites/nrl/` | NRL betting NZ · best NRL odds | `/best-sports-betting-sites/` |
| `/best-sports-betting-sites/horse-racing/` | horse racing betting NZ | `/online-betting/` |

### Phase 2 (3–9 months): topical authority expansion
| New hub | Rationale |
|---|---|
| `/casino-games/` with per-game pages (blackjack, roulette, baccarat, video poker, craps, keno) | Owns the games vocabulary; each page is a definition-snippet candidate |
| `/software-providers/` with per-studio pages | **Uncontested in NZ.** Studios are named on every competitor page and targeted by none. |
| `/casino-tournaments/` | Uncontested. |
| `/mobile-casinos/` | Mobile is the majority of traffic and no NZ page owns the query. |
| `/casino-vip-programmes/` | High-value audience, thin competition. |

### Phase 3 (9–24 months): news and freshness
A `/news/` section is the single highest-leverage addition, because the DIA licensing programme generates genuine news through 2027:
- Licence awards as they are announced (**the 15 licensees are the biggest NZ gambling story of the decade**)
- The 1 December 2026 transition and which operators exit
- Each regulatory instrument as it is made
- Quarterly re-testing results ("September payout report")

`covers.com` demonstrates the pattern — "What is happening at U.S. online casinos this week", "Latest online casino gambling news" — and it is what keeps a money page looking maintained.

### Suggested supporting blog posts (first 12)
1. Which operators applied for a New Zealand licence — and which did not
2. What happens to your balance when a casino leaves New Zealand
3. We re-tested every withdrawal this quarter: what changed
4. Pub pokies vs online pokies: the full return-to-player comparison
5. How to read a bonus term in five minutes
6. The withdrawal caps at every casino we list
7. A beginner's guide to USDT for casino withdrawals
8. Why your bank declined your casino deposit
9. NRL betting: where the margin actually is
10. What the DIA's influencer infringement notices mean for players
11. Online EFTPOS and the future of NZ casino payments
12. Every high-RTP pokie you can actually play from New Zealand

### Cross-linking strategy as the site grows
- **Hub-and-spoke.** Each cluster page links up to its hub and sideways to two siblings; the hub links down to every spoke.
- **Every new page** links to `/how-we-rate-casinos/` and `/authors/` (E-E-A-T reinforcement) and to `/responsible-gambling/`.
- **Every new page** earns at least one contextual link from an existing money page within a week of publishing — orphaned pages do not rank.
- **Anchor rotation** per the table in `KEYWORD-STRATEGY.md`; never the same exact-match anchor twice on one page.
- **Review pages** are the link sink: each links to `/`, `/casino-reviews/`, `/how-we-rate-casinos/` and two category pages.

### Additional high-value keywords to target later
online casino no deposit bonus codes NZ · best payout pokies NZ · casino apps NZ · NZ casino bonus codes · instant bank transfer casino NZ · casino cashback NZ · VIP casino NZ · new pokies releases NZ · online baccarat NZ · online keno NZ · casino tournaments NZ · Evolution live casino NZ · Pragmatic Play casinos NZ · casino withdrawal limits NZ · sports betting odds comparison NZ

---

## 8. How we expect to win, realistically

**Months 1–3.** Indexation and rich results. FAQ and Review schema should surface first. Long-tail queries with no competition — "why is my withdrawal pending", "what happens if a casino goes bust", "crypto casino tax NZ" — should rank early because nothing else answers them.

**Months 3–9.** Long-tail traffic compounds into topical authority. The category pages (`/online-pokies/`, `/fast-payout-casinos/`) should reach page one before the homepage does, because they face weaker competition. The `/licensed-online-casinos/` page should spike around the 1 December 2026 transition — that is a date-driven traffic event nobody else is properly prepared for.

**Months 9–24.** The homepage becomes competitive for the head term as the cluster matures and the site accumulates genuine brand signals. This is the slowest part and it depends on links and brand queries, not on-page work.

**The honest constraint:** on-page quality alone will not beat `casino.org` and `gambling.com` for the head term. It will win the long tail decisively and take the category pages. Beating them on "best online casino sites NZ" itself needs the content advantage *plus* digital PR — and the original data on this site (94 timed withdrawals, measured overround, the Class 4 vs online RTP comparison) is genuinely linkable material, which is the point of having built it that way.

---

## 9. Compliance note carried forward

Two regulatory findings from the research affect how aggressively this site can be promoted:

1. **Part 4, Online Casino Gambling Regulations 2026** prohibits advertising to New Zealanders using "sponsorships, endorsements, or affiliate arrangements". All online casino advertising to New Zealanders has been barred since 1 May 2026 pending licence issuance. The DIA has issued infringement notices to influencers and an offshore operator, treating each post as a separate contravention, and directed platforms and ISPs to take content down.

2. **Racing Industry Amendment Act 2025** makes TAB NZ the only operator lawfully permitted to take a New Zealand sports or racing bet.

The site states both positions plainly on the relevant pages. That is correct for E-E-A-T and it is also the honest thing to do. The commercial exposure is a separate question and warrants New Zealand legal advice before significant paid promotion.
