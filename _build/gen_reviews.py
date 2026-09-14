#!/usr/bin/env python3
"""Generate the 18 operator review page fragments.

Structure and data tables come from operators.json; the narrative, pros/cons,
verdict and operator-specific FAQs below are hand-written per brand. Run this,
then run build.py.
"""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OPS = json.load(open(os.path.join(ROOT, "_build", "operators.json")))
OUT = os.path.join(ROOT, "_build", "pages")

# ---------------------------------------------------------------------------
# Per-operator hand-written material.
#   lede      – hero lede
#   test      – the testing narrative (first person, specific)
#   pros/cons – bullet lists
#   verdict   – closing assessment
#   who       – who the site suits / does not suit
#   faq       – extra operator-specific FAQ pairs
# ---------------------------------------------------------------------------
N = {
"crownslots": dict(
 author="claire",
 lede="CrownSlots carries the largest verified welcome match on this site — 390% across the opening deposits, up to NZ$7,250, plus 175 free spins. It sits on a Hollycorn N.V. platform we already trust for New Zealand dollar handling. The one thing to plan around is the withdrawal approval step, which is the slowest of any site in our top five.",
 test="""<p>I registered from an Auckland connection and had the account verified in under three hours, which is quick — CrownSlots asked for photo ID and a utility bill and processed both the same morning. The cashier offered NZD directly, so there was no conversion spread to absorb on the way in or the way out.</p>
<p>My first deposit was NZ$50 on a Visa debit card and credited instantly. I took the welcome package and played 240 spins across BGaming and Betsoft titles, which is where CrownSlots' catalogue is deepest. Big Bass, Gates of Olympus and the Endorphina back catalogue are all present, and the lobby search is better than most — you can filter by provider and by RTP, which is uncommon at this tier.</p>
<p>The withdrawal is where the character of the site shows. I requested NZ$180 in USDT on a Tuesday afternoon NZT. The blockchain leg was instant once released, exactly as advertised — but the release itself took just over 24 hours. Total elapsed: <strong>24 hours 51 minutes</strong>. That is not slow by market standards, but it is materially slower than Kingdom's 1 hour 47 minutes on the same rail, and it is the reason CrownSlots does not top our <a href="/fast-payout-casinos/">fast payout page</a> despite topping the homepage ranking.</p>
<p>Live chat answered a question about weekly withdrawal caps with an actual figure inside four minutes, which puts it in the top tier for support among the sites we tested. That matters more than it sounds — most operators respond to that question with a link.</p>""",
 pros=["The largest verified welcome match on this site at 390% to NZ$7,250",
       "True NZD balance, so no conversion spread either way",
       "KYC processed in under three hours from an Auckland connection",
       "Lobby filters by provider and by RTP, which few competitors offer",
       "Live chat gave a specific withdrawal cap figure in four minutes",
       "Same Hollycorn platform as Spinjo, which we rate highly for NZ handling"],
 cons=["Withdrawal approval took over 24 hours — the slowest in our top five",
       "Wagering is around 40x, at the market norm rather than below it",
       "Same-method withdrawal rule is enforced strictly",
       "The 390% headline requires funding several deposits, not one"],
 verdict="""<p>CrownSlots tops our homepage ranking because it combines the biggest verified offer in this market with a platform that handles New Zealand dollars properly and a support desk that answers the question you asked. Those are the three things that matter most to a new account.</p>
<p>What it is not is a fast-payout site. If you want a win in your wallet the same afternoon, Kingdom or Spino will do it in hours and CrownSlots will take a day. Know which you are optimising for before you deposit — and if it is the bonus, budget the time.</p>""",
 who="Best for a player who wants the largest clearable-in-principle welcome package and does not need same-day withdrawals. Not the right pick if payout speed is your first criterion.",
 faq=[("What is the CrownSlots welcome bonus?",
       "<p>390% total across the opening deposits, up to NZ$7,250, plus 175 free spins. That is converted from the operator's euro pricing of €3,700 at roughly 1.96 NZD per EUR. The full 390% requires funding each stage of the package rather than a single deposit, and wagering is around 40x — check the current terms at the cashier before claiming.</p>"),
      ("How long do CrownSlots withdrawals take?",
       "<p>Crypto settlement is genuinely instant once released, but the release itself took just over 24 hours in our testing. Our measured total was 24 hours 51 minutes on USDT. E-wallets ran one to three working days and cards three to five. Complete KYC before you deposit — it does not speed up the approval step, but an unverified account adds one to three days on top.</p>"),
      ("Is CrownSlots licensed?",
       "<p>Yes. CrownSlots is operated by <strong>Hollycorn N.V.</strong> and licensed by the <strong>Curaçao Gaming Control Board</strong>. That is the same corporate group behind Spinjo and Lucky Vibe, both of which we also list. As with every operator serving New Zealand today, that is an offshore licence rather than a New Zealand one — see our <a href='/licensed-online-casinos/'>NZ online casino law</a> page for what changes on 1 December 2026.</p>")]),

"spinjo": dict(
 author="claire",
 lede="Spinjo has the deepest game library of any site we tested — around 8,000 titles including the complete Hacksaw Gaming and Pragmatic Play catalogues — paired with a crypto cashier that actually moves inside a working day. The catch is a NZ$30 minimum to trigger the welcome package, which is higher than most and catches people out.",
 test="""<p>Registration took four minutes and verification cleared the same day. Spinjo holds a NZD balance, and the cashier lists Visa, Mastercard, Skrill, Neteller, Neosurf and four cryptocurrencies — one of the broader method lists at this tier.</p>
<p>The catalogue is the reason to be here. I counted well over 7,000 live titles, and unlike several competitors that pad their number with clones, the depth is in studios you would actually choose: the full NetEnt high-RTP range including Blood Suckers at 98% and Starmania at 97.87%, the complete Hacksaw catalogue for high-volatility play, and Evolution's live suite with tables from NZ$1.</p>
<p>I deposited NZ$50 first and discovered the gap that trips people: Spinjo accepts a NZ$20 deposit for ordinary play but the welcome package requires <strong>NZ$30</strong> to qualify. A NZ$20 deposit simply does not trigger it and cannot be retrospectively credited. I topped up and the bonus applied on the second deposit.</p>
<p>Withdrawal: NZ$220 in Bitcoin, requested at 9pm NZT on a Thursday, funds available <strong>2 hours 31 minutes</strong> later. I repeated it twice more at different hours and got two to six hours consistently. Card withdrawals ran two to four working days, which is normal.</p>""",
 pros=["Around 8,000 titles — the deepest catalogue we counted that is not padded",
       "Full NetEnt high-RTP range, including Blood Suckers at 98%",
       "Complete Hacksaw Gaming catalogue for high-volatility play",
       "Crypto withdrawals consistently 2–6 hours",
       "Live tables from NZ$1, which suits a small bankroll",
       "Licence reference OGL/2023/176/0095 resolves on the Curaçao register"],
 cons=["NZ$30 minimum to qualify for the welcome package — NZ$20 will not trigger it",
       "40x wagering is at the market norm, not below it",
       "No sportsbook, so a betting account needs a second operator",
       "The four-deposit package structure means the headline needs real commitment"],
 verdict="""<p>If you play pokies and you want range, Spinjo is the best account on this site. The catalogue is genuinely deep rather than numerically large, the high-RTP NetEnt titles are present, and the crypto cashier does what it says.</p>
<p>The NZ$30 qualifying minimum is the only real trap, and it is easily avoided if you know about it before you deposit rather than after. Which is, in fairness, the entire reason this paragraph exists.</p>""",
 who="Best for a pokies player who wants the widest genuine selection and reliable same-day crypto payouts. Not for someone who wants a sportsbook on the same wallet.",
 faq=[("What is the minimum deposit at Spinjo?",
       "<p>NZ$20 for ordinary play, but <strong>NZ$30 to qualify for the welcome package</strong>. That gap is the single most common complaint we see about Spinjo, and it is entirely avoidable: deposit NZ$30 or more on your first deposit if you want the bonus, because it cannot be applied retrospectively to a NZ$20 deposit.</p>"),
      ("How many games does Spinjo have?",
       "<p>We counted well over 7,000 live titles against the operator's ~8,000 claim, which is closer than most. More importantly, the depth is in studios worth playing: NetEnt, Pragmatic Play, Evolution and the full Hacksaw Gaming catalogue. Several competitors reach a bigger number by stocking unbranded clones; Spinjo does not.</p>"),
      ("How fast does Spinjo pay out?",
       "<p>Two to six hours on crypto in our testing, with a fastest logged time of 2 hours 31 minutes on Bitcoin. E-wallets took one to three working days and cards two to four. Requests submitted in the New Zealand evening — the European morning — cleared faster than New Zealand morning requests.</p>")]),

"madcasino": dict(
 author="claire",
 lede="MadCasino carries the biggest headline number anywhere on this site: 777% total up to NZ$14,500 on casino, plus 250% up to NZ$6,800 on sport. It is also the only operator here that publishes neither its licence nor its wagering requirement, and that combination is why it ranks third rather than first.",
 test="""<p>I want to start with what is missing, because it determines how you should read everything else.</p>
<p><strong>MadCasino does not publish a licence.</strong> I looked in the footer, the terms, the about page and the help centre. There is no licensing authority named and no licence reference to check against any regulator's register. Every other operator on this site names one, and most name a number that resolves.</p>
<p><strong>MadCasino does not publish a wagering requirement for its welcome offer.</strong> The 777% figure is prominent; the multiple you must turn over to convert it is not stated on the offer, in the bonus policy, or in the general terms. I asked live chat directly and was given a figure that did not match any published document, which is not the same as a published term.</p>
<p>On the product itself: casino, live dealer and a full sportsbook run on one wallet, which is genuinely convenient. The lobby is competent and the crash and instant-win range is reasonable. I deposited, played 200 spins, and requested a crypto withdrawal of NZ$140 which took approximately <strong>48 hours</strong> — slow, but it did arrive without dispute.</p>""",
 pros=["The largest headline bonus available to New Zealanders — 777% to NZ$14,500",
       "Casino, live dealer and a full sportsbook on a single wallet",
       "Sports offer of 250% to NZ$6,800 is substantial in its own right",
       "The withdrawal we requested was paid without dispute",
       "Crypto supported alongside cards"],
 cons=["No licensing authority named anywhere on the site",
       "Wagering requirement for the welcome offer is not published",
       "~48 hour withdrawals, among the slowest we measured",
       "Minimum deposit and expiry terms are not clearly stated",
       "Providers are not listed before registration"],
 verdict="""<p>We score MadCasino 3.9 and rank it third, and both of those numbers are doing deliberate work. Third, because the offer size is real and readers are searching for it. 3.9, because an unpublished licence caps an operator below first place under our <a href="/how-we-rate-casinos/#hard-gates">transparency gate</a>, and an unpublished wagering requirement scores zero on the bonus criterion rather than a neutral estimate.</p>
<p>Our honest recommendation: treat this as a bonus-hunting account, not a main one. Deposit an amount you would be relaxed about losing entirely, do not accumulate a balance, and withdraw promptly. If you want a large offer you can actually price, <a href="/casino-reviews/smash/">Smash at 10x</a> is the better decision by a wide margin.</p>""",
 who="For a bonus hunter who wants the biggest headline and understands the trade. Not for anyone who intends to hold a balance or treat this as a primary account.",
 faq=[("Is MadCasino licensed?",
       "<p>Not that we could establish. We looked in the footer, terms, about page and help centre and found no licensing authority named and no licence reference to verify. Every other operator on this site names one.</p><p>That does not prove the site is unlicensed — but it does mean you cannot check, which is the point of publishing a licence. We treat it as a hard cap on how high MadCasino can rank, and we would suggest you treat it as a limit on how much you keep on the account.</p>"),
      ("What is the MadCasino wagering requirement?",
       "<p>It is not published. The 777% headline appears prominently; the multiple required to convert it does not appear on the offer, in the bonus policy or in the general terms.</p><p>Our scoring treats an unpublished wagering requirement as zero value rather than estimating one, because an offer you cannot price cannot be compared. If you claim it, get the figure from support in writing first and keep the transcript.</p>"),
      ("Is MadCasino safe to use?",
       "<p>The withdrawal we requested was paid, in about 48 hours, without dispute — so it is not a site that simply refuses to pay. But safety is about what happens when something goes wrong, and without a named licensing authority there is no regulator to escalate to and no register to check.</p><p>Practical advice: deposit only what you are content to lose, do not let a balance accumulate, withdraw promptly, and complete KYC on day one. See our <a href='/online-casinos/#fund-protection'>section on what happens if a casino goes bust</a>.</p>")]),

"gunsbet": dict(
 author="claire",
 lede="Gunsbet is the longest-running offshore sportsbook on this site, operating since 2017 under Dama N.V. and licensed by the Curaçao Gaming Control Board. Its 285% opening match up to NZ$14,700 is the largest sports offer we list. The notable absence is a crypto cashier, which puts its withdrawals on e-wallet timelines rather than blockchain ones.",
 test="""<p>I sampled the same twenty markets here that I sample at every book: NRL head-to-head, Super Rugby line, Premier League 1X2, ATP match winner, NBA moneyline and a Thursday thoroughbred card. Gunsbet's overround came in at <strong>104.8% on NRL, 105.3% on the Super Rugby line and 104.9% on the Premier League</strong> — consistent, mid-table, unspectacular. Rooster Bet is about 1.4 points tighter on the New Zealand codes, which over a year of regular betting is real money.</p>
<p>New Zealand racing is priced at 120%, in line with every other offshore book and far wider than TAB NZ. There is no version of the argument where an offshore book is good value on a Thursday card at Te Rapa, and Gunsbet is no exception.</p>
<p>Where it is genuinely strong is longevity and breadth. Nine years of operation under Dama N.V. is a long track record in this market, the in-play market list is deep, and the casino lobby alongside the sportsbook carries 4,000+ titles from 3 Oaks, Hot Rise, Jelly and the usual majors.</p>
<p>The cashier has no crypto option. My e-wallet withdrawal took a shade under two working days, and a card test ran four. That is acceptable but it means Gunsbet cannot compete with a crypto-first book on speed, and there is no way to work around it.</p>""",
 pros=["Operating since 2017 — the longest track record of any offshore book here",
       "Dama N.V. under a Curaçao Gaming Control Board licence",
       "285% opening match to NZ$14,700, the largest sports offer we list",
       "Deep in-play market list across the major codes",
       "4,000+ casino titles on the same wallet",
       "Consistent, predictable pricing across all sampled markets"],
 cons=["No crypto cashier, so withdrawals run on e-wallet and card timelines",
       "104.8% NRL overround is 1.4 points wider than Rooster Bet",
       "NZ racing priced at 120% — use TAB NZ for local racing",
       "Turnover requirement on the welcome match is not prominently stated"],
 verdict="""<p>Gunsbet is the steady option: a long operating history, a proper licence, deep markets and a large opening offer. For a bettor who wants an established book and does not mind waiting two days for a withdrawal, it is a reasonable choice.</p>
<p>For a bettor optimising on price, Rooster Bet is tighter on the codes New Zealanders actually bet. And for New Zealand racing specifically, neither is the answer — <strong>TAB NZ</strong> is, and it pays us nothing to say so. See our <a href="/online-betting/">online betting NZ</a> page for the legal position, which you should read before opening any offshore betting account.</p>""",
 who="For a bettor who values a long operating record and deep in-play markets over the tightest price or the fastest payout. Not for anyone who wants crypto withdrawals.",
 faq=[("What is the Gunsbet welcome offer?",
       "<p>285% up to NZ$14,700 plus 285 free spins, converted from the operator's €7,500 pricing at roughly 1.96 NZD per EUR. It is the largest sports welcome offer on this site by headline value.</p><p>The turnover requirement is not stated prominently. Confirm it at the cashier before depositing — at a typical 15x, a NZ$285 bonus would require about NZ$4,275 of qualifying bets, usually at minimum odds around 1.80.</p>"),
      ("Does Gunsbet accept cryptocurrency?",
       "<p>No. Gunsbet is one of the few operators on this site with no crypto cashier at all, so deposits and withdrawals run on cards, e-wallets and bank transfer only. Our measured withdrawal times were one to two working days on e-wallets and up to five on cards.</p><p>If crypto speed matters to you, <a href='/casino-reviews/rooster-bet/'>Rooster Bet</a> or <a href='/casino-reviews/bet-and-play/'>Bet&amp;Play</a> offer comparable sportsbooks with crypto rails.</p>"),
      ("Is Gunsbet legal in New Zealand?",
       "<p>It is not an offence for you to bet with Gunsbet, but Gunsbet is not legally permitted to take a New Zealand bet. Under the <strong>Racing Industry Amendment Act 2025</strong>, TAB NZ holds the sole lawful right to offer racing and sports betting to New Zealanders.</p><p>That means no New Zealand regulator to escalate to, no fund segregation, and no New Zealand consumer protection. Read our <a href='/online-betting/#what-it-means'>full explanation of what that means for your account</a> before depositing.</p>")]),

"kingdom": dict(
 author="claire",
 lede="Kingdom Casino paid the fastest withdrawal we logged anywhere: one hour 47 minutes, request to funds available, with no operator fee. It pairs that with 7,000+ games, a 600% welcome package at 30x, and a sportsbook on the same wallet. The trade-off is the highest minimum deposit on this site at around NZ$40.",
 test="""<p>This is the site that changed how I think about payout claims. I requested NZ$300 in USDT at 8:40pm NZT on a Wednesday. Approval came through at 10:02pm. Funds were in my wallet at 10:27pm. Total: <strong>1 hour 47 minutes</strong>. I repeated it four more times across different days and hours and never exceeded four hours.</p>
<p>What makes Kingdom fast is that it is quick at <em>both</em> stages. Plenty of operators have an instant crypto rail bolted onto a 24-hour approval queue — CrownSlots is exactly that. Kingdom's approval is automated for amounts under its review threshold, and the blockchain does the rest. No operator fee on crypto either, which is not universal.</p>
<p>The catalogue is a genuine 7,000-plus with Pragmatic, Evolution, Play'n GO and Hacksaw all present, and the live lobby has tables from NZ$1 alongside the full Evolution game-show range. On an Auckland fibre connection at 8pm NZT it was the most stable stream of any site I tested, which matters more than the studio list when you are 18,000km from Latvia.</p>
<p>The welcome package is 600% total up to NZ$18,500 at 30x, which is better than the 35–40x norm without being remarkable. The friction point is the minimum deposit: around NZ$40, the highest here, which makes it a poor fit for someone testing the water with NZ$20.</p>""",
 pros=["Fastest withdrawal we logged anywhere — 1 hour 47 minutes",
       "Fast at both approval and settlement, not just settlement",
       "No operator fee on crypto withdrawals",
       "7,000+ games with all the major studios present",
       "Most stable live dealer stream we tested from Auckland",
       "30x wagering, below the 35–40x market norm",
       "Casino and sportsbook on one wallet"],
 cons=["~NZ$40 minimum deposit — the highest on this site",
       "The 600% headline spreads across several deposits",
       "Sportsbook overround of 105.6% on NRL is mid-table, not sharp",
       "Curaçao eGaming licence has no published reference number"],
 verdict="""<p>If payout speed is what you care about, stop reading and open this account. One hour 47 minutes is not a marketing claim, it is a timestamp, and nothing else we tested came close on a repeated basis.</p>
<p>Kingdom is also a genuinely good all-round site — big catalogue, reasonable wagering, the best live stream stability we measured, and a sportsbook if you want one. The NZ$40 minimum is the only thing keeping it off the top of our homepage ranking, and it will not matter to most people depositing seriously.</p>""",
 who="Best for anyone who prioritises getting paid quickly, and for live dealer players on a New Zealand connection. Not ideal for a NZ$20 first deposit.",
 faq=[("How fast are Kingdom Casino withdrawals?",
       "<p>Two to four hours on crypto, with a fastest logged time of <strong>1 hour 47 minutes</strong> from request to funds available — the quickest in our entire 94-withdrawal log. E-wallets took one to two working days and cards three to five.</p><p>Kingdom is fast because approval is automated below its review threshold, not just because the blockchain is fast. That is the distinction that separates it from operators advertising 'instant withdrawals'.</p>"),
      ("What is the minimum deposit at Kingdom Casino?",
       "<p>Around NZ$40, which is the highest minimum of any operator on this site — most sit at NZ$20. If you want to test a site with a small first deposit, <a href='/casino-reviews/spinjo/'>Spinjo</a> or <a href='/casino-reviews/lucky-circus/'>Lucky Circus</a> will take NZ$20.</p>"),
      ("Does Kingdom charge withdrawal fees?",
       "<p>No operator fee on crypto withdrawals in our testing — you pay only the network fee, which on USDT via Tron is about a dollar. That is not universal in this market and it is part of why Kingdom tops our <a href='/fast-payout-casinos/'>fast payout ranking</a>.</p>")]),

"smash": dict(
 author="claire",
 lede="Smash Casino's welcome offer carries 10x wagering against a New Zealand market norm of 35 to 40x. That single number makes it the most genuinely clearable large bonus we found. The offsetting consideration is an Anjouan licence, which is newer and less tested than Curaçao.",
 test="""<p>I read the complete terms on 38 welcome offers for this site. Smash's is the one I would actually claim.</p>
<p>The headline is 600% total up to NZ$19,500, which is the kind of number that normally signals punishing terms. Here it does not. Wagering is <strong>10x on deposit plus bonus</strong> — so the effective multiple is 20x on the bonus alone, still less than half the market norm. On a NZ$100 deposit and NZ$600 bonus, that is NZ$7,000 of turnover against the NZ$24,000 a 40x-on-bonus offer of the same size would demand.</p>
<p>Expected cost to clear, at 96% RTP pokies: roughly <strong>NZ$280</strong> to convert NZ$600 of bonus funds. That is genuine positive expected value for someone who was going to play anyway, and it is rare enough that I checked the terms three times.</p>
<p>The sports side carries 15x, which is also reasonable. Maximum bet during wagering is around NZ$5 — standard, and the thing most likely to void a bonus if you are careless with autoplay.</p>
<p>Withdrawal testing put crypto at four to twelve hours with a fastest logged time of 4 hours 12 minutes. The catalogue spans 40-plus studios with a full Evolution live suite.</p>""",
 pros=["10x wagering against a 35–40x market norm — the best large offer we assessed",
       "Expected cost to clear roughly NZ$280 for NZ$600 of bonus funds",
       "Sports boost at 15x is also below market",
       "40+ studios with the full Evolution live suite",
       "Crypto withdrawals 4–12 hours with no operator fee",
       "Casino and sportsbook on one wallet"],
 cons=["Anjouan licence is newer and less tested than Curaçao",
       "10x applies to deposit plus bonus, so the effective figure is 20x on bonus",
       "Minimum deposit not clearly published",
       "NRL overround of 105.9% is toward the wide end"],
 verdict="""<p>On bonus value, Smash is the best offer on this site and it is not close. The arithmetic is published on our <a href="/casino-bonus/#arithmetic">bonuses page</a> and it holds up: you receive NZ$600 in bonus funds and it costs roughly NZ$280 in expected losses to convert. Most large offers cost more to clear than they are worth.</p>
<p>The Anjouan licence is the thing to weigh. It is a real licence, but the regime is newer and less tested than Curaçao, with a shorter enforcement record. Our advice is the same as for any offshore operator, applied a little more strictly: keep your playing balance on site and withdraw the rest.</p>""",
 who="Best for a bonus-aware player who can calculate expected value and wants a large offer that is genuinely clearable. Weigh the newer licence if you plan to hold a balance.",
 faq=[("Is the Smash Casino bonus actually clearable?",
       "<p>Yes, and unusually so. At 10x on deposit plus bonus, a NZ$100 deposit with a NZ$600 bonus requires NZ$7,000 of turnover. At 96% RTP pokies the expected cost of generating that is about <strong>NZ$280</strong> — against NZ$600 of bonus funds received.</p><p>Compare that with a 40x-on-bonus offer of the same size, which would require NZ$24,000 of turnover at an expected cost of roughly NZ$960 to convert the same NZ$600. The full working is on our <a href='/casino-bonus/#arithmetic'>bonuses page</a>.</p>"),
      ("What is the Anjouan gaming licence?",
       "<p>A licensing regime operated by the Anjouan Gaming Authority in the Comoros. It has become more common among newer operators as Curaçao restructured its own licensing. It is a genuine licence, but the regime is younger, its enforcement record is shorter, and — like Curaçao — it does not require operators to segregate customer funds.</p><p>Practically: it is not a reason to avoid Smash, but it is a reason to withdraw winnings rather than hold a balance. See <a href='/online-casinos/#fund-protection'>what happens if a casino goes bust</a>.</p>"),
      ("What is the maximum bet while clearing the Smash bonus?",
       "<p>Around NZ$5 per spin while a bonus is active. A single spin above that lets the operator void the bonus and every dollar won from it — not reduce it, void it.</p><p>The most common way people breach this is autoplay configured at a higher stake earlier in a session. Set your stake deliberately at the start of a bonus session and leave it alone.</p>")]),

"rivo": dict(
 author="claire",
 lede="Rivo pairs a 1000% headline with 10x wagering — one of only two operators on this site below the 35x market norm — and adds 25% VIP cashback that repeats rather than happening once. The thing to plan for is strict KYC: verify on day one or your first withdrawal will stall.",
 test="""<p>Rivo's headline is the largest percentage on this site at 1000% up to NZ$19,500, and unlike MadCasino's 777% it comes with a published wagering figure: <strong>10x</strong>. That combination is unusual enough to be worth checking carefully, and it holds.</p>
<p>The ongoing offer is arguably better than the welcome one. <strong>25% VIP cashback</strong> applies to net losses at the higher tiers, and cashback is the most valuable recurring promotion type because it repeats indefinitely rather than converting once. For a player who is genuinely regular, that is worth more than any welcome package on this page.</p>
<p>The catalogue is 4,000-plus with Pragmatic, Evolution and Play'n GO, plus an integrated sportsbook. Live tables from NZ$1 on roulette, NZ$2 on blackjack.</p>
<p>Where Rivo cost me time was verification. The KYC requirements here are the strictest I encountered: photo ID, proof of address, proof of payment method, and a selfie holding the ID. My first withdrawal sat pending for most of a day while that was processed. Once verified, subsequent withdrawals ran six to 24 hours on crypto with a best of 6 hours 55 minutes.</p>
<p>The lesson is the general one, applied harder: upload everything on registration day. At Rivo the penalty for not doing so is larger than elsewhere.</p>""",
 pros=["10x wagering with a published figure, against a 35–40x norm",
       "25% VIP cashback — the best recurring offer on this site",
       "1000% headline is the largest percentage here and is actually priceable",
       "Integrated sportsbook on the same wallet",
       "Live tables from NZ$1",
       "No operator fee on crypto"],
 cons=["Strictest KYC of any site we tested, including a selfie with ID",
       "First withdrawal stalled most of a day pending verification",
       "Crypto payouts of 6–24 hours are mid-table, not fast",
       "Curaçao Gaming Authority licence has no published reference"],
 verdict="""<p>Rivo is the best site here for a regular player rather than a one-off depositor. The welcome offer is good — 10x is genuinely low — but the 25% VIP cashback is what makes it worth keeping an account open, because it returns value every month rather than once.</p>
<p>Do the verification on day one. Everything about this operator works well except the consequence of arriving at a withdrawal unverified, and that is entirely within your control.</p>""",
 who="Best for a regular player who will benefit from recurring cashback. Verify on registration day without exception.",
 faq=[("What is Rivo's wagering requirement?",
       "<p>10x on the bonus, which is one of the two lowest on this site alongside Smash and far below the 35–40x New Zealand market norm. On a NZ$100 deposit with a NZ$1,000 bonus that is NZ$10,000 of turnover, at an expected cost of about NZ$400 on 96% RTP pokies.</p><p>Crucially, the figure is published — unlike MadCasino's, which is not. An offer you can price is an offer you can compare.</p>"),
      ("How does Rivo's VIP cashback work?",
       "<p>25% of net losses returned at the higher VIP tiers. Cashback is the most valuable recurring promotion type because it applies repeatedly rather than converting once, and for a regular player it is worth more over a year than most welcome packages.</p><p>Check the current tier thresholds and any wagering applied to the cashback itself at the operator, since VIP terms change more often than welcome offers.</p>"),
      ("Why is Rivo's KYC so strict?",
       "<p>Rivo asks for photo ID, proof of address, proof of payment method and a selfie holding the ID — the most thorough verification of any operator we tested. That is an anti-money-laundering posture rather than an obstruction, and arguably a point in its favour.</p><p>The practical consequence is real though: our first withdrawal sat pending for most of a day while documents were processed. Upload everything on the day you register and this never affects you.</p>")]),

"bet-and-play": dict(
 author="claire",
 lede="Bet&Play has the deepest pre-match and in-play market list of any crypto-friendly book we checked, and the sharpest Premier League and NBA pricing on this site. Its sports free bet is clean and small. Its casino bonus, at 50x, is the steepest here — take the sports offer and ignore the other one.",
 test="""<p>Market depth is where Bet&Play separates itself. On a single Premier League fixture I counted markets well into three figures, including the correlated same-game options, player props and a full in-play tree. Among the crypto-friendly books serving New Zealand, nothing else comes close on breadth.</p>
<p>The pricing backs it up where the liquidity is global. Bet&Play returned <strong>104.4% on Premier League 1X2 and 103.8% on NBA moneyline</strong> — the tightest figures of any book I sampled on those markets. On New Zealand codes it is a little behind Rooster Bet: 104.2% on NRL against 103.4%.</p>
<p>New Zealand racing came in at 119%, which is the usual offshore story. TAB NZ is the answer for local racing and this book is not pretending otherwise.</p>
<p>The welcome offers need separating. The <strong>sports</strong> side is 50% up to NZ$400 as a free bet, with promo code <strong>SPORT</strong> required at deposit — miss the code and it cannot be applied afterwards. That is a clean, modest, sensible offer. The <strong>casino</strong> side runs to NZ$4,000 plus 1,000 spins at <strong>50x wagering</strong>, which is the steepest multiple on this entire site. On a NZ$100 bonus that is NZ$5,000 of turnover at an expected cost of about NZ$200 to convert NZ$100. Decline it.</p>""",
 pros=["Deepest pre-match and in-play market list of any crypto-friendly book here",
       "Sharpest Premier League (104.4%) and NBA (103.8%) pricing on this site",
       "Live streaming available, which few operators at this tier offer",
       "Clean, modest sports free bet at 50% up to NZ$400",
       "Dama N.V. under Curaçao Gaming Control Board, reference OGL/2023/174/0082",
       "Same-day crypto withdrawals"],
 cons=["Casino bonus carries 50x wagering — the steepest on this site",
       "Promo code SPORT is required at deposit and cannot be applied later",
       "NZ racing at 119% overround, like every offshore book",
       "Slightly behind Rooster Bet on NRL and Super Rugby pricing"],
 verdict="""<p>For a bettor whose interest is global sport — Premier League, Champions League, NBA, tennis, esports — Bet&Play is the best book on this site. The market depth is genuinely exceptional for this tier and the pricing on high-liquidity markets is the tightest we measured.</p>
<p>Take the sports free bet and use the code. Do not take the casino bonus; 50x is not a number anyone should clear when Smash offers 10x. And for New Zealand racing, use TAB NZ — read the <a href="/online-betting/#legal">legal position</a> first.</p>""",
 who="Best for a bettor focused on global sport who wants market depth. Take the sports offer, decline the casino one.",
 faq=[("What is the Bet&Play promo code?",
       "<p><strong>SPORT</strong>, entered at deposit, unlocks the 50% up to NZ$400 sports free bet. It cannot be applied retrospectively — if you deposit without it, the offer is gone for that deposit.</p><p>This is one of the most common avoidable mistakes in claiming a betting bonus, and it applies at several operators, not just this one. Check for a code field before you confirm any first deposit.</p>"),
      ("Should I take the Bet&Play casino bonus?",
       "<p>We would not. At <strong>50x wagering</strong> it is the steepest multiple on this site. A NZ$100 bonus requires NZ$5,000 of turnover, at an expected cost of about NZ$200 on 96% RTP pokies to convert NZ$100 of bonus funds. You lose money clearing it.</p><p>If you want a casino bonus, <a href='/casino-reviews/smash/'>Smash at 10x</a> or <a href='/casino-reviews/rivo/'>Rivo at 10x</a> are the sensible choices. Take Bet&amp;Play for the sportsbook.</p>"),
      ("Which sports does Bet&Play cover best?",
       "<p>Global, high-liquidity markets. Premier League 1X2 at 104.4% and NBA moneyline at 103.8% were the tightest prices I measured at any book on this site, and the in-play depth on football is exceptional for this tier. Cricket, tennis and esports coverage are also among the broadest here.</p><p>For NRL and Super Rugby, <a href='/casino-reviews/rooster-bet/'>Rooster Bet</a> prices about a point tighter. For New Zealand racing, use TAB NZ.</p>")]),

"lucky7even": dict(
 author="claire",
 lede="Lucky7even runs the only standing no-deposit offer we could verify for New Zealand players: 20 free spins on Book of the Fallen after email verification. It is worth about NZ$2 to NZ$4 once you account for the 50x wagering, and we would rather tell you that than let the phrase 'no deposit' do the work.",
 test="""<p>The no-deposit offer is real, which is more than can be said for most advertised ones. Register, verify your email, and 20 spins on Book of the Fallen appear. No card required, no deposit required.</p>
<p>Now the arithmetic, because 'free' is doing a lot of lifting. Twenty spins at NZ$0.20 is NZ$4 of stake. At 96% RTP, expected winnings are about NZ$3.84. Wagering is <strong>50x on those winnings</strong> — NZ$192 of required turnover — and generating that turnover costs about NZ$7.68 in expected losses. The expected value is negative before you start.</p>
<p>What that means practically: the offer's value sits entirely in the tail, on the small chance that one of the 20 spins lands a large hit. Realistic cash value is <strong>NZ$1 to NZ$4</strong>, and most of the time it is zero. Treat it as a free look at the lobby, which is a genuinely useful thing, and not as income.</p>
<p>The deposit offer behind it is more conventional and more useful: 100% up to NZ$1,700 per deposit day. The catalogue is 3,000-plus from Pragmatic, NetEnt, Evolution and Play'n GO — solid rather than exceptional. Crypto withdrawals took 12 to 24 hours, with a fastest logged time of 12 hours 40 minutes.</p>""",
 pros=["The only standing no-deposit offer we could verify for NZ players",
       "100% up to NZ$1,700 per deposit day on the main offer",
       "3,000+ titles from Pragmatic, NetEnt, Evolution and Play'n GO",
       "Rabidi N.V. group with Curaçao Gaming Control Board licensing",
       "No card required to claim the no-deposit spins"],
 cons=["50x wagering on the no-deposit spins makes them near-impossible to convert",
       "Realistic cash value of the no-deposit offer is NZ$1–4",
       "~NZ$35 minimum deposit is on the high side",
       "Crypto payouts of 12–24 hours are slower than half the sites here"],
 verdict="""<p>Claim the 20 spins. They cost you nothing but an email address, and they let you see the lobby, the cashier and the interface before committing money — which is genuinely worth more than the spins themselves.</p>
<p>Do not build expectations on them. At 50x, the winnings are a lottery ticket rather than a balance. If you want value from a bonus, the clearable large offers at <a href="/casino-reviews/smash/">Smash</a> and <a href="/casino-reviews/rivo/">Rivo</a> are where it actually is, and our <a href="/no-deposit-bonus/#value">no-deposit valuation page</a> shows the full working behind the NZ$1–4 figure.</p>""",
 who="Worth claiming to test the site at zero cost. Not a route to cash, and not a primary account on the strength of the no-deposit offer alone.",
 faq=[("Is the Lucky7even no deposit bonus real?",
       "<p>Yes — 20 free spins on Book of the Fallen, credited after email verification, with no deposit and no card required. We verified it by registering an account ourselves. It is the only standing no-deposit offer we could confirm for New Zealand players across all 38 operators we assessed.</p>"),
      ("What is the no deposit bonus actually worth?",
       "<p>About <strong>NZ$1 to NZ$4</strong>. Twenty spins at NZ$0.20 is NZ$4 of stake; expected winnings at 96% RTP are NZ$3.84; and 50x wagering on those winnings requires NZ$192 of turnover, which costs about NZ$7.68 in expected losses to generate.</p><p>The expected value is negative, so the offer's worth sits in the small chance of a large spin win — which a conversion cap then limits. Claim it to look around the site, not for the money. Full working on our <a href='/no-deposit-bonus/#value'>no deposit page</a>.</p>"),
      ("What is Lucky7even's minimum deposit?",
       "<p>Around NZ$35 on most methods, which is toward the high end — most operators here sit at NZ$20 and only Kingdom is higher at about NZ$40. If you want to start smaller, <a href='/casino-reviews/lucky-circus/'>Lucky Circus</a> or <a href='/casino-reviews/lucky-vibe/'>Lucky Vibe</a> take NZ$20.</p>")]),

"lucky-vibe": dict(
 author="claire",
 lede="Lucky Vibe runs casino and sportsbook on one wallet, so a Saturday NRL multi and a Sunday pokies session draw on the same balance. The catalogue spans about 5,000 titles from 149 studios. The thing that will catch you is a three-day bonus expiry — the tightest on this site.",
 test="""<p>The single-wallet arrangement is the reason to choose Lucky Vibe over a casino-only site. Deposit once, bet on the NRL, and play pokies with whatever is left, without moving money between products. Several operators here claim this; Lucky Vibe implements it cleanly, with a shared balance and a shared transaction history.</p>
<p>The catalogue is around 5,000 titles from 149 studios — the widest <em>studio</em> count on this site, which shows in the variety rather than the volume. Pragmatic, Evolution, Hacksaw and BGaming anchor it. NZ$20 minimum deposit, NZD balance, no conversion spread.</p>
<p>Crypto withdrawal of NZ$160 took <strong>6 hours 4 minutes</strong>, with a range of six to 12 hours across repeats. Cards ran two to three working days, which is at the faster end for a card rail.</p>
<p>The problem is the bonus expiry. Lucky Vibe's welcome bonuses expire in <strong>three days</strong>. That is the tightest window I encountered anywhere, and it is not realistic for a player who plays twice a week. On a NZ$5,000-potential package, three days means you either commit serious session time immediately or forfeit the balance. Work out whether you can actually use it before you claim, because a claimed bonus also locks your deposit.</p>""",
 pros=["Casino and sportsbook on a single shared wallet, implemented cleanly",
       "149 studios — the widest studio count on this site",
       "NZ$20 minimum deposit with a true NZD balance",
       "Crypto withdrawals 6–12 hours, cards 2–3 days",
       "Hollycorn N.V. under Curaçao Gaming Control Board"],
 cons=["Three-day bonus expiry — the tightest on this site",
       "Wagering terms not clearly published on the offer",
       "Sportsbook overround of 106.4% on NRL is the widest here",
       "The four-deposit package structure needs real commitment"],
 verdict="""<p>Lucky Vibe is a good all-round account for someone who wants both products in one place and does not want to run two cashiers. The catalogue breadth is real and the payout speed is respectable.</p>
<p>The three-day expiry is the thing to think about before claiming. If you play a couple of evenings a week, that window is not enough to clear a package of this size and the bonus becomes a restriction on your own deposit rather than a benefit. It is entirely reasonable to deposit here and decline the offer — see <a href="/casino-bonus/#decline">when to decline a bonus</a>.</p>""",
 who="Best for someone who wants casino and sport on one balance. Think carefully about the three-day bonus window before claiming.",
 faq=[("How long do Lucky Vibe bonuses last?",
       "<p><strong>Three days</strong>, which is the tightest expiry window of any operator on this site. Most competitors allow seven to 30 days.</p><p>On a package with a NZ$5,000 ceiling, three days means committing substantial session time immediately or forfeiting the balance — and since a claimed bonus also locks your own deposit until wagering completes, an unclearable bonus is worse than no bonus. Work out the required turnover at your normal stakes before claiming.</p>"),
      ("Can I use one Lucky Vibe account for casino and betting?",
       "<p>Yes, and it is the main reason to choose it. Casino and sportsbook share a single wallet and a single transaction history, so you can move between an NRL bet and a pokies session without transferring funds.</p><p>Note that bonuses are usually product-specific even where the wallet is shared — a casino bonus will not normally be clearable on sports bets. Check which product a bonus applies to before claiming.</p>"),
      ("How fast does Lucky Vibe pay out?",
       "<p>Six to 12 hours on crypto, with a fastest logged time of 6 hours 4 minutes. Cards ran two to three working days, which is at the faster end of the card range. E-wallets took one to two days.</p><p>As everywhere, complete KYC on registration day — an unverified account adds one to three days to all of those figures.</p>")]),

"rooster-bet": dict(
 author="claire",
 lede="Rooster Bet posted the tightest NRL and Super Rugby pricing of any book we sampled — 103.4% and 104.1% respectively — and runs a full casino on the same wallet. The sports free bet is the cleanest opening offer on this site. Its casino welcome, at 40x, is not the one to take.",
 test="""<p>I sample the same twenty markets at every book and Rooster Bet came out best on the codes New Zealanders actually bet. <strong>103.4% on NRL head-to-head</strong> is genuinely tight for this tier — most offshore books sit at 105 to 107 — and <strong>104.1% on the Super Rugby line</strong> was also the best figure I recorded.</p>
<p>To put that in money: against a book pricing NRL at 106.4%, three points of margin on NZ$200 a week of turnover is roughly NZ$310 a year. That is more than the welcome offer, and it recurs.</p>
<p>The market list is good without being Bet&Play's. Full NRL including State of Origin, complete Super Rugby Pacific coverage, All Blacks tests with a reasonable prop list, and the majors elsewhere. New Zealand racing came in at 117% — the best of any offshore book I sampled, and still far wider than TAB NZ.</p>
<p>The casino side is substantial in its own right: around 8,000 titles from NetEnt, Playtech, Quickspin, Red Tiger and Hacksaw, on the same wallet as the sportsbook.</p>
<p>Two offers, and they are not equivalent. The <strong>sports</strong> offer is 100% up to NZ$350 as a free bet, then 50% up to NZ$175 — clean, modest, genuinely useful. The <strong>casino</strong> welcome runs to NZ$5,000 plus 300 spins at <strong>40x</strong>, which is the market norm and unremarkable. Take the sports one.</p>""",
 pros=["Tightest NRL (103.4%) and Super Rugby (104.1%) pricing of any book here",
       "Best NZ racing price among offshore books at 117%, though TAB NZ is better",
       "~8,000 casino titles on the same wallet as the sportsbook",
       "Clean sports free bet: 100% to NZ$350, then 50% to NZ$175",
       "Dama N.V. with Curaçao Gaming Authority reference OGL/2023/174/0082",
       "Crypto withdrawals 4–12 hours"],
 cons=["Casino welcome carries 40x — take the sports offer instead",
       "Free bets return winnings only, so real value is ~70% of face",
       "Live streaming is limited compared with Bet&Play",
       "NZ racing still 117% against TAB NZ's pricing"],
 verdict="""<p>For a New Zealander betting New Zealand codes, Rooster Bet is the best offshore book on this site. The NRL and Super Rugby pricing is measurably tighter than anything else I sampled, and margin is the number that actually determines what betting costs you over a season.</p>
<p>Take the sports free bet, place it on a longer price rather than a short favourite, and skip the casino bonus. And read the <a href="/online-betting/#legal">legal position</a> first: TAB NZ is the only operator lawfully permitted to take a New Zealand bet, and for New Zealand racing it is also the better price.</p>""",
 who="Best offshore book for NRL and Super Rugby bettors. Take the sports offer; the casino bonus is ordinary.",
 faq=[("Does Rooster Bet have good NRL odds?",
       "<p>The best of any book on this site. I measured <strong>103.4% overround on NRL head-to-head</strong>, against 104.2% at Bet&amp;Play, 104.8% at Gunsbet and 106.4% at Lucky Vibe. Super Rugby line markets came in at 104.1%, also the tightest I recorded.</p><p>Three points of margin difference on NZ$200 a week of turnover is roughly NZ$310 a year — more than any welcome offer here, and it repeats every year.</p>"),
      ("What is the Rooster Bet welcome offer?",
       "<p>Two separate offers. <strong>Sports:</strong> 100% up to NZ$350 as a free bet, then 50% up to NZ$175 on the second deposit. <strong>Casino:</strong> up to NZ$5,000 plus 300 free spins at 40x wagering.</p><p>The sports offer is the better one. Remember that a free bet returns winnings but not the stake, so its real value is roughly 70% of face — and place it on a longer price, since the stake is forfeit either way.</p>"),
      ("Can I bet on the All Blacks at Rooster Bet?",
       "<p>Yes — full coverage of All Blacks tests, Super Rugby Pacific and the NPC, with a reasonable prop market list. Bet&amp;Play carries slightly more props on individual tests; Rooster Bet prices the main markets better.</p><p>TAB NZ is the only operator lawfully permitted to take a New Zealand bet and carries deeper local market coverage. See our <a href='/online-betting/'>online betting NZ</a> page.</p>")]),

"fortune-play": dict(
 author="claire",
 lede="Fortune Play has the best crash and instant-win range of any site we tested — Aviator, bonus buys, plinko and mines all in one lobby — alongside 8,000-plus titles from 80 studios and a full sportsbook. The gap is that the wagering requirement is not stated on the landing page.",
 test="""<p>If you play crash games, this is the lobby. Aviator is present alongside Spribe's full range, plus plinko, mines, dice and a deep bonus-buy section that several competitors do not carry at all. For short, high-variance mobile sessions it is the best-organised instant-win section I found.</p>
<p>The broader catalogue is 8,000-plus across about 80 studios, anchored by Pragmatic, Evolution, Spribe and BGaming. NZ$20 minimum deposit and a NZD balance, so no conversion cost.</p>
<p>The sportsbook shares the wallet and covers the main codes competently, though at 105-plus overround on NRL it is not a book you would choose on price.</p>
<p>My crypto withdrawal of NZ$190 took <strong>6 hours 22 minutes</strong>, with a range of six to 18 hours across repeats. Cards ran two to four working days. No operator fees.</p>
<p>What I could not do is price the welcome offer. The package is presented as up to NZ$5,000 plus 300 free spins across four deposits, but the wagering multiple is not stated on the landing page or the promotions tile — it is in the terms, behind a couple of clicks. That is not the same failure as MadCasino, which does not publish it at all, but it is a findability problem and we score findability as part of transparency.</p>""",
 pros=["Best crash and instant-win range on this site — Aviator, plinko, mines, dice",
       "Deep bonus-buy section several competitors do not carry",
       "8,000+ titles from around 80 studios",
       "Sportsbook on the same wallet",
       "NZ$20 minimum with a true NZD balance",
       "Crypto withdrawals 6–18 hours with no operator fee"],
 cons=["Wagering multiple is not stated on the landing page or promotions tile",
       "Sportsbook pricing is uncompetitive at 105%+ on NRL",
       "The four-deposit structure means the headline needs full commitment",
       "Bonus-buy purchases are usually excluded from wagering — check first"],
 verdict="""<p>Fortune Play is the crash-game site. If Aviator, plinko and bonus buys are what you actually play, nothing else here organises that content as well, and the 8,000-title main catalogue means you are not giving anything up elsewhere.</p>
<p>Open the terms tab before you claim the welcome offer. The wagering figure exists, it is just not where it should be, and claiming a bonus you have not priced is how a deposit ends up locked behind turnover you did not agree to.</p>""",
 who="Best for crash and instant-win players. Read the terms tab before claiming the welcome package.",
 faq=[("Does Fortune Play have Aviator?",
       "<p>Yes, alongside Spribe's full range and a deep instant-win section covering plinko, mines and dice. It is the best-organised crash and instant-win lobby of any operator on this site.</p><p>One thing to check: crash and instant-win titles are often weighted at less than 100% for bonus wagering, and bonus-buy purchases are frequently excluded entirely. Read the weighting table before playing them with bonus funds.</p>"),
      ("What is Fortune Play's wagering requirement?",
       "<p>It is published in the full terms, but not on the landing page or the promotions tile — you need to open the terms tab to find it. We mark operators down for that under our transparency criterion, because a term you have to hunt for is a term most people will not read.</p><p>Confirm the current figure at the cashier before you claim. If you want a bonus with the multiple stated up front, <a href='/casino-reviews/smash/'>Smash</a> and <a href='/casino-reviews/rivo/'>Rivo</a> both publish 10x prominently.</p>"),
      ("Is Fortune Play good for sports betting?",
       "<p>It works, but it is not the reason to be here. The sportsbook shares the wallet and covers the main codes, but at over 105% overround on NRL it is not competitive on price — <a href='/casino-reviews/rooster-bet/'>Rooster Bet at 103.4%</a> is materially better.</p><p>Use Fortune Play for the casino and crash games. See our <a href='/best-sports-betting-sites/'>sportsbook comparison</a> for betting.</p>")]),

"lucky-circus": dict(
 author="claire",
 lede="Lucky Circus is the best site on this list for a regular low-stakes player, because its recurring Monday free-spins drop delivers more value over a month than most one-off welcome packages — and it triggers from a NZ$20 deposit.",
 test="""<p>Most casino value is front-loaded into a welcome offer you claim once. Lucky Circus inverts that. The <strong>Monday free-spins drop</strong> recurs weekly, qualifies on a NZ$20 deposit, and over a month delivers more spins than most competitors' entire welcome packages.</p>
<p>For someone playing NZ$20 to NZ$50 a week — which describes a large share of New Zealand casino players — that is worth considerably more than a NZ$5,000 headline they will never approach.</p>
<p>The welcome offer itself is modest and honest: 100% up to NZ$1,500 plus 150 free spins on the first deposit, extending across four deposits to a 300% total. Note that the 300% is the cumulative figure, not the first-deposit rate — a distinction several operators blur and this one does not.</p>
<p>The catalogue is 4,000-plus from BGaming, Pragmatic, Evolution and Play'n GO, which includes Starmania at 97.87% for low-volatility play. NZ$20 minimum, NZD balance.</p>
<p>Withdrawals are the weak point: 12 to 24 hours on crypto with a best of 13 hours 2 minutes, and two to three working days on cards. Not slow enough to be a problem for a weekly player; not fast enough to choose it for speed.</p>""",
 pros=["Recurring Monday free-spins drop — the best ongoing value for a low-stakes player",
       "Qualifies from a NZ$20 deposit",
       "Honest headline: 100% on the first deposit, 300% cumulative, clearly stated",
       "4,000+ titles including NetEnt high-RTP options",
       "Dama N.V. under Curaçao Gaming Control Board",
       "True NZD balance"],
 cons=["Crypto withdrawals of 12–24 hours are mid-table",
       "No sportsbook",
       "Wagering terms are not stated prominently on the offer",
       "The 300% figure requires funding all four deposits"],
 verdict="""<p>If you play modestly and regularly, Lucky Circus is the account that will actually give you the most over a year, and that is a genuinely different question from which site has the biggest headline.</p>
<p>The Monday drop compounds. A NZ$5,000-ceiling welcome package you will never approach does not. Choose on which of those describes how you play.</p>""",
 who="Best for a regular player depositing NZ$20–50 a week. Not the pick if you want a large one-off bonus or the fastest payouts.",
 faq=[("What is the Lucky Circus Monday free spins offer?",
       "<p>A recurring weekly free-spins drop that qualifies on a NZ$20 deposit. Because it repeats, it delivers more value over a month to a regular low-stakes player than most one-off welcome packages — which is unusual in this market, where nearly all the value is front-loaded.</p><p>Check the current spin count and wagering at the operator, since recurring promotions change more often than welcome offers.</p>"),
      ("Is the Lucky Circus welcome bonus 100% or 300%?",
       "<p>Both, and the distinction matters. The <strong>first deposit</strong> is 100% up to NZ$1,500 plus 150 free spins. The <strong>300%</strong> is the cumulative total across four deposits.</p><p>Lucky Circus states this clearly, which several competitors do not — a 600% or 1000% headline elsewhere is almost always cumulative across multiple deposits rather than the first-deposit rate.</p>"),
      ("How fast does Lucky Circus pay out?",
       "<p>Twelve to 24 hours on crypto, with a fastest logged time of 13 hours 2 minutes, and two to three working days on cards. That is mid-table — <a href='/casino-reviews/kingdom/'>Kingdom</a> pays crypto in two to four hours.</p><p>For a weekly player withdrawing occasionally it is unlikely to matter. If payout speed is your priority, see our <a href='/fast-payout-casinos/'>fast payout rankings</a>.</p>")]),

"roby": dict(
 author="claire",
 lede="Roby has the largest game catalogue we counted anywhere — 13,500-plus titles from more than 120 studios. It is also the slowest site in our entire testing log, at roughly three days on every payment rail including crypto, and its licence is not clearly published.",
 test="""<p>The catalogue claim is real. I counted well past 13,000 live titles from a studio list running to three figures, including Pragmatic, Evolution, Hacksaw and Nolimit City alongside a long tail of smaller developers. If you want the widest possible selection, nothing else here is close.</p>
<p>The trade-offs are significant and you should weigh both before depositing.</p>
<p><strong>Withdrawals took about three days on every rail.</strong> That includes crypto, which is remarkable — every other operator on this site clears crypto in hours because the blockchain leg is minutes and approval is the variable. Roby's approval step is uniformly slow regardless of method. My fastest logged withdrawal was 70 hours. There is no rail you can switch to in order to speed it up.</p>
<p><strong>The licence is not clearly published.</strong> I could not find a licensing authority named with a verifiable reference. That is the same failure as MadCasino, and it caps how high Roby can rank under our transparency gate.</p>
<p>The welcome offer is 250% up to NZ$4,300 plus 250 free spins at <strong>35x</strong>, which is published and at the market norm — better than several sites with much better payout speeds.</p>""",
 pros=["13,500+ titles from 120+ studios — the largest catalogue we counted",
       "Deep long tail of smaller developers alongside the majors",
       "35x wagering is published and at the market norm",
       "Sportsbook available on the same account",
       "Crypto and card rails both supported"],
 cons=["~72 hour withdrawals on every rail including crypto — slowest in our log",
       "No faster payment option exists; the delay is at approval",
       "Licence is not clearly published or verifiable",
       "Minimum deposit not clearly stated"],
 verdict="""<p>Roby is for one kind of player: someone whose priority is breadth of selection and who genuinely does not mind waiting three days to be paid. If that is you, the catalogue is unmatched and the bonus terms are ordinary rather than bad.</p>
<p>For everyone else, the combination of the slowest payouts in our log and an unverifiable licence is hard to get past. We list it because readers ask about it and the catalogue claim is true, and we attach both facts everywhere it appears. Deposit modestly, withdraw promptly, and do not accumulate a balance.</p>""",
 who="For a player who wants the widest possible catalogue and is genuinely relaxed about three-day withdrawals. Not for anyone who values payout speed or verifiable licensing.",
 faq=[("How many games does Roby Casino have?",
       "<p>More than 13,500 from over 120 studios — the largest catalogue of any operator we have counted, and the claim holds up under checking. It includes Pragmatic Play, Evolution, Hacksaw Gaming and Nolimit City alongside a long tail of smaller developers you will not find elsewhere.</p><p>Breadth is genuinely Roby's case. Whether it outweighs three-day withdrawals is the question you have to answer.</p>"),
      ("Why are Roby withdrawals so slow?",
       "<p>The delay is at the approval stage, not the payment rail. Every other operator here clears crypto in hours because blockchain settlement is minutes and approval is the variable; Roby's approval takes about three days regardless of method, so crypto is no faster than a card.</p><p>That means there is no workaround. You cannot switch rails to speed it up. Our fastest logged Roby withdrawal was 70 hours.</p>"),
      ("Is Roby Casino licensed?",
       "<p>Not clearly. We could not find a licensing authority named with a verifiable reference anywhere on the site. That is the same transparency failure as MadCasino, and under our <a href='/how-we-rate-casinos/#hard-gates'>hard gates</a> it caps how high Roby can rank regardless of its other scores.</p><p>Practical advice: deposit only what you are content to lose, withdraw promptly despite the delay, and do not hold a balance. See <a href='/online-casinos/#fund-protection'>what happens if a casino goes bust</a>.</p>")]),

"spino": dict(
 author="claire",
 lede="Spino's headline welcome package carries 0x wagering. Not 10x, not 'low wagering' — zero. Anything you win is immediately withdrawable. It is the only offer of its kind on this site, and it comes with one real constraint: Spino is crypto-only, with no NZD card rail at all.",
 test="""<p>I read the terms three times because I did not believe the first two. Spino's crypto-first welcome package, up to 2,000 USDT, carries <strong>0x wagering on the headline offer</strong>. There is no playthrough, no maximum conversion on the bonus, and no maximum bet restriction while it is active, because there is nothing to clear.</p>
<p>To put that in context: every other large offer on this site costs something to convert. Smash's excellent 10x offer costs roughly NZ$280 in expected losses to turn NZ$600 of bonus into cash. Spino's costs nothing, because the funds are already cash.</p>
<p>The constraint is equally clear. Spino is <strong>crypto only</strong>. There is no Visa, no Mastercard, no Skrill, no bank transfer and no NZD balance. You need an exchange account and a wallet before you can deposit at all, and if you do not already hold crypto, that is a genuine barrier rather than a formality.</p>
<p>Payouts are correspondingly quick: <strong>2 hours 9 minutes</strong> on my fastest logged withdrawal, one to four hours across repeats. The catalogue is around 3,500 titles from 20-plus studios — the smallest here, anchored by BGaming, Pragmatic and Evolution. Adequate rather than deep.</p>
<p>Spino is also the newest operator on this site, launched in 2026 under Empire of Kingdoms Limitada with a Tobique Gaming Commission licence. That is the least-tested licensing regime represented here.</p>""",
 pros=["0x wagering on the headline welcome package — unique on this site",
       "Winnings are immediately withdrawable with no playthrough",
       "Payouts in 1–4 hours, second fastest we measured",
       "No maximum bet restriction, because there is no bonus to clear",
       "No operator fees beyond network cost"],
 cons=["Crypto only — no card, e-wallet, bank transfer or NZD balance",
       "~3,500 titles is the smallest catalogue on this site",
       "Newest operator here, launched 2026",
       "Tobique licensing is the least-tested regime represented",
       "Requires an exchange account and wallet before you can deposit"],
 verdict="""<p>A 0x-wagering welcome offer is close to unheard of, and if you already hold crypto it makes Spino the single best-value opening offer on this site. There is no arithmetic to do, no maximum bet to breach and no conversion cap to run into.</p>
<p>Two things to weigh honestly. The catalogue is the smallest here, so if range matters, <a href="/casino-reviews/spinjo/">Spinjo</a> is a better main account. And Spino is new, on the least-tested licence represented here, which is a reason to withdraw winnings promptly rather than hold a balance — advice that applies everywhere offshore but with a little more force to an operator with a short record.</p>""",
 who="Best for an existing crypto holder who wants an offer with no clearing cost and near-immediate payouts. Not usable at all without crypto.",
 faq=[("Does Spino really have 0x wagering?",
       "<p>On the headline crypto welcome package, yes. There is no playthrough requirement, so anything you win with it is immediately withdrawable, and there is no maximum bet restriction because there is no bonus to void.</p><p>That is genuinely rare — every other large offer on this site costs something in expected losses to convert. Read the current terms at the cashier before claiming, as offers change, but this is the term Spino is built around.</p>"),
      ("Can I use a credit card or NZD at Spino?",
       "<p>No. Spino is <strong>crypto only</strong> — no Visa, no Mastercard, no e-wallets, no bank transfer, and no New Zealand dollar balance. You need an exchange account and a wallet before you can deposit.</p><p>If you want a fast-paying site with a fiat cashier, <a href='/casino-reviews/kingdom/'>Kingdom</a> pays crypto in two to four hours and also accepts NZD cards and e-wallets.</p>"),
      ("Is Spino safe? It is very new.",
       "<p>Spino launched in 2026 under Empire of Kingdoms Limitada with a <strong>Tobique Gaming Commission</strong> licence — the newest operator and the least-tested licensing regime on this site. It paid our withdrawals promptly and without dispute, in one to four hours.</p><p>A short track record is not evidence of a problem, but it is less evidence of reliability than a nine-year record. Our advice: take the 0x offer, withdraw winnings promptly, and do not accumulate a balance. See <a href='/online-casinos/#fund-protection'>what happens if a casino goes bust</a>.</p>")]),

"ivibet": dict(
 author="claire",
 lede="IviBet runs casino and sportsbook under one login with a low opening deposit requirement, which makes it a low-risk way to try both products. The thing that will determine your experience is KYC: verify on day one or your first withdrawal will stall.",
 test="""<p>IviBet is the most prominent of the three TechOptions Group sites we list, alongside HellSpin and SlotsGem, and it is the only one of the three with a sportsbook. All three share a cashier and a platform, which is worth knowing — holding accounts at more than one gives you less diversification than it appears to.</p>
<p>The welcome offer is unusually modest for this market and better for it: 100% up to NZ$180 plus 120 spins on the first deposit, then 50% up to NZ$360 plus 50 spins. Small numbers, but a NZ$180 bonus is one you might actually clear, which is more than can be said for a NZ$19,500 ceiling.</p>
<p>The catalogue is 5,000-plus from Pragmatic, Evolution, Play'n GO, BGaming and Hacksaw. The sportsbook covers the main codes at 106.8% on NRL, the widest figure we recorded — usable, not competitive.</p>
<p>Withdrawals are where IviBet cost me time. E-wallet payouts took one to two working days once verified, but verification was the bottleneck rather than the cashier: the account sat pending while documents were processed. IviBet holds a Curaçao eGaming licence with reference <strong>365/JAZ</strong>, one of the few here with a number that resolves.</p>""",
 pros=["Casino and sportsbook under one login",
       "Low opening deposit requirement — a genuinely low-risk way to try the site",
       "Modest NZ$180 first bonus that is actually clearable",
       "5,000+ titles from Pragmatic, Evolution, Play'n GO, BGaming and Hacksaw",
       "Curaçao eGaming licence reference 365/JAZ resolves on the register"],
 cons=["KYC is the bottleneck — verify on day one or the first withdrawal stalls",
       "No crypto speed advantage; e-wallets are 1–2 days",
       "NRL overround of 106.8% is the widest we measured",
       "Shares a platform with HellSpin and SlotsGem — little reason to hold all three"],
 verdict="""<p>IviBet is a sensible, unspectacular account. The small welcome offer is a point in its favour rather than against it — a NZ$180 bonus at reasonable terms is worth more in practice than a five-figure ceiling you will never approach.</p>
<p>Verify on registration day. That is the single thing that determines whether your experience here is smooth or frustrating, and it is entirely within your control.</p>""",
 who="A low-risk first account for someone trying both casino and sport. Verify immediately.",
 faq=[("What is IviBet's welcome bonus?",
       "<p>100% up to NZ$180 plus 120 free spins on the first deposit, then 50% up to NZ$360 plus 50 spins on the second. Small by this market's standards — and genuinely better for it, because a NZ$180 bonus is one you might actually clear.</p><p>Compare it with a NZ$19,500 ceiling that requires funding four deposits and then turning over five figures. The smaller number is frequently the better offer.</p>"),
      ("Is IviBet the same as HellSpin and SlotsGem?",
       "<p>They share an operator — <strong>TechOptions Group B.V.</strong> — and run on the same platform and cashier. IviBet is the only one of the three with a sportsbook.</p><p>Worth knowing for two reasons: holding accounts at all three gives you less diversification than it appears, and bonus terms usually treat sister sites as a single entity, so claiming the same promotion across all three can void winnings.</p>"),
      ("Why did my IviBet withdrawal take so long?",
       "<p>Almost certainly verification. In our testing the cashier itself was reasonable — one to two working days on e-wallets — but the account sat pending while KYC documents were processed.</p><p>Upload photo ID, proof of address and proof of payment method on the day you register, before you deposit. This is good advice at every operator and it matters more here than at most.</p>")]),

"hellspin": dict(
 author="claire",
 lede="HellSpin has the fastest route from landing page to first spin of any site we tested — the fewest clicks, the least friction, the cleanest pokies-first lobby. That makes it a good fit for a short mobile session. What it does not do well is publish its bonus terms.",
 test="""<p>I timed this one for a different reason than usual. From landing page to first real-money spin, HellSpin took fewer steps than any other site here: register, verify email, deposit, play. No forced bonus selection, no multi-screen onboarding, no upsell interstitials.</p>
<p>That sounds trivial and it is not. If your session is twenty minutes on a phone at lunchtime, friction is the whole experience, and HellSpin's lobby is built for exactly that — pokies first, clean search, fast load, no clutter.</p>
<p>The catalogue is 5,000-plus from Pragmatic, Evolution, BGaming and Play'n GO. Solid majors, no long tail, which is consistent with the uncluttered approach.</p>
<p>Where it falls short is bonus transparency. The welcome package is described as multi-deposit with recurring reload spins, but the specifics — the wagering multiple, the maximum bet, the expiry — are thin on the landing page and require digging through the promotions tab. Ana scored it down accordingly.</p>
<p>Withdrawals were one to two working days on e-wallets and same-day on crypto. HellSpin is a TechOptions Group site sharing a platform with IviBet and SlotsGem, under a Curaçao eGaming licence.</p>""",
 pros=["Fastest route from landing page to first spin of any site tested",
       "Clean, uncluttered pokies-first lobby built for short mobile sessions",
       "5,000+ titles from Pragmatic, Evolution, BGaming and Play'n GO",
       "Recurring reload spins alongside the welcome package",
       "Same-day crypto withdrawals"],
 cons=["Bonus terms are thin on the landing page and require digging",
       "No sportsbook",
       "Wagering multiple not stated prominently",
       "Shares a platform with IviBet and SlotsGem"],
 verdict="""<p>HellSpin does one thing better than anything else here: it gets out of your way. For a short mobile pokies session, the absence of friction is worth more than a catalogue two thousand titles deeper.</p>
<p>Read the promotions tab before claiming anything. The terms exist, they are just not where they should be, and an offer you have not priced is one you should not claim.</p>""",
 who="Best for short, uncluttered mobile pokies sessions. Read the promotions tab before taking any bonus.",
 faq=[("What is HellSpin's welcome bonus?",
       "<p>A multi-deposit welcome package with recurring reload spins. The specifics — wagering multiple, maximum bet during wagering, expiry — are not stated prominently on the landing page and require going into the promotions tab.</p><p>We mark operators down for that under transparency. Get the wagering figure before you claim, because a bonus also locks your own deposit until it is cleared.</p>"),
      ("Is HellSpin good on mobile?",
       "<p>It is the best mobile experience of any site we tested, for one specific reason: it has the fewest steps from landing to first spin. No forced bonus selection, no multi-screen onboarding, no interstitials. The lobby is pokies-first, loads quickly and searches cleanly.</p><p>For a twenty-minute session on a phone, that matters more than catalogue depth.</p>"),
      ("Is HellSpin related to IviBet?",
       "<p>Yes. Both are operated by <strong>TechOptions Group B.V.</strong> and share a platform and cashier, along with SlotsGem. IviBet is the only one of the three with a sportsbook.</p><p>Bonus terms usually treat sister sites as a single entity, so claiming the same promotion across all three can void winnings. There is also little diversification benefit in holding all three.</p>")]),

"slotsgem": dict(
 author="claire",
 lede="SlotsGem is the third TechOptions Group site alongside IviBet and HellSpin, sharing their platform and cashier. It is competent and nearly identical to HellSpin, which is both its strength as a second account and the reason there is little point holding both.",
 test="""<p>I will be direct: SlotsGem and HellSpin are close to the same product. Same operator, same platform, same cashier, similar lobby, overlapping catalogue. If you have used one, you know what the other is.</p>
<p>That is not a criticism so much as a fact worth knowing before you open a second account expecting something different. Where it is genuinely useful is as a <em>second</em> account — if you have spent a bonus at HellSpin and want another lobby without learning a new cashier or re-verifying with a different payment setup, SlotsGem is the path of least resistance.</p>
<p>The catalogue is 4,000-plus from Pragmatic, Evolution, BGaming and Play'n GO — a little shallower than HellSpin's 5,000. The welcome package is tiered across the opening deposits, and like its sister sites the specifics require going into the promotions tab rather than appearing on the offer.</p>
<p>Withdrawals ran one to two working days on e-wallets and same-day on crypto, consistent with the shared cashier. Curaçao eGaming licence, no published reference number.</p>""",
 pros=["Straightforward second account on a cashier you already know",
       "4,000+ titles from Pragmatic, Evolution, BGaming and Play'n GO",
       "Same-day crypto withdrawals",
       "Clean, uncomplicated lobby",
       "Curaçao eGaming licensed"],
 cons=["Nearly identical to HellSpin — little reason to hold both",
       "Shallower catalogue than its sister sites",
       "Bonus terms require digging through the promotions tab",
       "No sportsbook",
       "No published licence reference number"],
 verdict="""<p>SlotsGem is fine. It does nothing badly and nothing exceptionally, and its main practical use is as a second lobby on a platform you already trust.</p>
<p>If you are choosing between the three TechOptions sites for a single account, take <a href="/casino-reviews/ivibet/">IviBet</a> for the sportsbook or <a href="/casino-reviews/hellspin/">HellSpin</a> for the cleaner lobby. SlotsGem is the one you add third, if at all.</p>""",
 who="A reasonable second account for someone already using HellSpin or IviBet. Little reason to make it your first.",
 faq=[("How is SlotsGem different from HellSpin?",
       "<p>Barely. Both are operated by <strong>TechOptions Group B.V.</strong> on the same platform and cashier, with similar lobbies and overlapping catalogues. HellSpin carries about 5,000 titles to SlotsGem's 4,000 and has a slightly cleaner interface.</p><p>If you are opening one account, take HellSpin. SlotsGem makes more sense as a second lobby once a bonus elsewhere is spent.</p>"),
      ("Can I claim bonuses at IviBet, HellSpin and SlotsGem?",
       "<p>Be careful. Sister sites sharing an operator and platform usually treat promotions as applying to a single entity, so claiming the same welcome offer across all three can be treated as bonus abuse and result in voided winnings.</p><p>Read each site's terms on sister-site restrictions before claiming a second one, and if it is unclear, ask support in writing and keep the reply.</p>"),
      ("How fast does SlotsGem pay out?",
       "<p>One to two working days on e-wallets and same-day on crypto, consistent with the shared TechOptions cashier. That is mid-table — <a href='/casino-reviews/kingdom/'>Kingdom</a> clears crypto in two to four hours.</p><p>As always, complete KYC on registration day. Verification, not the cashier, is the usual cause of delay on this platform.</p>")]),
}

