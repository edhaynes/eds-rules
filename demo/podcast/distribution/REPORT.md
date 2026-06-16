# Report — work done while you were out (2026-06-16)

Two threads: **(1) get the podcast onto Apple (path A)** and **(2) Linda's paid-promotion
list**. Both are ready for you below. Nothing irreversible was published while you were gone.

---

## 1. Podcast distribution — kit is built, one step left (your login)

You picked **path A (Spotify for Creators)** — free, hosts the audio, auto-distributes to
**Apple Podcasts + Spotify**. Its only step I can't do is the account/login. Everything it
needs is built and sitting in `demo/podcast/distribution/out/` (regenerate any time with
`python3 demo/podcast/distribution/podcast.py`):

- **`cover.jpg`** — 3000×3000 owl show art (Apple/Spotify spec, 297 KB).
- **5 tagged MP3s:**
  | File | Episode | Length |
  |---|---|---|
  | `guys-scalpel.mp3` | Guy's Scalpel — 100 Rules Cut to a Layered Core | 6:41 |
  | `guy-turgeon-interview.mp3` | In Conversation with Guy Turgeon | 30:38 |
  | `hooks-before-first-commit.mp3` | Hooks Before the First Commit (narrated) | 1:46 |
  | `zero-hardcoded-final-word.mp3` | Zero Hardcoded Anything (narrated) | 2:00 |
  | `secret-you-cant-take-back.mp3` | The Secret You Can't Take Back (narrated) | 1:52 |
- **Show metadata** to paste in:
  - Title: **Ed's Rules** · Subtitle: *100 Rules for Writing My Software*
  - Author: **Ed Haynes** · Category: **Technology** · Language: en-us · Explicit: No
  - Description: *Opinionated rules for AI pair-programming, distilled from a long career —
    and the conversations and experiments behind them. Small local models plus good rules;
    an immutable axiom core plus composable preference layers. Take what works, fork what
    doesn't. CC-BY-4.0. github.com/edhaynes/eds-rules*

### To finish path A (~15 min, your login)
1. Sign in at **podcasters.spotify.com** (Spotify for Creators).
2. New show → paste the metadata + upload `cover.jpg`.
3. Upload the 5 MP3s as episodes (titles/descriptions above; the generator's
   `EPISODES` list has the per-episode blurbs).
4. Enable **Apple Podcasts** distribution in settings → it submits the feed for you.

### Curation note
I included all five finished audio pieces. The two YouTube episodes (interview + talk)
are the substantial ones; the three ~2-min narrated pieces are the "best-vs-worst" recap
series. Drop any you don't want — just don't upload them.

### Path B is also one command away (if you'd rather own the feed)
I built a valid `feed.xml` (RSS 2.0 + iTunes) but did **not** publish it (that's a new
public channel + your choice was A). To switch to self-hosting later:
1. Set `OWNER_EMAIL` in `podcast.py` (left as a placeholder — I won't commit your email to a public repo).
2. `gh release create podcast-2026-06-16 out/*.mp3 out/cover.jpg` (hosts the media at the URL `feed.xml` already points to).
3. Commit/serve `feed.xml` and submit its URL at **Apple Podcasts Connect** (free).

---

## 2. Linda's paid-promotion list (academic + open-source)

Full brief: **`promotion/LINDA-paid-venues.md`** (every cost cited + dated; gated ones flagged).
Headline: almost nobody publishes a rate card — the few that do are the low-friction path.

**Best value (her shortlist):**
1. **Sponsor an AI-tooling OSS project's README via Open Collective (~$500/mo)** — most on-ethos, logo where devs read.
2. **Practical AI podcast — $1,200/episode** — cleanest buy that hits the "small local LLM + good rules" thesis.
3. **AlphaSignal secondary slot — $3,000** — only research-literate newsletter with public pricing; home for the scaling-law angle.
4. **ICLR Sci-Journal-Publisher tier ($1,500)** or **ASE Sunshine (€2,000)** — cheapest credible in-person research placement.
5. **Cooper Press classified ($180–250)** — low-risk transparent OSS-dev test.

**Free/earned (do regardless of budget):** pitch **Import AI**, **Ahead of AI**, **Davis
Summarizes Papers** as coverage (they don't sell ads but are the best-fit research
audiences), and submit to **Hugging Face Daily Papers**. Draft pitches in
`promotion/outreach-drafts.md`.

Every paid buy needs your accounts/budget, so I prepared but did not purchase anything.

---

## 3. Everything else — current status (all live / pushed)

- **Ep 94** public: https://youtu.be/UJvVmNy0gTM (owl splash + explainer cards)
- **Ep 93** public: https://youtu.be/uy7-QJ-QoOo (Guy interview)
- **Synopsis PDF** (GitHub release): https://github.com/edhaynes/eds-rules/releases/download/rules-synopsis-2026-06-16/eds-rules-synopsis.pdf
- **Layered taxonomy** on branch `rules-taxonomy` (not merged — your call). `main`'s README still shows the flat 100; merge or stand up a Pages site when you want a clean promo link.

---

## 4. Flagged for your call
- **"A" interpretation:** I read "A" as the podcast path A (Spotify), the last A/B choice you saw. If you meant Linda's *section A* or something else, redirect me.
- **Podcast episode set** — curate the five (above).
- **Promotion spend** — none made; pick from the shortlist and I'll execute what doesn't need your card, draft what does.
- **Owner email** for the RSS feed — placeholder until you set it.

— Jason-eds
