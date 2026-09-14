#!/usr/bin/env python3
"""RNRV site builder.

Reads _build/pages/*.html fragments (JSON front matter inside <!--@ ... @-->)
and writes clean-URL pages at {url}index.html. Every page gets the same
chrome, design tokens, schema block and self-referencing canonical, so the
homepage layout and colour scheme propagate site-wide by construction.
"""
import json, os, re, html, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "_build", "pages")

DOMAIN = "https://rnrv.co.nz"
SITE = "RNRV"
TAGLINE = "NZ Online Casino &amp; Betting Guide"
UPDATED = "2026-09-13"
UPDATED_HUMAN = "13 September 2026"
MONTH_YEAR = datetime.date.today().strftime("%B %Y")
FOUNDED = "2026"

OPS = json.load(open(os.path.join(ROOT, "_build", "operators.json")))
ORDER = [s for s, _ in sorted(OPS.items(), key=lambda kv: kv[1]["rank"])]

# ---------------------------------------------------------------- authors
AUTHORS = {
 "claire": dict(
   name="Claire Morrison", slug="claire-morrison", initials="CM",
   role="Senior Writer &amp; Reviewer",
   jobTitle="Senior Writer and Reviewer",
   photo="/images/authors/claire-morrison.jpg",
   knows=["online casinos","online pokies","casino bonuses","NZD payment processing",
          "withdrawal testing","sports betting","New Zealand gambling"],
   short="Opens every account on this site personally, deposits her own New Zealand dollars and times every withdrawal.",
   bio="Claire has spent fifteen years writing about consumer finance and regulated industries in New Zealand, "
       "the last four of them covering online gambling. She opens every account RNRV writes about in her own name, "
       "completes verification like any other customer, deposits her own New Zealand dollars and logs the timestamp "
       "on every withdrawal request from her home connection north of Auckland. The payout figures on this site are "
       "hers, and so is the decision to publish the ones that are inconvenient."),
 "elizabeth": dict(
   name="Elizabeth King", slug="elizabeth-king", initials="EK",
   role="Editor &amp; Fact-Checker",
   jobTitle="Editor and Fact-Checker",
   photo="/images/authors/elizabeth-king.jpg",
   knows=["New Zealand gambling law","Online Casino Gambling Act 2026","Department of Internal Affairs licensing",
          "bonus terms and conditions","gambling taxation","responsible gambling policy","editorial standards"],
   short="Checks every claim on this site against a primary source before it publishes.",
   bio="Elizabeth read law at Victoria University of Wellington and spent a decade in regulatory and editorial roles "
       "before joining RNRV. Nothing publishes on this site until she has checked it: the complete terms behind every "
       "bonus figure, every payout time against the testing log, and every legal and tax claim against the "
       "legislation or the Department of Internal Affairs guidance it rests on. Where a figure could not be verified, "
       "the decision to write \"check current terms\" rather than estimate is hers."),
}
# Every page is written by Claire and fact-checked by Elizabeth. Older fragment
# front matter still names the previous bylines, so those keys alias across.
WRITER = "claire"
CHECKER = "elizabeth"
for _old in ("tane", "ana", "hemi", "team"):
    AUTHORS[_old] = AUTHORS[WRITER]

# ---------------------------------------------------------------- navigation
NAV = [
 ("Casinos", "/online-casinos/", [
   ("Best Online Casinos NZ", "/online-casinos/"),
   ("Licensed Online Casinos", "/licensed-online-casinos/"),
   ("New Casinos NZ", "/new-casinos-nz/"),
   ("Online Pokies", "/online-pokies/"),
   ("Casino Payout Percentages", "/casino-payout-percentages/"),
   ("Fast Payout Casinos", "/fast-payout-casinos/"),
   ("Live Casino", "/live-casino/"),
   ("Crypto Casinos NZ", "/crypto-casinos-nz/"),
   ("Casino Reviews", "/casino-reviews/"),
 ]),
 ("Bonuses", "/casino-bonus/", [
   ("Casino Bonus NZ", "/casino-bonus/"),
   ("No Deposit Bonus NZ", "/no-deposit-bonus/"),
 ]),
 ("Betting", "/online-betting/", [
   ("Online Betting NZ", "/online-betting/"),
   ("Best Sports Betting Sites", "/best-sports-betting-sites/"),
 ]),
 ("Guides", None, [
   ("Casino Payment Methods", "/casino-payment-methods/"),
   ("Tax on Gambling Winnings", "/gambling-winnings-tax-nz/"),
   ("How We Rate Casinos", "/how-we-rate-casinos/"),
   ("Responsible Gambling", "/responsible-gambling/"),
 ]),
 ("About", "/about/", None),
 ("Contact", "/contact/", None),
]

FOOTER = [
 ("Online Casinos", [
   ("Best Online Casinos NZ", "/online-casinos/"),
   ("Licensed Online Casinos NZ", "/licensed-online-casinos/"),
   ("New Casinos NZ", "/new-casinos-nz/"),
   ("Online Pokies NZ", "/online-pokies/"),
   ("Casino Payout Percentages", "/casino-payout-percentages/"),
   ("Fast Payout Casinos NZ", "/fast-payout-casinos/"),
   ("Live Casino NZ", "/live-casino/"),
   ("Crypto Casinos NZ", "/crypto-casinos-nz/"),
 ]),
 ("Bonuses &amp; Betting", [
   ("Casino Bonus NZ", "/casino-bonus/"),
   ("No Deposit Bonus NZ", "/no-deposit-bonus/"),
   ("Online Betting NZ", "/online-betting/"),
   ("Best Sports Betting Sites NZ", "/best-sports-betting-sites/"),
   ("Casino Payment Methods", "/casino-payment-methods/"),
 ]),
 ("Guides", [
   ("Casino Reviews", "/casino-reviews/"),
   ("Tax on Gambling Winnings NZ", "/gambling-winnings-tax-nz/"),
   ("How We Rate Casinos", "/how-we-rate-casinos/"),
   ("Responsible Gambling", "/responsible-gambling/"),
 ]),
 ("Company", [
   ("About Us", "/about/"),
   ("Contact Us", "/contact/"),
   ("Our Authors", "/authors/"),
   ("Terms and Conditions", "/terms/"),
   ("Privacy Policy", "/privacy/"),
   ("Cookie Policy", "/cookie-policy/"),
 ]),
]

# ---------------------------------------------------------------- icons
IC = {
 "star":  '<path d="M12 3l2.6 5.3 5.9.9-4.3 4.1 1 5.8L12 16.9 6.8 19.2l1-5.8L3.5 9.2l5.9-.9z"/>',
 "bolt":  '<path d="M13 2 3 14h7l-1 8 10-12h-7z"/>',
 "warn":  '<path d="M10.3 3.6 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.6a2 2 0 0 0-3.4 0z"/><path d="M12 9v4M12 17h.01"/>',
 "info":  '<circle cx="12" cy="12" r="9"/><path d="M12 8h.01M11 12h1v4h1"/>',
 "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 "check": '<path d="M20 6 9 17l-5-5"/>',
 "cross": '<path d="M18 6 6 18M6 6l12 12"/>',
 "shield":'<path d="M12 3l7 3v6c0 4.5-3 7.9-7 9-4-1.1-7-4.5-7-9V6z"/>',
 "coin":  '<circle cx="12" cy="12" r="9"/><path d="M15 9.5c-.6-.9-1.7-1.5-3-1.5-1.7 0-3 .9-3 2s1.3 2 3 2 3 .9 3 2-1.3 2-3 2c-1.3 0-2.4-.6-3-1.5"/>',
}
def ic(k, cls="ic"):
    return (f'<span class="{cls}" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{IC[k]}</svg></span>')

# ---------------------------------------------------------------- helpers
MISSING = set()

def aff(slug, kind="casino"):
    op = OPS[slug]
    url = op["sportsLink"] if kind == "sports" else op["casinoLink"]
    url = url or op["casinoLink"] or op["sportsLink"]
    if not url:
        MISSING.add(op["name"]); return "/casino-reviews/"
    return url

def op_logo(slug, sports=False):
    op = OPS.get(slug) or {}
    if sports and op.get("logoSports"):
        return op["logoSports"]
    return op.get("logo", "")

def resolve_tokens(s):
    s = re.sub(r"\{\{(aff|affs):([a-z0-9\-]+)\}\}",
               lambda m: html.escape(aff(m.group(2), "sports" if m.group(1) == "affs" else "casino"), quote=True), s)
    s = re.sub(r"\{\{op:([a-z0-9\-]+):([A-Za-z]+)\}\}",
               lambda m: html.escape(str(OPS[m.group(1)].get(m.group(2), ""))), s)
    s = s.replace("{{updated}}", UPDATED_HUMAN)
    s = s.replace("{{month}}", MONTH_YEAR)
    return s

def cta(slug, label=None, kind="casino", block=False, cls="btn-lime"):
    op = OPS[slug]
    label = label or f"Visit {op['name']}"
    b = " btn-block" if block else ""
    return (f'<a class="btn {cls}{b}" href="{html.escape(aff(slug, kind), quote=True)}" '
            f'target="_blank" rel="nofollow sponsored noopener">{label}</a>')

def stars(rating):
    """Five-star row from a 5-point rating, with a true half-fill overlay."""
    svg = f'<svg viewBox="0 0 24 24" fill="currentColor">{IC["star"]}</svg>'
    full = int(rating); frac = rating - full
    half = 0.25 <= frac < 0.75
    if frac >= 0.75:
        full += 1
    out = []
    for i in range(5):
        if i < full:
            out.append(f'<span class="st st-on">{svg}</span>')
        elif i == full and half:
            out.append(f'<span class="st st-half">{svg}<span class="st-h">{svg}</span></span>')
        else:
            out.append(f'<span class="st">{svg}</span>')
    return f'<span class="stars" role="img" aria-label="Rated {rating} out of 5">{"".join(out)}</span>'