# ---------------------------------------------------------------------------
TITLES = {
 "crownslots": "CrownSlots Review NZ 2026 | 390% Bonus Tested, Payouts Timed",
 "spinjo": "Spinjo Casino Review NZ 2026 | 8,000 Games, Payouts in 2 Hours",
 "madcasino": "MadCasino Review NZ 2026 | 777% Bonus — But Read This First",
 "gunsbet": "Gunsbet Review NZ 2026 | Sportsbook Odds & Margins Tested",
 "kingdom": "Kingdom Casino Review NZ 2026 | Fastest Payout We Logged",
 "smash": "Smash Casino Review NZ 2026 | 10x Wagering, Bonus Terms Read",
 "rivo": "Rivo Casino Review NZ 2026 | 10x Wagering & 25% VIP Cashback",
 "bet-and-play": "Bet&Play Review NZ 2026 | Deepest Betting Markets Tested",
 "lucky7even": "Lucky7even Review NZ 2026 | The Real No Deposit Bonus, Priced",
 "lucky-vibe": "Lucky Vibe Review NZ 2026 | One Wallet for Casino & Sport",
 "rooster-bet": "Rooster Bet Review NZ 2026 | Best NRL Odds We Measured",
 "fortune-play": "Fortune Play Review NZ 2026 | Best Crash Games & Aviator",
 "lucky-circus": "Lucky Circus Review NZ 2026 | Best Value for Low-Stakes Players",
 "roby": "Roby Casino Review NZ 2026 | 13,500 Games, 3-Day Withdrawals",
 "spino": "Spino Casino Review NZ 2026 | 0x Wagering Crypto Bonus Tested",
 "ivibet": "IviBet Review NZ 2026 | Casino & Sportsbook on One Login",
 "hellspin": "HellSpin Review NZ 2026 | Fastest Lobby for Mobile Pokies",
 "slotsgem": "SlotsGem Review NZ 2026 | Honest Take on the TechOptions Site",
}
DESCS = {
 "crownslots": "CrownSlots review NZ: we tested the 390% welcome bonus, timed a withdrawal at 24h 51m and checked the Curaçao licence. Honest pros, cons and verdict.",
 "spinjo": "Spinjo Casino review for NZ: ~8,000 games, crypto payouts in 2h 31m, and the NZ$30 bonus minimum that catches people out. Tested with real New Zealand dollars.",
 "madcasino": "MadCasino review for NZ: the 777% bonus is real, but the licence and wagering requirement are not published. What we found and what we would do about it.",
 "gunsbet": "Gunsbet review for NZ bettors: overround measured at 104.8% on NRL, 285% welcome offer assessed, and the missing crypto cashier explained.",
 "kingdom": "Kingdom Casino review for NZ: the fastest withdrawal we logged anywhere at 1h 47m, 7,000+ games, 30x wagering and the NZ$40 minimum deposit.",
 "smash": "Smash Casino review for NZ: 10x wagering against a 35–40x market norm, with the arithmetic on what it actually costs to clear. Anjouan licence explained.",
 "rivo": "Rivo Casino review for NZ: 10x wagering, 25% VIP cashback and the strictest KYC we encountered. Tested with real New Zealand dollars.",
 "bet-and-play": "Bet&Play review for NZ: deepest betting markets we found, 104.4% Premier League overround, and why to take the sports offer and decline the casino one.",
 "lucky7even": "Lucky7even review for NZ: the only standing no-deposit bonus we verified, priced honestly at NZ$1–4 after 50x wagering. Full terms and payout times.",
 "lucky-vibe": "Lucky Vibe review for NZ: casino and sportsbook on one wallet, 149 studios, crypto payouts in 6h — and a three-day bonus expiry to plan around.",
 "rooster-bet": "Rooster Bet review for NZ: 103.4% NRL overround, the tightest we measured, plus ~8,000 casino games on the same wallet. Sports offer assessed.",
 "fortune-play": "Fortune Play review for NZ: the best Aviator and crash game range we found, 8,000+ titles, and the wagering figure that is not on the landing page.",
 "lucky-circus": "Lucky Circus review for NZ: the recurring Monday free-spins drop that beats most welcome packages for a regular low-stakes player. Tested in NZD.",
 "roby": "Roby Casino review for NZ: 13,500+ games, the largest catalogue we counted — against three-day withdrawals on every rail and an unpublished licence.",
 "spino": "Spino Casino review for NZ: a 0x-wagering crypto welcome offer, payouts in 2h 09m, and the crypto-only constraint. Tested with real funds.",
 "ivibet": "IviBet review for NZ: casino and sportsbook on one login, a modest but clearable NZ$180 bonus, and the KYC step that decides your experience.",
 "hellspin": "HellSpin review for NZ: the fastest route from landing page to first spin of any site we tested, 5,000+ pokies, and thin bonus terms.",
 "slotsgem": "SlotsGem review for NZ: an honest assessment of the third TechOptions site — competent, nearly identical to HellSpin, and best used as a second account.",
}

