# Real user query research — what people actually ask

**Conducted 14 September 2026.** Method, findings, and exactly what was added to the site in response.

---

## 1. Method, and what did not work

The goal was genuine user queries, not invented FAQ headings.

| Source | Result |
|---|---|
| **Search autocomplete (Google + Bing)** | ✅ **Primary source.** 2,856 probes → **2,699 unique suggestions**. This is the same data AnswerThePublic is built on. |
| **Competitor FAQ headings** | ✅ 78 question headings harvested from the 10 ranking pages already scraped. These are largely PAA-derived, so they proxy People Also Ask. |
| **Reddit** | ❌ **Blocked.** Firecrawl does not support the domain; Reddit returns 403 to server requests and a bot challenge in-browser. Not worked around. Thread *titles* from search results were still usable — they are themselves user questions. |
| **AnswerThePublic direct** | ❌ Gated. Reproduced its method instead, which is the same underlying data. |
| **SERP "People Also Ask" block** | ❌ Not exposed by the search API. Approximated via competitor FAQ headings + question-prefix autocomplete. |

### The autocomplete harvest
For each of 33 seed keywords across 12 clusters, we probed:
- the bare seed
- 15 question prefixes (`how`, `what`, `why`, `when`, `where`, `which`, `who`, `can`, `is`, `are`, `do`, `does`, `should`, `will`, `if`)
- 26 alphabet-soup suffixes (`seed a` … `seed z`)

against **both Google and Bing**, localised to New Zealand (`gl=nz`, `market=en-NZ`). Raw output: [`autocomplete.json`](autocomplete.json).

| Cluster | Suggestions | Cluster | Suggestions |
|---|---|---|---|
| home | 476 | crypto | 144 |
| highpay | 352 | betting | 179 |
| bonuses | 314 | pokies | 178 |
| nodeposit | 302 | fastpay | 154 |
| payments | 270 | tax | 114 |
| law | 102 | live | 114 |

### Filtering
Question-form or question-ending suggestions were isolated, then stripped of:
- **other markets** — Australia, South Africa, Canada, UK, US states, UAE (a large share of raw volume)
- **foreign brand queries** — BetMGM, Bovada, 1xBet, PlayOJO, Stake, OLG and similar
- **SEO spam domains** appearing in Bing suggestions (`igamblingstar`, `truejackpotguide`, `casinorankboard`, `brainal`)
- **homonyms** — "poki" the games site, "hokey pokey", "Pokeno"

What remained was diffed against an index of the 299 questions the site already answered.

---

## 2. What the data actually showed

### 2.1 The wagering-requirement cluster is enormous and under-served
The single largest question cluster on the whole site's topic space. Dozens of distinct phrasings, and critically these three shapes:

- **Numeric:** "what is a 40x wagering requirement", "what is a 10x wagering requirement", "what is 20x wagering requirement", "what is a 5x wagering requirement"
- **Procedural:** "how to calculate wagering requirements", "how to complete wagering requirements", "how to meet wagering requirements"
- **Adversarial:** "how to beat wagering requirements", "how to beat wagering requirements online casino"

We had "what does wagering mean" but answered none of the numeric or procedural variants.

### 2.2 The RTP cluster is dominated by one unanswered question
31 RTP questions, and the recurring theme was **verification and manipulation**:
- "can casinos change rtp", "can casino change rtp", "can casinos adjust rtp", "can casinos change rtp on slots"
- "how to check casino rtp", "how to find casino rtp", "where to find the rtp on a slot machine", "how do you know the rtp on a slot machine"
- "how to calculate rtp in casino"

People suspect operators tamper with returns. The honest answer is more interesting than a flat denial — studios ship multiple RTP configurations and operators choose which to deploy — and nobody in this market says so.

### 2.3 Tax is almost entirely one question asked 30 ways
50 tax queries, the overwhelming majority variants of "do you pay tax on gambling winnings nz". Already well covered. The genuine gaps were adjacent:
- "are lottery winnings taxable in nz" / "do lottery winnings get taxed in nz"
- "why is gambling not taxed" / "why are gambling winnings taxed"
- "what is the gambling winnings tax rate"

### 2.4 Trust and refusal-to-pay queries
- "can a casino refuse to pay out"
- "what to do if online casino won't pay"
- "do online casinos pay real money"
- "what is the most trusted online casino in new zealand"
- "do casinos pay out more on certain days" *(a myth worth killing)*