# ---------------------------------------------------------------- blocks
def toplist(slugs, kind="casino", intro=None, heading=None, hid="toplist"):
    """Ranked operator cards — the primary conversion unit.

    One markup structure serves both layouts: a horizontal grid on desktop, and a
    stacked, centred card on mobile (rank, badge, logo, name, tagline, score bar,
    offer box, CTA, fine print).
    """
    rows = []
    for i, slug in enumerate(slugs, 1):
        op = OPS[slug]
        logo = op_logo(slug, sports=(kind == "sports"))
        bonus = op.get("welcomeSports") if kind == "sports" and op.get("welcomeSports") else op["welcome"]
        short = op.get("welcomeSports") if kind == "sports" and op.get("welcomeSports") else op.get("short", bonus)
        badge = op.get("badge") or ("Editor's #1" if i == 1 else "")
        pct = round(op["rating"] / 5 * 100)
        aff_url = html.escape(aff(slug, kind), quote=True)
        feats = []
        if op.get("payout"):   feats.append((ic("bolt"), "Payout", op["payout"]))
        if op.get("wagering"): feats.append((ic("coin"), "Wagering", op["wagering"]))
        if op.get("minDep"):   feats.append((ic("info"), "Min deposit", op["minDep"]))
        if op.get("licence"):  feats.append((ic("shield"), "Licence", op["licence"]))
        featc = "".join(f'<div class="tl-feat">{i_}<span class="k">{k}</span><span class="v">{v}</span></div>'
                        for i_, k, v in feats)
        badge_html = f'<span class="tl-badge">{badge}</span>' if badge else ""
        rows.append(
            f'<article class="tl-card" id="rank-{i}">'
            f'<div class="tl-rank"><span>{i:02d}</span></div>'
            f'{badge_html}'
            f'<div class="tl-brand">'
            f'<a class="tl-logo" href="/casino-reviews/{op["slug"]}/" aria-label="{op["name"]} review">'
            f'<img src="{logo}" alt="{op["name"]} logo" width="150" height="64" loading="lazy" decoding="async"></a>'
            f'<p class="tl-name">{op["name"]}</p>'
            f'<p class="tl-tag">{op.get("tag", "")}</p>'
            f'<div class="tl-bar" role="img" aria-label="Our score: {op["rating"]} out of 5">'
            f'<span style="width:{pct}%"></span></div>'
            f'<div class="tl-scorerow"><span class="tl-scorelab">Our score</span>'
            f'<b>{op["rating"]}<span class="of5">/5</span></b></div>'
            f'</div>'
            f'<div class="tl-offer">'
            f'<a class="tl-offerbox" href="{aff_url}" target="_blank" rel="nofollow sponsored noopener" '
            f'aria-label="Claim the welcome offer at {op["name"]}">'
            f'<span class="tl-label">Welcome offer</span>'
            f'<span class="tl-bonus">{short}</span>'
            f'<span class="tl-offercta">Claim this offer <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
            f'<path d="M5 12h13M13 6l6 6-6 6"/></svg></span>'
            f'</a>'
            f'<p class="tl-usp">{op["usp"]}</p>'
            f'<div class="tl-feats">{featc}</div>'
            f'</div>'
            f'<div class="tl-act">'
            f'<a class="btn btn-lime btn-block" href="{aff_url}" target="_blank" '
            f'rel="nofollow sponsored noopener" aria-label="Get bonus at {op["name"]}">Get bonus</a>'
            f'<a class="tl-read" href="/casino-reviews/{op["slug"]}/">Read the {op["name"]} review</a>'
            f'<p class="tl-fine">{op.get("fine", "18+. T&amp;Cs apply.")}</p>'
            f'</div>'
            f'</article>')
    h = f'<h2 id="{hid}">{heading}</h2>' if heading else ""
    p = f'<p class="lede">{intro}</p>' if intro else ""
    return (f'<section class="sec sec-tl"><div class="wrap">{h}{p}<div class="tl">{"".join(rows)}</div>'
            f'</div></section>')

def review_grid():
    """Card grid of every operator review, in overall rank order."""
    cards = []
    for slug in ORDER:
        op = OPS[slug]
        tags = []
        if op.get("casino"): tags.append("Casino")
        if op.get("sports"): tags.append("Sportsbook")
        if op.get("crypto"): tags.append("Crypto")
        tagh = "".join(f'<span class="chip">{t}</span>' for t in tags)
        warn = ('<p class="rv-warn">%s%s</p>' % (ic("warn"), op["watch"])) if op.get("watch") else ""
        cards.append(f'''<a class="card card-lnk rv-card" href="/casino-reviews/{op['slug']}/">
<div class="rv-top"><img src="{op_logo(slug)}" alt="{op['name']} logo" width="150" height="64" loading="lazy" decoding="async">
<div class="rv-score">{stars(op['rating'])}<b>{op['rating']}</b><span class="of5">/5</span></div></div>
<h3>{op['name']}</h3>
<p class="rv-bonus">{op['welcome']}</p>
<p>{op['usp']}</p>
{warn}
<div class="chips rv-chips">{tagh}</div>
<span class="more">Read the {op['name']} review &rarr;</span></a>''')
    return '<div class="grid g3 rv-grid">' + "".join(cards) + '</div>'

def faq_block(items, heading="Frequently asked questions", hid="faq"):
    qs = "".join(
        f'<details class="faq-i"><summary><span>{q}</span></summary><div class="faq-a">{a}</div></details>'
        for q, a in items)
    return (f'<section class="sec sec-faq"><div class="wrap"><h2 id="{hid}">{heading}</h2>'
            f'<div class="faq">{qs}</div></div></section>')

def faq_schema(items):
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": strip_tags(q),
         "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}} for q, a in items]}

def strip_tags(s):
    """Plain text for schema fields: drop tags, decode entities, collapse space."""
    s = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", s, flags=re.S | re.I)
    s = re.sub(r"</(p|div|li|h[1-6]|tr|br)>", " ", s, flags=re.I)
    s = re.sub(r"<[^>]+>", "", s)
    s = html.unescape(s)
    return re.sub(r"\s+", " ", s).strip()

# ---------------------------------------------------------------- chrome
LOGO_SVG = ('<svg class="mk" viewBox="0 0 36 36" aria-hidden="true">'
            '<rect width="36" height="36" rx="8" fill="var(--lime)"/>'
            '<path d="M11 26V10h7.2a4.6 4.6 0 0 1 1.2 9l4.1 7h-4.2l-3.6-6.6H14.7V26z" fill="var(--ink)"/>'
            '<path d="M14.7 13.2v3.9h3.4a1.95 1.95 0 0 0 0-3.9z" fill="var(--lime)"/></svg>')

def brandmark(tag=True):
    t = f'<span class="lg-tag">{TAGLINE}</span>' if tag else ""
    return (f'<span class="lg-lock">{LOGO_SVG}<span class="lg-word">RNRV</span></span>{t}')

def nav_html():
    caret = ('<svg viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">'
             '<path d="M3 4.5l3 3 3-3"/></svg>')
    out = ['<a class="skip" href="#main">Skip to content</a>',
           '<header class="nav"><div class="wrap">',
           f'<a class="lg" href="/" aria-label="{SITE} — NZ online casino and betting guide">{brandmark()}</a>',
           '<nav class="nav-links" aria-label="Main">']
    for label, href, kids in NAV:
        if not kids:
            out.append(f'<a href="{href}">{label}</a>')
        else:
            trig = (f'<a class="nav-trig" href="{href}">{label} {caret}</a>' if href
                    else f'<span class="nav-trig" tabindex="0" role="button">{label} {caret}</span>')
            links = "".join(f'<a href="{h}">{l}</a>' for l, h in kids)
            out.append(f'<div class="nav-item">{trig}<div class="nav-dd"><div class="nav-dd-in">{links}</div></div></div>')
    out.append('</nav>')
    out.append('<a class="btn btn-lime btn-sm nav-cta" href="#toplist">Top casinos</a>')
    out.append('<details class="menu"><summary aria-label="Open menu"><svg viewBox="0 0 24 24" width="22" height="22" '
               'fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M3 6h18M3 12h18M3 18h18"/>'
               '</svg></summary><div class="menu-panel">')
    for label, href, kids in NAV:
        if kids:
            out.append(f'<b>{label}</b>')
            out += [f'<a href="{h}">{l}</a>' for l, h in kids]
        else:
            out.append(f'<a href="{href}">{label}</a>')
    out.append('<b>Company</b><a href="/authors/">Our Authors</a><a href="/responsible-gambling/">Responsible Gambling</a>')
    out.append('</div></details></div></header>')
    return "".join(out)

RG_FOOT = (
 '<strong>18+ only. Gambling can be harmful.</strong> The <strong>Online Casino Gambling Act 2026</strong> came into '
 'force on 1 May 2026 and the Department of Internal Affairs is awarding up to <strong>15 online casino licences</strong>. '
 'From <strong>1 December 2026</strong> only operators holding a licence, or with an application under consideration, may '
 'continue to serve New Zealanders. The casino sites listed on RNRV are currently licensed offshore. Sports and racing '
 'betting is separate: under the Racing Industry Amendment Act 2025, <strong>TAB NZ is the only operator legally '
 'permitted to take betting from New Zealand</strong>. Never gamble money you cannot afford to lose. '
 'Free, confidential help 24/7: <strong>Gambling Helpline 0800 654 655</strong> (free text 8006), '
 '<strong>Problem Gambling Foundation 0800 664 262</strong>, or <strong>Need to Talk 1737</strong>. '
 'RNRV earns affiliate commission from some operators listed. It never changes our rankings.')

