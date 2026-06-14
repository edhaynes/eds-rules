# Episode (story) — "The systems guy who never built a screen"
Author: Jason-eds · Draft 1 (SKELETON — has [FILL] gaps only Eddie can supply) · ~3.5 min

Delivery: Eddie, first person. Blank lines = card cuts. `[CARD: …]` = production cue.
A story episode (Ep90-style narrative), not a rule pairing. Placement TBD — likely the
first **guest slot** if Jose comes on the mic, otherwise a solo story between rule blocks.

---

## 0:00 — The one thing I never did
[CARD: "C · IPv6 · RTOS · …  GUI?"]

Forty-seven years of code. I wrote a TCP/IP stack inside a network encryptor. I built a
certified IPv6 stack. Real-time operating systems, where a late millisecond is a bug.
Systems, memory, determinism — that's my whole life.

And in all that time there's one thing I never once built: a screen. A real user
interface. Backends, protocols, architecture — yes. A button a human clicks? Never.

## 0:40 — Ghostwriter, and the wall
[CARD: "Ghostwriter — the frontend"]

So I'm building Ghostwriter — a tool for writers, people whose tools are Word and a
notebook. Which means the *interface* is the whole product. And the frontend was
[FILL: what was the frontend before? plain HTML/JS? Streamlit? Gradio? hand-rolled
something? — one or two sentences on what it was and why it was fighting you].

[FILL: the specific frustration — what couldn't you make it do, or what made it feel
wrong, that told you the stack was the problem and not you?]

## 1:30 — Claude taught me GUIs
[CARD: "I didn't learn React. I learned to ask."]

Here's what changed first. I didn't go take a frontend course. Claude taught me GUIs the
way a patient senior dev teaches a backend guy — [FILL: how did it actually go? Did Claude
explain components in systems terms? Show you a working page you could modify? Walk you
through layout/state as if they were data structures? Give the 1-2 moments that made it
click for you].

For a systems person it reframed the whole thing: a UI is just state and events — a state
machine with a face. Once it was *that*, I could reason about it. [FILL: keep/cut this line
depending on whether that's actually how it clicked for you.]

## 2:20 — Jose Mayora's prompt
[CARD: "the one-line prompt that flipped the stack"]

Then [FILL: who is Jose Mayora to you — colleague? friend? someone online?] handed me one
simple prompt. Not a tutorial, not a repo — a prompt.

[CARD: the prompt itself, on screen]

[FILL: the literal prompt, or the gist of it — this is the heart of the episode. What did
it say? Why did that specific framing work when everything before hadn't?]

And that was it. [FILL: what happened — did it scaffold a whole Vite + React app in one
shot? convert the old thing? give you the mental model you'd been missing?] Suddenly I was
on Vite and React, and it felt right instead of like a fight.

## 3:00 — The lesson
[CARD: "the right prompt opens a door you thought was locked"]

[FILL — pick the one you mean:]
- A whole domain I'd written off as "not me" turned out to be one good prompt away.
- The stack was never the hard part; asking the right question was.
- The right collaborator — human or AI — doesn't do it for you, they hand you the key.

Forty-seven years in, and I shipped my first real interface. Not because I finally learned
frontend — because I finally learned how to ask.

---

### What I need from you to finish this (the [FILL] gaps)
1. **Jose's prompt** — literal text or close gist. The episode lives or dies on this.
2. **The before-state** — what Ghostwriter's frontend was before Vite+React, and the
   specific frustration.
3. **How Claude taught you GUIs** — 1-3 concrete moments (not "it helped" — what it did).
4. **Who Jose Mayora is** + guest episode (he's on the mic) or you narrating solo.
5. **The lesson line** you want (pick one above or give your own).

### Notes
- No invented biography: bio facts (TACLANE, IPv6, RTOS, "tool for writers") are from the
  rules canon; everything in [FILL] is left blank until you supply it.
- If guest format: add a short Jose intro card + 2-3 interview beats and I'll restructure.