### 2.5 Honest-doubt queries nobody answers
Real, high-intent, and universally dodged by affiliate content:
- "are casinos a waste of money"
- "how to win real money online casino" / "how to win on pokie machines nz"

These deserve a straight answer. Dodging them is exactly the credibility problem that makes this category distrusted.

### 2.6 Gateway queries outside the obvious topic
- "how to buy bitcoin in nz", "where to buy bitcoin in new zealand", "is crypto legal in nz"
- "what is poli payment nz"
- "dollar deposit casino nz" / "$1 deposit casino nz"
- "is online poker legal in new zealand"
- "which sports betting app is best"

### 2.7 Reddit thread titles (from search results)
Even without thread bodies, the titles are user questions and confirm the betting-law anxiety:
*"Offshore online casinos in NZ: legal or risky?"* · *"Question about the new sports betting rules"* · *"NZ bans all offshore betting including bet365"* · *"TAB monopoly a disaster"* · *"Which sports betting app is best?"* · *"What are some good online pokies for people in NZ?"*

Note: most "Reddit" results for these keywords are **SEO spam wikis in unrelated subreddits** (r/LawnTalk, r/sysco, r/MitsubishiEclipse, r/LearnHTML). Genuine discussion is confined to r/newzealand.

---

## 3. What was added

**27 new FAQ entries** across 12 pages, plus **one new content section**. Every one answers a query that appeared in the harvest.

| Page | Added | Queries answered |
|---|---|---|
| `/` | 6 | do online casinos pay real money · most trusted online casino nz · best mobile casino nz · how to win real money online casino · are casinos a waste of money · what to do if a casino won't pay |
| `/online-pokies/` | 3 | can you play pokies online for real money · how much do pokies pay out · how to win on pokie machines nz |
| `/casino-bonus/` | 3 + **new section** | what is a 40x/20x/10x wagering requirement · how to calculate wagering requirements · how to beat wagering requirements |
| `/gambling-winnings-tax-nz/` | 3 | gambling winnings tax rate nz · why is gambling not taxed · are lottery winnings taxable in nz |
| `/fast-payout-casinos/` | 2 | can a casino refuse to pay out · do casinos pay out more on certain days |
| `/casino-payout-percentages/` | 2 | can casinos change rtp · how to calculate rtp |
| `/crypto-casinos-nz/` | 2 | is crypto legal in nz · how to buy bitcoin in nz |
| `/casino-payment-methods/` | 2 | what is poli payment nz · $1 deposit casino nz |
| `/licensed-online-casinos/` | 1 | is online poker legal in new zealand |
| `/best-sports-betting-sites/` | 1 | which sports betting app is best |
| `/live-casino/` | 1 | can you win real money at a live casino |
| `/no-deposit-bonus/` | 1 | how to get free spins no deposit |

### The new section
**`/casino-bonus/#multiples` — "What each wagering multiple actually means"**
A table running 0x / 10x / 20x / 30x / 35x / 40x / 50x / not-published against the turnover each demands on a NZ$100 bonus and the expected cost of clearing it, plus which operators sit at each level. Directly targets the numeric query cluster and is built for a featured snippet.

### Site totals after this pass
- **324 FAQ accordion items** across 40 pages
- **97,933 words** (up from 94,249)
- All FAQ entries carry `FAQPage` schema

---

## 4. Deliberately not answered

| Query | Why |
|---|---|
| "how to beat wagering requirements" *(as a trick)* | Answered, but honestly — you don't. The alternative is describing bonus abuse, which gets accounts closed. |
| "no kyc casino nz", "instant withdrawal no verification" | Answered with why the answer is no. We will not recommend operators skipping AML obligations. |
| Other-market queries (AU, ZA, CA, UK, US) | Wrong audience; would dilute NZ relevance. |
| Foreign brand queries (BetMGM, Bovada, 1xBet…) | Not operators we list or can test. |
| "how much is one bitcoin in nzd" | Price data, not our topic, and stale the moment it publishes. |

---

## 5. Repeating this

The harvester is reproducible — the probe list and both endpoints are in section 1. Worth re-running **quarterly**, and specifically:

- **After 1 December 2026**, when the licensing transition will generate a wave of new queries ("which casinos left new zealand", "is [brand] still legal in nz", "how do I get my money out of a casino that closed"). That is a predictable traffic event and the query space does not exist yet.
- **When licences are awarded**, since operator-name queries will spike for the 15 licensees.

Track in Search Console: queries with impressions but no target page. Those become the next cluster pages — see `SEO-STRATEGY.md` §7.