def foot_html():
    cols = ""
    for t, links in FOOTER:
        items = "".join('<a href="%s">%s</a>' % (h, l) for l, h in links)
        cols += '<div class="ft-col"><b>%s</b>%s</div>' % (t, items)
    year = datetime.date.today().year
    return f'''<footer class="ft"><div class="wrap">
<div class="ft-top">
<div class="ft-brand">
<a class="lg lg-ft" href="/" aria-label="{SITE}">{brandmark()}</a>
<p>New Zealand's independent guide to online casinos, pokies and betting. We open real accounts, deposit real
New Zealand dollars and time every withdrawal, so the rankings on this site reflect what actually happened
&mdash; not what an operator claims in its marketing.</p>
<div class="ft-badges">
<span class="ft-badge">{ic("shield")}18+ only</span>
<span class="ft-badge">{ic("check")}NZD tested</span>
<span class="ft-badge">{ic("clock")}Updated {UPDATED_HUMAN}</span>
</div>
</div>
<div class="ft-cols">{cols}</div>
</div>
<div class="ft-rg">{RG_FOOT}</div>
<div class="ft-help">
<a href="https://www.gamblinghelpline.co.nz/" rel="noopener nofollow" target="_blank">Gambling Helpline</a>
<a href="https://www.pgf.nz/" rel="noopener nofollow" target="_blank">Problem Gambling Foundation</a>
<a href="https://www.dia.govt.nz/gambling" rel="noopener nofollow" target="_blank">Department of Internal Affairs</a>
<a href="https://www.choicenotchance.org.nz/" rel="noopener nofollow" target="_blank">Choice Not Chance</a>
</div>
<div class="ft-legal"><span>&copy; {year} {SITE}. All rights reserved.</span>
<span><a href="/terms/">Terms</a> &middot; <a href="/privacy/">Privacy</a> &middot;
<a href="/cookie-policy/">Cookies</a> &middot; <a href="/responsible-gambling/">Responsible Gambling</a> &middot;
<a href="/authors/">Authors</a> &middot; <a href="/about/">About Us</a> &middot; <a href="/contact/">Contact Us</a></span></div>
</div></footer>'''

# ---------------------------------------------------------------- hero
def hero_html(fm, body_lede):
    a = AUTHORS[fm.get("author", WRITER)]
    ck = AUTHORS[CHECKER]
    crumbs = ""
    if fm.get("crumbs"):
        parts = ['<a href="/">Home</a>']
        for i, pair in enumerate(fm["crumbs"]):
            n, h = pair
            parts.append('<span aria-hidden="true">/</span>')
            parts.append(f'<span aria-current="page">{n}</span>' if i == len(fm["crumbs"]) - 1
                         else f'<a href="{h}">{n}</a>')
        crumbs = f'<nav class="crumbs" aria-label="Breadcrumb">{"".join(parts)}</nav>'
    stats = ""
    if fm.get("stats"):
        stats = '<div class="hero-stats">' + "".join(
            f'<div class="hs"><span class="k">{k}</span><span class="v">{v}</span></div>'
            for k, v in fm["stats"]) + '</div>'
    pills = ""
    if fm.get("pills"):
        pills = '<div class="hero-pills">' + "".join(
            f'<span class="pill">{ic("check")}{p}</span>' for p in fm["pills"]) + '</div>'
    ctas = ""
    if fm.get("ctas"):
        ctas = '<div class="hero-ctas">' + "".join(
            f'<a class="btn {c}" href="{h}">{l}</a>' for l, h, c in fm["ctas"]) + '</div>'
    card = fm.get("heroCard")
    cardhtml = ""
    if card:
        op = OPS[card["op"]]
        kind = card.get("kind", "casino")
        # Prefer a punchy headline: explicit override > sports offer > short form > full text
        offer = card.get("offer")
        if not offer and kind == "sports" and op.get("welcomeSports"):
            offer = op["welcomeSports"]
        if not offer:
            offer = op.get("short") or op["welcome"]
        cardhtml = f'''<aside class="hero-card" aria-label="Editor's top pick">
<div class="hc-band">{card.get("band", "Editor's #1 pick for New Zealand")}</div>
<div class="hc-body">
<div class="hc-logobox"><img class="hc-logo" src="{op_logo(card["op"], sports=(kind=="sports"))}" alt="{op['name']} logo" width="150" height="64" loading="eager" decoding="async"></div>
<p class="hc-name">{op['name']}</p>
<p class="hc-sub">{card.get("sub", op['usp'])}</p>
<a class="hc-offerbox" href="{html.escape(aff(card["op"], kind), quote=True)}" target="_blank" rel="nofollow sponsored noopener" aria-label="Claim the welcome offer at {op['name']}"><span class="hc-offerlab">Exclusive welcome offer</span><span class="hc-offer">{offer}</span><span class="hc-offercta">Claim this offer <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h13M13 6l6 6-6 6"/></svg></span></a>
<div class="hc-score">{stars(op['rating'])}<b>{op['rating']}</b><span class="of5">/5</span></div>
<p class="hc-meta">{card.get("meta", "")}</p>
{cta(card["op"], label=f"Visit {op['name']}", kind=kind, block=True)}
<p class="hc-fine">18+. New customers only. T&amp;Cs apply.</p>
</div></aside>'''
    return f'''<section class="hero"><div class="wrap"><div class="hero-grid"><div class="hero-main">
{crumbs}
<p class="eyebrow">{ic("clock")}Updated {UPDATED_HUMAN} &middot; New Zealand</p>
<h1>{fm["h1"]}</h1>
<p class="hero-lede">{body_lede}</p>
{stats}{ctas}{pills}
<div class="byline">
<a class="av" href="/authors/#{a['slug']}" aria-label="{strip_tags(a['name'])}, author"><img src="{a['photo']}" srcset="{a['photo']} 1x, {a['photo'].replace('.jpg','@2x.jpg')} 2x" alt="{strip_tags(a['name'])}" width="44" height="44" loading="eager" decoding="async"></a>
<span class="by-txt">By <a href="/authors/#{a['slug']}"><b>{a['name']}</b></a>, {a['role']}
<span class="by-sub">Fact-checked by <a href="/authors/#{ck['slug']}"><b>{ck['name']}</b></a> &middot; <a href="/how-we-rate-casinos/">How we review</a></span></span>
</div>
</div>{cardhtml}</div></div></section>'''

def disclosures_html(fm):
    """Site and page level disclosures, consolidated at the foot of the page.

    Per-offer terms (wagering, minimum deposit, 18+) stay attached to each offer
    and CTA, where advertising standards expect them. What moves down here is
    the page-level material: the affiliate disclosure, the general terms notice
    and the responsible gambling line.
    """
    has_affiliate = bool(fm.get("toplist") or fm.get("heroCard") or fm.get("reviewOf"))
    if not has_affiliate:
        return ""
    return f'''<section class="sec sec-disc"><div class="wrap"><div class="disc">
<h2 id="disclosures">Disclosures</h2>
<div class="disc-grid">
<div class="disc-item"><h3>{ic("coin")}How we are funded</h3>
<p>RNRV earns affiliate commission when a reader opens an account through a link on this page. That is the
entire business model, and we would rather state it than bury it.</p>
<p>It does not buy placement. No operator has paid for a position, seen a page before publication, or had
editorial input. Our commission rates are published against our rankings on
<a href="/how-we-rate-casinos/#money">how we rate casinos</a> so the claim is checkable rather than asserted.</p></div>
<div class="disc-item"><h3>{ic("info")}Offers and terms</h3>
<p>18+. New customers only. Wagering requirements and full terms apply to every offer shown on this page.
Bonus terms change without notice &mdash; always read the operator\'s own current terms before claiming.</p>
<p>Figures here were verified in {{{{month}}}} and are re-checked monthly. Where we could not verify a figure
we say so rather than estimate.</p></div>
<div class="disc-item"><h3>{ic("warn")}Gambling carries risk</h3>
<p>Every game referenced on this site has a negative expected value &mdash; it returns less than it takes.
A higher RTP makes the entertainment cheaper, not profitable. Never gamble money you cannot afford to lose.</p>
<p>Free, confidential help 24/7: <strong>Gambling Helpline 0800 654 655</strong> (free text 8006),
<strong>Problem Gambling Foundation 0800 664 262</strong>, or <strong>Need to Talk 1737</strong>.
See <a href="/responsible-gambling/">responsible gambling</a>.</p></div>
</div></div></div></section>'''