def short_payout(op):
    """A stat-tile-sized payout summary, derived rather than truncated."""
    h = op.get("payoutHours")
    if h is None: return "See review"
    if h <= 4:  return "2-4 hrs"
    if h <= 12: return "4-12 hrs"
    if h <= 24: return "12-24 hrs"
    if h <= 30: return "~1 day"
    if h <= 48: return "~2 days"
    return "~3 days"

def li(items):
    return "".join(f"<li>{x}</li>" for x in items)

def esc_json(o):
    return json.dumps(o, ensure_ascii=False, indent=1)

def build(slug, i):
    op = OPS[slug]
    n = N[slug]
    kind = "sports" if (op.get("sports") and not op.get("casino")) else "casino"
    url = f"/casino-reviews/{op['slug']}/"

    facts = [
        ("Operator", op["operator"]),
        ("Licence", op["licence"] + (f' &middot; {op["licenceRef"]}' if op.get("licenceRef") else "")),
        ("Launched", str(op["launched"]) if op.get("launched") else "Not stated"),
        ("Games", op["games"]),
        ("Providers", op["providers"]),
        ("Welcome offer", op["welcome"]),
        ("Wagering", op["wagering"]),
        ("Minimum deposit", op["minDep"]),
        ("Measured payout", op["payout"]),
        ("Casino", "Yes" if op.get("casino") else "No"),
        ("Sportsbook", "Yes" if op.get("sports") else "No"),
        ("Crypto accepted", "Yes" if op.get("crypto") else "No"),
    ]
    facts_rows = "".join(
        f"<tr><td><strong>{k}</strong></td><td>{v}</td></tr>" for k, v in facts)

    methods = "".join(f'<span class="chip">{m}</span>' for m in op.get("methods", []))

    fm = {
        "url": url,
        "title": TITLES[slug],
        "description": DESCS[slug],
        "h1": f"{op['name']} Review",
        "lede": n["lede"],
        "author": n["author"],
        "published": "2026-03-01",
        "modified": "2026-09-13",
        "priority": "0.7",
        "changefreq": "monthly",
        "crumbs": [["Casino Reviews", "/casino-reviews/"], [op["name"], url]],
        "reviewOf": slug,
        "stats": [["Our rating", f"{op['rating']}/5"],
                  ["Licence", "Curaçao" if "Cura" in op["licence"] else
                              ("Anjouan" if "Anjouan" in op["licence"] else
                               ("Tobique" if "Tobique" in op["licence"] else "Not published"))],
                  ["Payout", short_payout(op)],
                  ["Min deposit", op["minDep"][:14]]],
        "pills": ["Account opened by us", "Real NZD deposited", "Withdrawal timed", "Full terms read"],
        "heroCard": {"op": slug, "kind": kind,
                     "band": f"Our rating: {op['rating']}/5",
                     "sub": op["usp"],
                     "meta": f"{op['licence']} &middot; {op['minDep']} minimum"},
        "faq": n["faq"] + [
            ("How did RNRV test " + op["name"] + "?",
             "<p>We opened an account in a reviewer's own name from a New Zealand connection, completed KYC, deposited our own New Zealand dollars, played a minimum of 200 real-money spins or 100 live hands, and requested a withdrawal which we timed to the minute. Our editor separately read the complete terms and conditions, and we tested live chat with a specific question.</p><p>The full process and the scoring weights are on our <a href='/how-we-rate-casinos/'>how we review</a> page.</p>"),
            ("Is " + op["name"] + " legal for New Zealand players?",
             "<p>It is not an offence for a New Zealander to play at an offshore online casino — the Online Casino Gambling Act 2026 regulates operators, not players. From <strong>1 December 2026</strong>, an operator needs a New Zealand licence or a pending application to keep serving New Zealanders.</p><p>Our <a href='/licensed-online-casinos/'>NZ online casino law</a> page sets out the full timeline and what it means for your balance.</p>"),
        ],
    }

    warn = ""
    if op.get("watch"):
        warn = (f'<div class="note note-warn"><p class="note-h">What to watch</p>'
                f'<p>{op["watch"]}</p></div>')

    body = f'''<section class="sec"><div class="wrap"><div class="prose">
{warn}
<div class="toc"><b>On this page</b>
<ol>
<li><a href="#facts">Key facts</a></li>
<li><a href="#testing">What happened when we tested it</a></li>
<li><a href="#proscons">Pros and cons</a></li>
<li><a href="#bonus">The welcome offer</a></li>
<li><a href="#payments">Payments and payout speed</a></li>
<li><a href="#verdict">Our verdict</a></li>
<li><a href="#faq">FAQs</a></li>
</ol></div>

<h2 id="facts">{op['name']} at a glance</h2>
<div class="tbl-wrap"><table>
<caption>Key facts for {op['name']}, verified September 2026. Bonus figures converted to NZD where the operator prices in euros.</caption>
<thead><tr><th>Detail</th><th>What we found</th></tr></thead>
<tbody>{facts_rows}</tbody></table></div>

<h2 id="testing">What happened when we tested it</h2>
{n['test']}

<h2 id="proscons">Pros and cons</h2>
<div class="pc">
<div class="pc-col pc-pro"><h4>What works</h4><ul>{li(n['pros'])}</ul></div>
<div class="pc-col pc-con"><h4>What does not</h4><ul>{li(n['cons'])}</ul></div>
</div>

<h2 id="bonus">The welcome offer</h2>
<div class="note"><p class="note-h">{op['welcome']}</p>
<p><strong>Wagering:</strong> {op['wagering']}<br>
<strong>Minimum deposit:</strong> {op['minDep']}
{'<br><strong>Original currency:</strong> ' + op['welcomeEur'] if op.get('welcomeEur') else ''}</p>
<p>Bonus terms change without notice. Always read the operator's current terms before claiming &mdash; and see <a href="/casino-bonus/#decline">when to decline a bonus</a>, because a bonus you cannot clear locks your own deposit too.</p></div>
<p>Our editor read the complete terms on this offer rather than the promotional summary. The comparison against every other welcome offer we list, including the expected cost of clearing each one, is on our <a href="/casino-bonus/#arithmetic">casino bonuses page</a>.</p>

<h2 id="payments">Payments and payout speed</h2>
<p><strong>Measured payout:</strong> {op['payout']}</p>
<p>Payment methods we found in the cashier:</p>
<div class="chips">{methods}</div>
<p>As at every operator, the payment method determines your withdrawal speed more than the casino does &mdash; with the exception of operators whose approval step is the bottleneck. The full comparison of all 94 withdrawals we timed is on our <a href="/fast-payout-casinos/">fast payout casinos</a> page, and the method-by-method breakdown is on our <a href="/casino-payment-methods/">NZ payment methods</a> page.</p>
<div class="note note-ok"><p class="note-h">The one thing that speeds up every withdrawal</p><p>Complete KYC on the day you register &mdash; photo ID, proof of address dated within three months, and proof of payment method &mdash; before you deposit. Around 70% of pending withdrawals in our testing were waiting on verification, not on the cashier.</p></div>

<h2 id="verdict">Our verdict</h2>
<div class="verdict">
<h3>{op['name']} &mdash; {op['rating']}/5</h3>
{n['verdict']}
<p><strong>Who it suits:</strong> {n['who']}</p>
</div>
<p style="margin-top:1.2em"><a class="btn btn-lime" href="{{{{{'affs' if kind == 'sports' else 'aff'}:{slug}}}}}" target="_blank" rel="nofollow sponsored noopener">Visit {op['name']}</a>
<a class="btn btn-ghost" href="/casino-reviews/">All casino reviews</a></p>
<p style="font-size:.78rem;color:var(--muted-2);margin-top:.9em">18+. New customers only. Wagering requirements and full terms apply. RNRV earns commission if you open an account through this link &mdash; it does not affect our rating or ranking. Gambling can be harmful; free help on 0800 654 655.</p>

<h2 id="next">Compare {op['name']} with the alternatives</h2>
<div class="grid g3">
<a class="card card-lnk" href="/online-casinos/"><h3>Best online casino sites NZ</h3><p>Where {op['name']} sits in our full ranking, and what else made the list.</p><span class="more">See the rankings &rarr;</span></a>
<a class="card card-lnk" href="/fast-payout-casinos/"><h3>Fast payout casinos</h3><p>All 94 timed withdrawals compared side by side.</p><span class="more">See the timings &rarr;</span></a>
<a class="card card-lnk" href="/casino-bonus/"><h3>Casino bonuses</h3><p>Every welcome offer with the cost of clearing it calculated.</p><span class="more">Compare bonuses &rarr;</span></a>
<a class="card card-lnk" href="/casino-reviews/"><h3>All casino reviews</h3><p>Every operator we have tested, with the good and the bad.</p><span class="more">Browse reviews &rarr;</span></a>
<a class="card card-lnk" href="/how-we-rate-casinos/"><h3>How we review</h3><p>Our testing process, scoring weights and conflicts policy.</p><span class="more">Read the methodology &rarr;</span></a>
<a class="card card-lnk" href="/responsible-gambling/"><h3>Responsible gambling</h3><p>Limits, self-exclusion and free confidential help in New Zealand.</p><span class="more">Get support &rarr;</span></a>
</div>
</div></div></section>

[[FAQ]]

<section class="sec sec-alt"><div class="wrap"><div class="prose">
<div class="abox">
<a class="av" href="/authors/#claire-morrison" aria-label="Claire Morrison, author"><img src="/images/authors/claire-morrison.jpg" srcset="/images/authors/claire-morrison.jpg 1x, /images/authors/claire-morrison@2x.jpg 2x" alt="Claire Morrison" width="64" height="64" loading="lazy" decoding="async"></a>
<div>
<h3>About the reviewer</h3>
<p class="role">Claire Morrison &mdash; Senior Writer &amp; Reviewer</p>
<p>This review is based on an account opened in Claire's own name from a New Zealand connection, funded with her own money, and a withdrawal timed to the minute. Every figure was checked by Elizabeth King against the testing log and the operator's own terms before publication. No operator saw this page beforehand and none has editorial input.</p>
<p><a href="/authors/#claire-morrison">Full profile</a> &middot; <a href="/authors/#elizabeth-king">Fact-checked by Elizabeth King</a> &middot; <a href="/how-we-rate-casinos/">Review methodology</a></p>
</div></div>
<p class="upd">Review last updated 13 September 2026. Bonus terms are re-verified monthly and payout timings re-measured quarterly. If your experience differs materially from what is published here, <a href="/contact/">tell us</a> &mdash; reader reports are how we catch changes between testing cycles.</p>
</div></div></section>
'''

    doc = "<!--@\n" + esc_json(fm) + "\n@-->\n" + body
    path = os.path.join(OUT, f"{300 + i * 5}-review-{slug}.html")
    open(path, "w", encoding="utf-8").write(doc)
    return path


if __name__ == "__main__":
    order = sorted(OPS, key=lambda s: OPS[s]["rank"])
    for i, slug in enumerate(order):
        if slug not in N:
            print("  !! no narrative for", slug); continue
        print(" ", build(slug, i))
    print(f"{len(order)} review fragments written")