# ---------------------------------------------------------------- CSS
CSS = r"""
*,*::before,*::after{box-sizing:border-box}
:root{
--ink:#12151A;--ink-2:#1A1F26;--ink-3:#242B34;--ink-4:#333C48;
--lime:#C8FF3D;--lime-2:#A8E024;--lime-3:#E8FFA8;
--paper:#F7F7F4;--white:#fff;--line:#E4E4DE;--line-2:#D2D2CA;
--text:#1A1F26;--muted:#5E6672;--muted-2:#7C8492;
--ok:#137A4B;--ok-bg:#E7F6EE;--warn:#9A5B00;--warn-bg:#FFF3DF;--bad:#A32A2A;--bad-bg:#FBEAEA;
--h:'Archivo',-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;
--b:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;
--m:'JetBrains Mono',ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
--wrap:1200px;--r:14px;--r-sm:9px;
--sh:0 1px 2px rgba(18,21,26,.05),0 8px 24px -12px rgba(18,21,26,.16);
--sh-lg:0 2px 4px rgba(18,21,26,.06),0 22px 48px -20px rgba(18,21,26,.24);
}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth;scroll-padding-top:84px}
body{margin:0;background:var(--paper);color:var(--text);font-family:var(--b);font-size:17px;line-height:1.68;
-webkit-font-smoothing:antialiased;overflow-x:hidden}
img{max-width:100%;height:auto;display:block}
a{color:#15603C;text-underline-offset:.18em;text-decoration-thickness:1px}
a:hover{color:#0E4429}
.wrap{width:100%;max-width:var(--wrap);margin:0 auto;padding:0 22px}
.skip{position:absolute;left:-9999px;top:0;background:var(--lime);color:var(--ink);padding:10px 16px;z-index:99;font-weight:700}
.skip:focus{left:8px;top:8px}
h1,h2,h3,h4,h5,h6{font-family:var(--h);font-weight:700;letter-spacing:-.018em;line-height:1.18;color:var(--ink);margin:0}
h1{font-size:clamp(2rem,1.25rem + 2.6vw,3.15rem);letter-spacing:-.03em}
h2{font-size:clamp(1.5rem,1.1rem + 1.5vw,2.15rem);letter-spacing:-.025em;margin:0 0 .5em}
h3{font-size:clamp(1.18rem,1.03rem + .6vw,1.42rem);margin:2em 0 .45em}
h4{font-size:1.06rem;margin:1.6em 0 .35em}
h5{font-size:.96rem;margin:1.4em 0 .3em;text-transform:uppercase;letter-spacing:.06em;color:var(--muted)}
p{margin:0 0 1.05em}
.mono{font-family:var(--m);font-size:.82em;letter-spacing:-.01em}
.ic{display:inline-flex;width:1em;height:1em;vertical-align:-.12em;margin-right:.4em;flex:none}
.ic svg{width:100%;height:100%}

/* ---------- buttons ---------- */
.btn{display:inline-flex;align-items:center;justify-content:center;gap:.5em;font-family:var(--h);font-weight:700;
font-size:.95rem;letter-spacing:-.01em;padding:13px 22px;border-radius:var(--r-sm);text-decoration:none;
border:1.5px solid transparent;cursor:pointer;transition:transform .12s ease,box-shadow .12s ease,background .12s ease;
white-space:nowrap;line-height:1.2}
.btn:hover{transform:translateY(-1px)}
.btn-lime{background:var(--lime);color:var(--ink);box-shadow:0 2px 0 var(--lime-2)}
.btn-lime:hover{background:var(--lime-3);color:var(--ink);box-shadow:0 4px 0 var(--lime-2)}
.btn-dark{background:var(--ink);color:#fff}
.btn-dark:hover{background:var(--ink-3);color:#fff}
.btn-ghost{background:transparent;color:var(--ink);border-color:var(--line-2)}
.btn-ghost:hover{background:#fff;color:var(--ink);border-color:var(--ink)}
.btn-ghost-l{background:transparent;color:#fff;border-color:rgba(255,255,255,.34)}
.btn-ghost-l:hover{background:rgba(255,255,255,.1);color:#fff}
.btn-block{display:flex;width:100%}
.btn-sm{padding:9px 15px;font-size:.85rem}

/* ---------- nav ---------- */
.nav{background:var(--ink);position:sticky;top:0;z-index:50;border-bottom:1px solid rgba(255,255,255,.07)}
.nav>.wrap{display:flex;align-items:center;gap:18px;min-height:66px}
.lg{display:flex;align-items:center;gap:11px;text-decoration:none;flex:none}
.lg-lock{display:inline-flex;align-items:center;gap:9px}
.lg .mk{width:31px;height:31px;flex:none}
.lg-word{font-family:var(--h);font-weight:800;font-size:1.34rem;letter-spacing:.02em;color:#fff}
.lg-tag{font-size:.68rem;font-weight:600;color:var(--lime);letter-spacing:.05em;text-transform:uppercase;
border-left:1px solid rgba(255,255,255,.2);padding-left:11px;max-width:9.5em;line-height:1.25}
.nav-links{display:flex;align-items:center;gap:2px;margin-left:auto}
.nav-links>a,.nav-trig{display:inline-flex;align-items:center;gap:.35em;padding:9px 12px;border-radius:8px;
color:rgba(255,255,255,.86);text-decoration:none;font-size:.93rem;font-weight:500;cursor:pointer}
.nav-links>a:hover,.nav-trig:hover{background:rgba(255,255,255,.09);color:#fff}
.nav-trig svg{width:11px;height:11px;opacity:.65}
.nav-item{position:relative}
.nav-dd{position:absolute;top:100%;left:0;padding-top:8px;opacity:0;visibility:hidden;transform:translateY(-5px);
transition:.15s ease;z-index:60}
.nav-item:hover .nav-dd,.nav-item:focus-within .nav-dd{opacity:1;visibility:visible;transform:none}
.nav-dd-in{background:#fff;border:1px solid var(--line);border-radius:12px;box-shadow:var(--sh-lg);padding:7px;min-width:248px}
.nav-dd-in a{display:block;padding:9px 13px;border-radius:7px;color:var(--text);text-decoration:none;font-size:.91rem;font-weight:500}
.nav-dd-in a:hover{background:var(--paper);color:var(--ink)}
.nav-cta{flex:none}
.menu{display:none;margin-left:auto}
.menu summary{list-style:none;color:#fff;padding:8px;cursor:pointer;display:flex}
.menu summary::-webkit-details-marker{display:none}
.menu-panel{position:absolute;left:0;right:0;top:100%;background:var(--ink-2);border-top:1px solid rgba(255,255,255,.1);
padding:14px 22px 20px;max-height:76vh;overflow:auto}
.menu-panel a{display:block;padding:9px 0;color:rgba(255,255,255,.88);text-decoration:none;border-bottom:1px solid rgba(255,255,255,.07)}
.menu-panel b{display:block;margin:15px 0 4px;color:var(--lime);font-size:.72rem;text-transform:uppercase;letter-spacing:.08em}

/* ---------- hero ---------- */
.hero{background:var(--ink);color:#fff;padding:34px 0 46px;position:relative;overflow:hidden}
.hero::after{content:"";position:absolute;right:-160px;top:-160px;width:520px;height:520px;border-radius:50%;
background:radial-gradient(circle,rgba(200,255,61,.16),transparent 66%);pointer-events:none}
.hero-grid{display:grid;grid-template-columns:minmax(0,1.55fr) minmax(0,.85fr);gap:40px;align-items:start;position:relative;z-index:1}
.hero h1{color:#fff;margin:0 0 .4em}
.crumbs{font-size:.8rem;color:rgba(255,255,255,.6);margin-bottom:16px;display:flex;flex-wrap:wrap;gap:.45em;align-items:center}
.crumbs a{color:rgba(255,255,255,.72);text-decoration:none}
.crumbs a:hover{color:var(--lime)}
.crumbs span[aria-hidden]{opacity:.42}
.eyebrow{display:inline-flex;align-items:center;font-family:var(--m);font-size:.74rem;text-transform:uppercase;
letter-spacing:.1em;color:var(--lime);margin:0 0 12px;font-weight:600}
.hero-lede{font-size:1.12rem;line-height:1.62;color:rgba(255,255,255,.84);max-width:60ch;margin:0 0 22px}
.hero-stats{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:10px;margin:0 0 22px;max-width:560px}
.hs{background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.11);border-radius:10px;padding:11px 12px}
.hs .k{display:block;font-size:.68rem;text-transform:uppercase;letter-spacing:.07em;color:rgba(255,255,255,.58);margin-bottom:3px}
.hs .v{display:block;font-family:var(--h);font-weight:700;font-size:1.14rem;color:var(--lime)}
.hero-ctas{display:flex;flex-wrap:wrap;gap:11px;margin:0 0 20px}
.hero-pills{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 22px}
.pill{display:inline-flex;align-items:center;font-size:.79rem;font-weight:500;color:rgba(255,255,255,.8);
background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:99px;padding:5px 12px}
.pill .ic{color:var(--lime);width:.9em;height:.9em}
.byline{display:flex;align-items:center;gap:12px;padding:15px 0 0;border-top:1px solid rgba(255,255,255,.12);margin-bottom:14px}
.av{width:44px;height:44px;border-radius:50%;overflow:hidden;flex:none;display:block;
background:var(--ink-3);box-shadow:0 0 0 2px rgba(200,255,61,.55)}
.av img{width:100%;height:100%;object-fit:cover;display:block}
.by-txt{font-size:.88rem;color:rgba(255,255,255,.78);line-height:1.45}
.by-txt a{color:#fff;text-decoration:none;border-bottom:1px solid rgba(200,255,61,.55)}
.by-txt a:hover{color:var(--lime)}
.by-sub{display:block;font-size:.79rem;color:rgba(255,255,255,.52);margin-top:2px}
.by-sub a{border-bottom-color:rgba(255,255,255,.25)}
.hero-fine{font-size:.76rem;color:rgba(255,255,255,.46);line-height:1.5;max-width:66ch;margin:0}
.hero-fine strong{color:rgba(255,255,255,.72)}
.hero-card{background:#fff;color:var(--text);border-radius:var(--r);overflow:hidden;box-shadow:var(--sh-lg);position:sticky;top:84px}
.hc-band{background:var(--lime);color:var(--ink);font-family:var(--h);font-weight:700;font-size:.76rem;
text-transform:uppercase;letter-spacing:.07em;padding:9px 18px;text-align:center}
.hc-body{padding:20px 20px 18px;text-align:center}
.hc-logobox{display:block;background:#fff;border:1px solid var(--line);border-radius:10px;
padding:8px 14px;margin:0 auto 13px;max-width:212px}
.hc-logo{max-height:58px;max-width:100%;width:auto;margin:0 auto;object-fit:contain}
.hc-name{font-family:var(--h);font-weight:700;font-size:1.24rem;color:var(--ink);margin:0 0 2px}
.hc-sub{font-size:.86rem;color:var(--muted);margin:0 0 14px;line-height:1.45}
.hc-offerbox{display:block;position:relative;background:var(--ink);border-radius:12px;
padding:14px 14px 13px;margin:0 0 14px;text-decoration:none;cursor:pointer;
box-shadow:0 10px 26px -12px rgba(18,21,26,.85);transition:transform .13s ease,box-shadow .13s ease}
.hc-offerbox:hover{transform:translateY(-2px);box-shadow:0 14px 30px -12px rgba(18,21,26,.95)}
.hc-offerbox:focus-visible{outline:3px solid var(--lime);outline-offset:3px}
.hc-offerlab{display:block;font-family:var(--h);font-size:.64rem;font-weight:800;text-transform:uppercase;
letter-spacing:.13em;color:var(--lime);margin-bottom:6px}
.hc-offerlab::before{content:"";display:inline-block;width:5px;height:5px;border-radius:50%;
background:var(--lime);vertical-align:.17em;margin-right:.55em}
.hc-offer{display:block;font-family:var(--h);font-weight:800;font-size:1.2rem;color:var(--lime);margin:0;
line-height:1.24;letter-spacing:-.02em;text-wrap:balance}
.hc-offercta{display:inline-flex;align-items:center;gap:.4em;margin-top:9px;font-family:var(--h);
font-weight:700;font-size:.78rem;color:#fff;border-bottom:1px solid rgba(255,255,255,.32);padding-bottom:2px}
.hc-offercta svg{width:13px;height:13px;transition:transform .13s ease}
.hc-offerbox:hover .hc-offercta svg{transform:translateX(3px)}
.hc-score{display:flex;align-items:center;justify-content:center;gap:6px;margin:0 0 12px;font-size:.92rem}
.hc-score b{font-family:var(--h)}
.hc-score .of5{color:var(--muted);font-size:.85rem}
.hc-meta{font-size:.8rem;color:var(--muted);margin:0 0 14px;line-height:1.5}
.hc-fine{font-size:.71rem;color:var(--muted-2);margin:10px 0 0}

/* ---------- stars ---------- */
.stars{display:inline-flex;gap:1px;flex:none}
.st{position:relative;width:15px;height:15px;display:inline-block;color:var(--line-2);flex:none}
.st svg{width:15px;height:15px;display:block}
.st-on{color:#E8A800}
.st-half>.st-h{position:absolute;inset:0;width:50%;overflow:hidden;color:#E8A800;display:block}

/* ---------- sections ---------- */
.sec{padding:52px 0}
.sec-alt{background:#fff;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.sec-ink{background:var(--ink);color:rgba(255,255,255,.85)}
.sec-ink h2,.sec-ink h3,.sec-ink h4{color:#fff}
.sec-ink a{color:var(--lime)}
.sec>.wrap>h2{scroll-margin-top:88px}
.lede{font-size:1.08rem;color:var(--muted);max-width:74ch;margin:0 0 26px}
.sec-ink .lede{color:rgba(255,255,255,.72)}
.prose{max-width:none}
.prose>p,.prose>ul,.prose>ol{max-width:80ch}
.prose h2{margin-top:2.1em;scroll-margin-top:88px}
.prose h3{scroll-margin-top:88px}
.prose>*:first-child{margin-top:0}
.prose ul,.prose ol{margin:0 0 1.15em;padding-left:1.3em}
.prose li{margin:0 0 .45em}
.prose ul{list-style:none;padding-left:0}
.prose ul>li{position:relative;padding-left:1.5em}
.prose ul>li::before{content:"";position:absolute;left:.3em;top:.72em;width:6px;height:6px;border-radius:50%;background:var(--lime-2)}
.prose ol{padding-left:1.4em}
.prose ol>li::marker{font-family:var(--h);font-weight:700;color:var(--ink)}
.prose strong{font-weight:650;color:var(--ink)}
.sec-ink .prose strong{color:#fff}

/* ---------- toplist ---------- */
.sec-tl{padding-top:44px}
.tl{display:flex;flex-direction:column;gap:14px}
.tl-card{background:#fff;border:1px solid var(--line);border-radius:var(--r);box-shadow:var(--sh);
display:grid;grid-template-columns:58px minmax(0,225px) minmax(0,1fr) minmax(0,250px);gap:20px;
padding:20px 22px 20px 0;align-items:center;position:relative;scroll-margin-top:88px;
transition:box-shadow .15s ease}
.tl-card:hover{box-shadow:var(--sh-lg)}
.tl-card:first-child{border-color:var(--lime-2);border-width:2px}
.tl-rank{display:flex;align-items:center;justify-content:center;align-self:stretch;background:var(--paper);
border-right:1px solid var(--line);border-radius:var(--r) 0 0 var(--r);font-family:var(--h);font-weight:800;
font-size:1.3rem;color:var(--muted-2);letter-spacing:-.03em}
.tl-card:first-child .tl-rank{background:var(--lime);color:var(--ink)}
.tl-badge{position:absolute;top:10px;right:14px;font-size:.66rem;font-weight:800;text-transform:uppercase;
letter-spacing:.08em;background:var(--lime);color:var(--ink);padding:4px 11px;border-radius:99px;
font-family:var(--h);white-space:nowrap;z-index:2}
.tl-brand{text-align:center;min-width:0}
.tl-logo{display:block;background:#fff;border:1px solid var(--line);border-radius:10px;padding:7px 10px;margin-bottom:9px}
.tl-logo img{max-height:56px;max-width:100%;width:auto;margin:0 auto;object-fit:contain}
.tl-name{font-family:var(--h);font-weight:700;font-size:1rem;color:var(--ink);margin:0 0 6px;line-height:1.25}
.tl-tag{display:none}
.tl-bar{height:7px;border-radius:99px;background:var(--line);overflow:hidden;margin:0 0 7px}
.tl-bar>span{display:block;height:100%;border-radius:99px;
background:linear-gradient(90deg,var(--lime-2),var(--lime))}
.tl-scorerow{display:flex;align-items:baseline;justify-content:space-between;gap:8px;font-size:.86rem}
.tl-scorelab{color:var(--muted-2)}
.tl-scorerow b{font-family:var(--h);font-size:1.02rem;color:var(--ink)}
.tl-scorerow .of5{color:var(--muted-2);font-size:.8rem;font-weight:500}
.tl-offer{min-width:0}
.tl-offerbox{display:block;background:#F6FFE4;border:1px solid #DFF3AE;border-radius:10px;
padding:11px 14px;margin:0 0 10px;text-decoration:none;cursor:pointer;
transition:background .13s ease,border-color .13s ease,transform .13s ease}
.tl-offerbox:hover{background:#EEFFCE;border-color:var(--lime-2);transform:translateY(-1px)}
.tl-offerbox:focus-visible{outline:3px solid var(--lime-2);outline-offset:2px}
.tl-offercta{display:inline-flex;align-items:center;gap:.35em;margin-top:7px;font-family:var(--h);
font-weight:700;font-size:.75rem;color:#4F6B0A;border-bottom:1px solid rgba(79,107,10,.3);padding-bottom:1px}
.tl-offercta svg{width:12px;height:12px;transition:transform .13s ease}
.tl-offerbox:hover .tl-offercta svg{transform:translateX(3px)}
.tl-label{display:block;font-size:.64rem;text-transform:uppercase;letter-spacing:.1em;color:#5E7C10;
font-weight:800;font-family:var(--h);margin-bottom:4px}
.tl-label::before{content:"";display:inline-block;width:5px;height:5px;border-radius:50%;
background:#8FB61C;vertical-align:.15em;margin-right:.5em}
.tl-bonus{display:block;font-family:var(--h);font-weight:700;font-size:1.02rem;color:var(--ink);margin:0;line-height:1.32}
.tl-usp{font-size:.89rem;color:var(--muted);margin:0 0 11px;line-height:1.5}
.tl-feats{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:7px 16px}
.tl-feat{display:flex;align-items:baseline;gap:.3em;font-size:.79rem;line-height:1.4;color:var(--muted)}
.tl-feat .ic{color:var(--lime-2);width:.88em;height:.88em;align-self:center}
.tl-feat .k{font-weight:650;color:var(--ink);white-space:nowrap}
.tl-feat .v{color:var(--muted)}
.tl-act{text-align:center;min-width:0}
.tl-read{display:block;margin-top:9px;font-size:.84rem;color:var(--muted);text-decoration:none;
border-bottom:1px solid var(--line-2);padding-bottom:1px}
.tl-read:hover{color:var(--ink);border-color:var(--ink)}
.tl-fine{font-size:.71rem;color:var(--muted-2);margin:9px 0 0;line-height:1.45}
/* ---------- page-foot disclosures ---------- */
.sec-disc{background:var(--paper);border-top:1px solid var(--line);padding:38px 0 44px}
.disc h2{font-size:1.12rem;margin:0 0 4px;letter-spacing:-.01em}
.disc h2::after{content:"";display:block;width:38px;height:3px;border-radius:2px;background:var(--lime-2);margin:9px 0 20px}
.disc-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:22px}
.disc-item h3{display:flex;align-items:center;font-family:var(--h);font-weight:700;font-size:.88rem;
color:var(--ink);margin:0 0 .5em;text-transform:uppercase;letter-spacing:.05em}
.disc-item h3 .ic{color:var(--muted-2);width:.95em;height:.95em}
.disc-item p{font-size:.82rem;line-height:1.6;color:var(--muted);margin:0 0 .7em}
.disc-item p:last-child{margin-bottom:0}
.disc-item strong{color:var(--ink)}

/* ---------- tables ---------- */
.tbl-wrap{overflow-x:auto;-webkit-overflow-scrolling:touch;margin:0 0 1.4em;border:1px solid var(--line);
border-radius:var(--r);background:#fff}
table{border-collapse:collapse;width:100%;font-size:.9rem;min-width:600px}
caption{text-align:left;font-size:.83rem;color:var(--muted);padding:12px 16px 0;caption-side:top}
th,td{padding:11px 15px;text-align:left;border-bottom:1px solid var(--line);vertical-align:top}
thead th{background:var(--ink);color:#fff;font-family:var(--h);font-weight:600;font-size:.78rem;
text-transform:uppercase;letter-spacing:.05em;white-space:nowrap;border-bottom:none}
tbody tr:last-child td{border-bottom:none}
tbody tr:nth-child(even){background:#FBFBF9}
td strong{color:var(--ink)}
.t-num{font-family:var(--m);font-size:.85em;white-space:nowrap}
.t-yes{color:var(--ok);font-weight:650}
.t-no{color:var(--bad);font-weight:650}

/* ---------- callouts ---------- */
.note{border-left:4px solid var(--lime-2);background:#fff;border-radius:0 var(--r-sm) var(--r-sm) 0;
padding:16px 20px;margin:0 0 1.4em;box-shadow:var(--sh)}
.note>*:last-child{margin-bottom:0}
.note-h{display:flex;align-items:center;font-family:var(--h);font-weight:700;font-size:.95rem;color:var(--ink);margin:0 0 .4em}
.note-warn{border-left-color:#E8A800;background:var(--warn-bg)}
.note-warn .note-h{color:var(--warn)}
.note-bad{border-left-color:#C0392B;background:var(--bad-bg)}
.note-bad .note-h{color:var(--bad)}
.note-ok{border-left-color:#1E9E63;background:var(--ok-bg)}
.note-ok .note-h{color:var(--ok)}

/* ---------- pros/cons ---------- */
.pc{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;margin:0 0 1.5em}
.pc-col{background:#fff;border:1px solid var(--line);border-radius:var(--r);padding:16px 20px}
.pc-col h4{margin:0 0 .6em;display:flex;align-items:center;font-size:.95rem}
.pc-pro h4{color:var(--ok)}
.pc-con h4{color:var(--bad)}
.pc-col ul{list-style:none;margin:0;padding:0}
.pc-col li{position:relative;padding-left:1.6em;margin:0 0 .5em;font-size:.91rem;line-height:1.5;color:var(--muted)}
.pc-col li::before{position:absolute;left:0;top:0;font-weight:700}
.pc-pro li::before{content:"+";color:var(--ok)}
.pc-con li::before{content:"\2212";color:var(--bad)}

/* ---------- cards / grids ---------- */
.grid{display:grid;gap:14px}
.g2{grid-template-columns:repeat(2,minmax(0,1fr))}
.g3{grid-template-columns:repeat(3,minmax(0,1fr))}
.g4{grid-template-columns:repeat(4,minmax(0,1fr))}
.card{background:#fff;border:1px solid var(--line);border-radius:var(--r);padding:20px 22px;box-shadow:var(--sh)}
.card h3{margin:0 0 .4em;font-size:1.08rem}
.card p:last-child{margin-bottom:0}
.card-lnk{text-decoration:none;color:inherit;display:block;transition:.15s ease}
.card-lnk:hover{box-shadow:var(--sh-lg);transform:translateY(-2px);color:inherit}
.card-lnk .more{font-family:var(--h);font-weight:700;font-size:.86rem;color:#15603C}
.kpi{background:#fff;border:1px solid var(--line);border-radius:var(--r);padding:18px 20px;text-align:center}
.kpi .v{display:block;font-family:var(--h);font-weight:800;font-size:1.75rem;color:var(--ink);line-height:1.1}
.kpi .k{display:block;font-size:.8rem;color:var(--muted);margin-top:5px}
.sec-ink .card,.sec-ink .kpi{background:var(--ink-2);border-color:rgba(255,255,255,.12)}
.sec-ink .kpi .v{color:var(--lime)}
.sec-ink .kpi .k,.sec-ink .card p{color:rgba(255,255,255,.72)}

/* ---------- review grid ---------- */
.rv-grid{margin:0 0 1.6em}
.rv-card{display:flex;flex-direction:column;padding:18px 20px}
.rv-top{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:12px}
.rv-top img{max-height:46px;width:auto;object-fit:contain;max-width:140px}
.rv-score{display:flex;align-items:center;gap:5px;font-size:.85rem;flex:none}
.rv-score b{font-family:var(--h)}
.rv-card h3{margin:0 0 .25em;font-size:1.05rem}
.rv-bonus{font-family:var(--h);font-weight:650;font-size:.92rem;color:var(--ink);margin:0 0 .5em;line-height:1.35}
.rv-card p{font-size:.88rem;color:var(--muted);margin:0 0 .6em;line-height:1.5}
.rv-warn{font-size:.82rem!important;color:var(--warn)!important;background:var(--warn-bg);border-radius:7px;padding:8px 10px}
.rv-warn .ic{color:var(--warn)}
.rv-chips{margin:auto 0 .7em}
.rv-chips .chip{font-size:.72rem;padding:3px 10px}

/* ---------- steps ---------- */
.steps{counter-reset:s;list-style:none;padding:0;margin:0 0 1.5em;display:grid;gap:12px}
.steps>li{counter-increment:s;position:relative;background:#fff;border:1px solid var(--line);border-radius:var(--r);
padding:16px 20px 16px 62px}
.steps>li::before{content:counter(s);position:absolute;left:18px;top:16px;width:30px;height:30px;border-radius:8px;
background:var(--lime);color:var(--ink);display:flex;align-items:center;justify-content:center;
font-family:var(--h);font-weight:800;font-size:.95rem}
.steps>li::marker{content:none}
.steps h4{margin:0 0 .3em;font-size:1rem}
.steps p{margin:0;font-size:.93rem;color:var(--muted)}

/* ---------- faq ---------- */
.faq{display:grid;gap:9px}
.faq-i{background:#fff;border:1px solid var(--line);border-radius:var(--r-sm);overflow:hidden}
.faq-i[open]{border-color:var(--line-2);box-shadow:var(--sh)}
.faq-i summary{list-style:none;cursor:pointer;padding:15px 48px 15px 20px;font-family:var(--h);font-weight:650;
font-size:1rem;color:var(--ink);position:relative;line-height:1.4}
.faq-i summary::-webkit-details-marker{display:none}
.faq-i summary::after{content:"";position:absolute;right:20px;top:50%;width:10px;height:10px;
border-right:2px solid var(--muted-2);border-bottom:2px solid var(--muted-2);
transform:translateY(-70%) rotate(45deg);transition:transform .15s ease}
.faq-i[open] summary::after{transform:translateY(-30%) rotate(-135deg)}
.faq-i summary:hover{background:var(--paper)}
.faq-a{padding:0 20px 17px;font-size:.95rem;color:var(--muted);line-height:1.62}
.faq-a>*:last-child{margin-bottom:0}
.faq-a ul{margin:.5em 0 .8em}

/* ---------- author box ---------- */
.abox{background:#fff;border:1px solid var(--line);border-radius:var(--r);padding:22px 24px;
display:grid;grid-template-columns:64px minmax(0,1fr);gap:18px;box-shadow:var(--sh);margin:0 0 1.4em}
.abox .av{width:64px;height:64px;box-shadow:0 0 0 2px var(--line)}
.abox h3{margin:0 0 .1em;font-size:1.1rem}
.abox .role{font-size:.86rem;color:var(--muted);margin:0 0 .55em;font-weight:600}
.abox p{font-size:.92rem;color:var(--muted);margin:0 0 .6em}
.abox .knows{display:flex;flex-wrap:wrap;gap:6px;margin-top:.5em}
.abox .knows span{font-size:.74rem;background:var(--paper);border:1px solid var(--line);border-radius:99px;
padding:3px 10px;color:var(--muted)}

/* ---------- toc ---------- */
.toc{background:#fff;border:1px solid var(--line);border-radius:var(--r);padding:18px 22px;margin:0 0 1.6em;box-shadow:var(--sh)}
.toc b{display:block;font-family:var(--h);font-size:.76rem;text-transform:uppercase;letter-spacing:.08em;
color:var(--muted-2);margin-bottom:10px}
.toc ol{columns:2;column-gap:34px;margin:0;padding-left:1.2em;font-size:.92rem}
.toc li{margin:0 0 .38em;break-inside:avoid}
.toc a{color:var(--text);text-decoration:none}
.toc a:hover{color:#15603C;text-decoration:underline}

/* ---------- misc ---------- */
.verdict{background:var(--ink);color:#fff;border-radius:var(--r);padding:24px 28px;margin:0 0 1.5em}
.verdict h3{color:#fff;margin:0 0 .45em}
.verdict p{color:rgba(255,255,255,.82);margin:0 0 .8em}
.verdict p:last-child{margin:0}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 1.3em}
.chip{font-size:.8rem;background:#fff;border:1px solid var(--line);border-radius:99px;padding:6px 14px;
color:var(--muted);text-decoration:none;font-weight:500}
a.chip:hover{border-color:var(--ink);color:var(--ink)}
.src{font-size:.85rem;color:var(--muted)}
.src ol{padding-left:1.3em}
.src li{margin-bottom:.4em}
.upd{font-family:var(--m);font-size:.76rem;color:var(--muted-2);margin:0 0 1.4em}

/* ---------- footer ---------- */
.ft{background:var(--ink);color:rgba(255,255,255,.62);padding:48px 0 30px;font-size:.9rem}
.ft-top{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,2.6fr);gap:40px;margin-bottom:32px}
.ft-brand p{margin:14px 0 14px;max-width:46ch;line-height:1.6;color:rgba(255,255,255,.56);font-size:.87rem}
.ft-badges{display:flex;flex-wrap:wrap;gap:8px}
.ft-badge{display:inline-flex;align-items:center;font-size:.74rem;color:rgba(255,255,255,.7);
background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:99px;padding:4px 11px}
.ft-badge .ic{color:var(--lime);width:.9em;height:.9em}
.ft-cols{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:26px}
.ft-col b{display:block;font-family:var(--h);font-size:.74rem;text-transform:uppercase;letter-spacing:.09em;
color:#fff;margin-bottom:11px}
.ft-col a{display:block;color:rgba(255,255,255,.6);text-decoration:none;padding:3px 0;font-size:.86rem}
.ft-col a:hover{color:var(--lime)}
.ft-rg{background:rgba(255,255,255,.045);border:1px solid rgba(255,255,255,.09);border-radius:var(--r);
padding:18px 22px;font-size:.81rem;line-height:1.62;color:rgba(255,255,255,.6)}
.ft-rg strong{color:rgba(255,255,255,.88)}
.ft-help{display:flex;flex-wrap:wrap;gap:18px;padding:18px 0 0;font-size:.83rem}
.ft-help a{color:var(--lime);text-decoration:none}
.ft-help a:hover{text-decoration:underline}
.ft-legal{display:flex;flex-wrap:wrap;justify-content:space-between;gap:12px;border-top:1px solid rgba(255,255,255,.1);
margin-top:20px;padding-top:18px;font-size:.79rem;color:rgba(255,255,255,.44)}
.ft-legal a{color:rgba(255,255,255,.6);text-decoration:none}
.ft-legal a:hover{color:var(--lime)}

/* ---------- responsive ---------- */
@media(max-width:1080px){
.lg-tag{display:none}
.nav-links>a,.nav-trig{padding:9px 9px;font-size:.88rem}
.hero-grid{grid-template-columns:1fr;gap:28px}
.hero-card{position:static;max-width:420px}
.tl-card{grid-template-columns:50px minmax(0,195px) minmax(0,1fr);padding-right:20px}
.tl-act{grid-column:2/-1;text-align:left}
.tl-act .btn{max-width:340px}
.ft-top{grid-template-columns:1fr;gap:28px}
}
@media(max-width:900px){
.nav-links,.nav-cta{display:none}
.menu{display:block}
.g4{grid-template-columns:repeat(2,minmax(0,1fr))}
.g3{grid-template-columns:repeat(2,minmax(0,1fr))}
.ft-cols{grid-template-columns:repeat(2,minmax(0,1fr))}
}
@media(max-width:700px){
body{font-size:16px}
.wrap{padding:0 16px}
.sec{padding:36px 0}

/* --- compressed hero: H1, author and updated date stay above the fold --- */
.hero{padding:12px 0 14px}
.hero::after{width:320px;height:320px;right:-120px;top:-120px}
.hero-grid{gap:0}
.hero-main{display:flex;flex-direction:column}
.crumbs{order:1;margin-bottom:10px;font-size:.76rem}
.eyebrow{order:2;margin:0 0 8px;font-size:.7rem;letter-spacing:.08em}
.hero h1{order:3;font-size:1.72rem;line-height:1.14;margin:0 0 10px}
.byline{order:4;padding:0;border-top:none;margin:0 0 10px;gap:10px}
.byline .av{width:38px;height:38px}
.by-txt{font-size:.82rem}
.by-sub{font-size:.74rem;margin-top:1px}
.hero-lede{order:5;font-size:.95rem;line-height:1.5;margin:0 0 4px;
display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden}
.hero-stats,.hero-ctas,.hero-pills,.hero-fine,.hero-card{display:none}

/* --- toplist: stacked card --- */
.sec-tl{padding:16px 0 32px}
.sec-tl>.wrap>h2{font-size:1.32rem;line-height:1.2;margin:0 0 10px}
.sec-tl>.wrap>.lede{font-size:.9rem;margin:0 0 13px;
display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.tl{gap:16px}
.tl-card{display:block;padding:13px 14px 15px;border-radius:16px;border-color:var(--line-2)}
.tl-card:first-child{border-color:var(--lime-2)}
.tl-rank{position:static;display:block;background:none;border:none;border-radius:0;
font-size:1.45rem;color:#5E7C10;text-align:left;line-height:1;margin:0 0 2px;padding:0}
.tl-card:first-child .tl-rank{background:none;color:#5E7C10}
.tl-badge{top:12px;right:12px;font-size:.6rem;padding:5px 10px}
.tl-brand{margin-top:6px}
.tl-logo{display:inline-block;padding:7px 12px;margin:0 auto 8px;border-radius:9px;min-width:172px}
.tl-logo img{max-height:52px}
.tl-name{font-size:1.12rem;margin:0 0 4px}
.tl-tag{display:block;font-size:.8rem;color:var(--muted);margin:0 0 10px;line-height:1.4;
padding:0 4px}
.tl-bar{height:8px;margin:0 0 7px}
.tl-scorerow{margin:0 0 11px;font-size:.88rem}
.tl-scorerow b{font-size:1.08rem}
.tl-offerbox{text-align:center;padding:11px 14px;margin:0 0 11px;border-radius:10px}
.tl-bonus{font-size:1rem}
.tl-usp,.tl-feats{display:none}
.tl-act .btn{height:48px;font-size:1rem;border-radius:10px}
.tl-read{margin-top:11px;font-size:.82rem;display:inline-block;border-bottom-color:var(--line-2)}
.tl-fine{margin-top:9px;font-size:.72rem}
.disc-grid{grid-template-columns:1fr;gap:18px}
.sec-disc{padding:28px 0 34px}

.pc,.g2,.g3,.g4{grid-template-columns:1fr}
.toc ol{columns:1}
.ft-cols{grid-template-columns:1fr}
}
@media(max-width:400px){
.hero h1{font-size:1.56rem}
.tl-tag{font-size:.77rem}
.sec-tl>.wrap>h2{font-size:1.24rem}
}
@media(prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important;scroll-behavior:auto!important}}
"""

# ---------------------------------------------------------------- title width
# Google truncates SERP titles on pixel width, not character count. These are
# exact Arial 20px advance widths (the standard desktop-SERP approximation),
# so a title can be checked at build time instead of eyeballed.
TITLE_PX_LIMIT = 580
ARIAL20 = {" ": 6.0, "!": 6.0, "\"": 7.0, "#": 11.0, "$": 11.0, "%": 18.0, "&": 13.0, "'": 4.0, "(": 7.0, ")": 7.0, "*": 8.0, "+": 12.0, ",": 6.0, "-": 7.0, ".": 6.0, "/": 6.0, "0": 11.0, "1": 11.0, "2": 11.0, "3": 11.0, "4": 11.0, "5": 11.0, "6": 11.0, "7": 11.0, "8": 11.0, "9": 11.0, ":": 6.0, ";": 6.0, "<": 12.0, "=": 12.0, ">": 12.0, "?": 11.0, "@": 20.0, "A": 13.0, "B": 13.0, "C": 14.0, "D": 14.0, "E": 13.0, "F": 12.0, "G": 16.0, "H": 14.0, "I": 6.0, "J": 10.0, "K": 13.0, "L": 11.0, "M": 17.0, "N": 14.0, "O": 16.0, "P": 13.0, "Q": 16.0, "R": 14.0, "S": 13.0, "T": 12.0, "U": 14.0, "V": 13.0, "W": 19.0, "X": 13.0, "Y": 13.0, "Z": 12.0, "[": 6.0, "\\": 6.0, "]": 6.0, "^": 9.0, "_": 11.0, "`": 7.0, "a": 11.0, "b": 11.0, "c": 10.0, "d": 11.0, "e": 11.0, "f": 6.0, "g": 11.0, "h": 11.0, "i": 4.0, "j": 4.0, "k": 10.0, "l": 4.0, "m": 17.0, "n": 11.0, "o": 11.0, "p": 11.0, "q": 11.0, "r": 7.0, "s": 10.0, "t": 6.0, "u": 11.0, "v": 10.0, "w": 14.0, "x": 10.0, "y": 10.0, "z": 10.0, "{": 7.0, "|": 5.0, "}": 7.0, "~": 12.0, "—": 20.0, "–": 11.0, "’": 4.0, "‘": 4.0, "“": 7.0, "”": 7.0, "…": 20.0, "é": 11.0, "ç": 10.0, "ā": 11.0, "ē": 11.0, "ī": 6.0, "ō": 11.0, "ū": 11.0, "À": 13.0}

def title_px(text):
    """Rendered width of a title in pixels at Arial 20px."""
    t = html.unescape(re.sub(r"<[^>]+>", "", text)).replace("{{month}}", MONTH_YEAR)
    return round(sum(ARIAL20.get(c, 11.12) for c in t), 1)

# ---------------------------------------------------------------- schema
def org_schema():
    return {
        "@type": "Organization",
        "@id": f"{DOMAIN}/#organization",
        "name": SITE,
        "url": DOMAIN + "/",
        "logo": {"@type": "ImageObject", "url": f"{DOMAIN}/favicon-512x512.png", "width": 512, "height": 512},
        "foundingDate": FOUNDED,
        "email": "editor@rnrv.co.nz",
        "areaServed": {"@type": "Country", "name": "New Zealand"},
        "knowsAbout": ["online casinos", "online pokies", "casino bonuses", "sports betting",
                       "New Zealand gambling law", "responsible gambling"],
        "publishingPrinciples": f"{DOMAIN}/how-we-rate-casinos/",
        "contactPoint": {"@type": "ContactPoint", "email": "editor@rnrv.co.nz",
                         "contactType": "editorial", "areaServed": "NZ", "availableLanguage": "en"},
    }

def person_schema(key):
    a = AUTHORS[key]
    return {
        "@type": "Person",
        "@id": f"{DOMAIN}/authors/#{a['slug']}",
        "name": a["name"],
        "url": f"{DOMAIN}/authors/#{a['slug']}",
        "jobTitle": a["jobTitle"],
        "description": strip_tags(a["bio"]),
        "knowsAbout": a["knows"],
        "image": DOMAIN + a["photo"].replace(".jpg", "@2x.jpg"),
        "worksFor": {"@id": f"{DOMAIN}/#organization"},
    }

def head_html(fm, extra_schema):
    for _k in ("title", "description", "h1", "lede"):
        if isinstance(fm.get(_k), str):
            fm[_k] = fm[_k].replace("{{month}}", MONTH_YEAR)
    url = DOMAIN + fm["url"]
    a = AUTHORS[fm.get("author", WRITER)]
    ck = AUTHORS[CHECKER]
    graph = [
        org_schema(),
        {"@type": "WebSite", "@id": f"{DOMAIN}/#website", "url": DOMAIN + "/", "name": SITE,
         "inLanguage": "en-NZ", "publisher": {"@id": f"{DOMAIN}/#organization"}},
        person_schema(fm.get("author", WRITER)),
        person_schema(CHECKER),
        {"@type": "WebPage", "@id": f"{url}#webpage", "url": url, "name": strip_tags(fm["title"]),
         "description": strip_tags(fm["description"]), "inLanguage": "en-NZ",
         "isPartOf": {"@id": f"{DOMAIN}/#website"},
         "datePublished": fm.get("published", UPDATED), "dateModified": fm.get("modified", UPDATED),
         "author": {"@id": f"{DOMAIN}/authors/#{a['slug']}"},
         "reviewedBy": {"@id": f"{DOMAIN}/authors/#{ck['slug']}"},
         "primaryImageOfPage": {"@type": "ImageObject", "url": f"{DOMAIN}/favicon-512x512.png"}},
    ]
    crumbs = [{"@type": "ListItem", "position": 1, "name": "Home", "item": DOMAIN + "/"}]
    for i, (n, h) in enumerate(fm.get("crumbs", []), 2):
        crumbs.append({"@type": "ListItem", "position": i, "name": strip_tags(n), "item": DOMAIN + h})
    if len(crumbs) > 1:
        graph.append({"@type": "BreadcrumbList", "@id": f"{url}#breadcrumb", "itemListElement": crumbs})
    graph.extend(extra_schema)

    ld = json.dumps({"@context": "https://schema.org", "@graph": graph},
                    ensure_ascii=False, separators=(",", ":"))
    og_img = f"{DOMAIN}/favicon-512x512.png"
    robots = fm.get("robots", "index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1")
    return f'''<!DOCTYPE html><html lang="en-NZ"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{fm["title"]}</title>
<link rel="canonical" href="{url}">
<meta name="description" content="{fm["description"]}">
<meta name="robots" content="{robots}">
<meta name="rating" content="adult"><meta name="age-restriction" content="18+">
<link rel="alternate" hreflang="en-nz" href="{url}">
<link rel="alternate" hreflang="x-default" href="{url}">
<meta property="og:type" content="{fm.get("ogtype","article")}">
<meta property="og:site_name" content="{SITE}">
<meta property="og:locale" content="en_NZ">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{fm["title"]}">
<meta property="og:description" content="{fm["description"]}">
<meta property="og:image" content="{og_img}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{fm["title"]}">
<meta name="twitter:description" content="{fm["description"]}">
<meta name="twitter:image" content="{og_img}">
<meta name="author" content="{strip_tags(a['name'])}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800&family=Inter:wght@400;500;600;650&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="icon" type="image/png" sizes="48x48" href="/favicon-48x48.png">
<link rel="icon" type="image/png" sizes="96x96" href="/favicon-96x96.png">
<link rel="icon" type="image/png" sizes="144x144" href="/favicon-144x144.png">
<link rel="icon" type="image/png" sizes="192x192" href="/favicon-192x192.png">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
<link rel="shortcut icon" href="/favicon.ico">
<meta name="theme-color" content="#12151A">
<style>{CSS}</style>
<script type="application/ld+json">{ld}</script>
</head><body>'''

# ---------------------------------------------------------------- page build
FM_RE = re.compile(r"<!--@(.*?)@-->", re.S)

def build_page(path):
    raw = open(path, encoding="utf-8").read()
    m = FM_RE.search(raw)
    if not m:
        raise SystemExit(f"no front matter in {path}")
    fm = json.loads(m.group(1))
    body = raw[m.end():].strip()

    extra = []
    blocks = {}

    # toplist block
    if fm.get("toplist"):
        t = fm["toplist"]
        slugs = t["ops"]
        blocks["TOPLIST"] = toplist(slugs, kind=t.get("kind", "casino"),
                                    intro=t.get("intro"), heading=t.get("heading"),
                                    hid=t.get("id", "toplist"))
        kind = t.get("kind", "casino")
        extra.append({
            "@type": "ItemList", "@id": f"{DOMAIN}{fm['url']}#itemlist",
            "name": strip_tags(t.get("heading") or fm["h1"]),
            "numberOfItems": len(slugs), "itemListOrder": "https://schema.org/ItemListOrderDescending",
            "itemListElement": [
                {"@type": "ListItem", "position": i,
                 "item": {"@type": "Product", "name": OPS[s]["name"],
                          "url": f"{DOMAIN}/casino-reviews/{OPS[s]['slug']}/",
                          "image": DOMAIN + op_logo(s, sports=(kind == "sports")),
                          "brand": {"@type": "Brand", "name": OPS[s]["name"]},
                          "review": {"@type": "Review",
                                     "author": {"@id": f"{DOMAIN}/authors/#{AUTHORS[fm.get('author','team')]['slug']}"},
                                     "reviewRating": {"@type": "Rating", "ratingValue": OPS[s]["rating"],
                                                      "bestRating": 5, "worstRating": 1},
                                     "reviewBody": strip_tags(OPS[s]["usp"])}}}
                for i, s in enumerate(slugs, 1)]})

    blocks["REVIEWGRID"] = review_grid()

    # FAQ block
    if fm.get("faq"):
        items = [(q, a) for q, a in fm["faq"]]
        blocks["FAQ"] = faq_block(items, heading=fm.get("faqHeading", "Frequently asked questions"))
        extra.append(faq_schema(items))

    # Review schema for operator review pages
    if fm.get("reviewOf"):
        s = fm["reviewOf"]
        op = OPS[s]
        extra.append({
            "@type": "Review", "@id": f"{DOMAIN}{fm['url']}#review",
            "itemReviewed": {"@type": "Product", "name": op["name"], "image": DOMAIN + op_logo(s),
                             "brand": {"@type": "Brand", "name": op["name"]},
                             "description": strip_tags(op["usp"])},
            "author": {"@id": f"{DOMAIN}/authors/#{AUTHORS[fm.get('author','team')]['slug']}"},
            "publisher": {"@id": f"{DOMAIN}/#organization"},
            "datePublished": fm.get("published", UPDATED), "dateModified": fm.get("modified", UPDATED),
            "reviewRating": {"@type": "Rating", "ratingValue": op["rating"], "bestRating": 5, "worstRating": 1},
            "reviewBody": strip_tags(op["usp"])})

    # HowTo schema
    if fm.get("howto"):
        h = fm["howto"]
        extra.append({"@type": "HowTo", "name": h["name"], "description": h.get("description", ""),
                      "step": [{"@type": "HowToStep", "position": i, "name": strip_tags(n),
                                "text": strip_tags(t)} for i, (n, t) in enumerate(h["steps"], 1)]})

    for k, v in fm.get("schema", {}).items():
        extra.append(v)

    lede = fm.get("lede", "")
    out = [head_html(fm, extra), nav_html(), hero_html(fm, lede), '<main id="main">']
    for k, v in blocks.items():
        body = body.replace("[[%s]]" % k, v)
    # any unreplaced markers
    body = re.sub(r"\[\[(TOPLIST|FAQ|REVIEWGRID)\]\]", "", body)
    out.append(body)
    out.append(disclosures_html(fm))
    out.append("</main>")
    out.append(foot_html())
    out.append("</body></html>")
    doc = resolve_tokens("".join(out))

    dest_dir = os.path.join(ROOT, fm["url"].strip("/"))
    os.makedirs(dest_dir, exist_ok=True)
    dest = os.path.join(dest_dir, "index.html")
    open(dest, "w", encoding="utf-8").write(doc)
    return fm, len(re.findall(r"\w+", strip_tags(body)))

# ---------------------------------------------------------------- sitemap
def sitemap(pages):
    rows = []
    for fm in sorted(pages, key=lambda f: (-float(f.get("priority", "0.7")), f["url"])):
        rows.append(
            f'<url><loc>{DOMAIN}{fm["url"]}</loc>'
            f'<lastmod>{fm.get("modified", UPDATED)}</lastmod>'
            f'<changefreq>{fm.get("changefreq", "monthly")}</changefreq>'
            f'<priority>{fm.get("priority", "0.7")}</priority></url>')
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           + "\n".join(rows) + "\n</urlset>\n")
    open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write(xml)

ROBOTS = f"""# robots.txt for {DOMAIN}
Sitemap: {DOMAIN}/sitemap.xml

User-agent: *
Allow: /

User-agent: AhrefsBot
Disallow: /

User-agent: SemrushBot
Disallow: /

User-agent: MJ12bot
Disallow: /

User-agent: DotBot
Disallow: /

User-agent: Rogerbot
Disallow: /

User-agent: serpstatbot
Disallow: /

User-agent: SistrixBot
Disallow: /
"""


# ---------------------------------------------------------------- redirect stubs
# Static hosting cannot emit a true 301, so these are meta-refresh + canonical,
# which Google treats as a permanent redirect signal. If the host supports real
# redirects (Cloudflare rules, Netlify _redirects, nginx), configure a 301 there
# and delete the stub.
REDIRECTS = {
    "/instant-withdrawals/": "/fast-payout-casinos/",
}

def write_redirects():
    for src, dest in REDIRECTS.items():
        d = os.path.join(ROOT, src.strip("/"))
        os.makedirs(d, exist_ok=True)
        html_doc = f"""<!DOCTYPE html><html lang="en-NZ"><head><meta charset="utf-8">
<title>Redirecting to {dest}</title>
<link rel="canonical" href="{DOMAIN}{dest}">
<meta http-equiv="refresh" content="0; url={dest}">
<meta name="robots" content="noindex,follow">
<style>body{{font:16px/1.6 -apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;
background:#12151A;color:#F7F7F4;margin:0;display:grid;place-items:center;min-height:100vh;padding:24px}}
a{{color:#C8FF3D}}</style></head><body>
<p>This page has moved to <a href="{dest}">{DOMAIN}{dest}</a>. Redirecting&hellip;</p>
<script>location.replace("{dest}");</script>
</body></html>"""
        open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(html_doc)
    return list(REDIRECTS)

def main():
    pages = []
    total = 0
    for f in sorted(os.listdir(SRC)):
        if not f.endswith(".html"):
            continue
        fm, words = build_page(os.path.join(SRC, f))
        pages.append(fm)
        total += words
        print(f"  {fm['url']:<42} {words:>6} words")
    write_redirects()
    sitemap(pages)
    open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8").write(ROBOTS)
    print(f"\n{len(pages)} pages, {total:,} words total")

    wide = [(title_px(fm["title"]), fm["url"], fm["title"]) for fm in pages
            if title_px(fm["title"]) > TITLE_PX_LIMIT]
    widest = max(title_px(fm["title"]) for fm in pages)
    if wide:
        print(f"\n!! {len(wide)} title(s) over {TITLE_PX_LIMIT}px and will be truncated in SERPs:")
        for w, u, t in sorted(wide, reverse=True):
            print(f"   {w:>6.1f}px  {u}  {t}")
    else:
        print(f"titles: all within {TITLE_PX_LIMIT}px (widest {widest}px)")
    if MISSING:
        print("MISSING affiliate links:", ", ".join(sorted(MISSING)))

if __name__ == "__main__":
    main()
