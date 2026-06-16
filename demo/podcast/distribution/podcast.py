#!/usr/bin/env python3
"""Build the podcast distribution kit from finished episode audio.

Outputs (into ./out, gitignored — large media):
  cover.jpg            3000x3000 show art (Apple/Spotify spec)
  <slug>.mp3           tagged MP3 per episode (for Spotify-for-Creators upload, path A)
  feed.xml             valid RSS 2.0 + iTunes feed (for self-host submit to Apple, path B)

Path A (Spotify for Creators): upload the .mp3s + cover, paste the show metadata.
Path B (own RSS): host the .mp3s + cover (e.g. a GitHub release at REL_BASE),
  publish feed.xml at a public URL, submit that URL to Apple Podcasts Connect.

Set OWNER_EMAIL before submitting to Apple (left as a placeholder on purpose —
not committing a personal email to a public repo).
Requires: ffmpeg, Pillow.
"""
import os, subprocess, html
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
OWL = os.path.expanduser("~/projects/eds-rules/demo/assets/bard-owl-square.png")
ARIAL = "/System/Library/Fonts/Supplemental/Arial%s.ttf"

SHOW = dict(
    title="Ed's Rules",
    subtitle="100 Rules for Writing My Software",
    author="Ed Haynes",
    owner_email="you@example.com",   # <-- SET before Apple submission
    link="https://github.com/edhaynes/eds-rules",
    category="Technology",
    language="en-us",
    desc=("Opinionated rules for AI pair-programming, distilled from a long career — "
          "and the conversations and experiments behind them. Small local models plus "
          "good rules; an immutable axiom core plus composable preference layers. "
          "Take what works, fork what doesn't. CC-BY-4.0. github.com/edhaynes/eds-rules"),
)
REL_BASE = "https://github.com/edhaynes/eds-rules/releases/download/podcast-2026-06-16/"

# newest first; src is the finished audio/video to extract from
EPISODES = [
    dict(slug="guys-scalpel", title="Guy's Scalpel — 100 Rules Cut to a Layered Core",
         date="Mon, 16 Jun 2026 12:00:00 -0400",
         src=os.path.expanduser("~/projects/eds-rules/demo/podcast/ep94-edit/work/ep94-final.mp4"),
         desc="After the conversation with Guy Turgeon, the 100 rules get cut into a layered structure: a small immutable axiom core plus composable preference layers. Watch: https://youtu.be/UJvVmNy0gTM"),
    dict(slug="guy-turgeon-interview", title="In Conversation with Guy Turgeon",
         date="Sun, 15 Jun 2026 12:00:00 -0400",
         src=os.path.expanduser("~/projects/eds-rules/demo/podcast/ep93-interview/work/ep93-final.mp4"),
         desc="Ed sits down with Guy Turgeon (chief architect, Red Hat Telco) to grade the rule set — the 90% rule, API-first, attack surface, UBI, and a career in embedded software. Watch: https://youtu.be/uy7-QJ-QoOo"),
    dict(slug="hooks-before-first-commit", title="Hooks Before the First Commit, and the Architect Who Thinks Slow",
         date="Sat, 14 Jun 2026 12:00:00 -0400",
         src=os.path.expanduser("~/projects/eds-rules/demo/podcast/ep94.wav"),
         desc="The rule-quality series: the best secret-hygiene rule against a low-scoring one. Same list, different grades."),
    dict(slug="zero-hardcoded-final-word", title="Zero Hardcoded Anything, and Who Gets the Final Word",
         date="Sat, 14 Jun 2026 11:00:00 -0400",
         src=os.path.expanduser("~/projects/eds-rules/demo/podcast/ep93.wav"),
         desc="The rule-quality series: zero hardcoded values against the team's governance rule."),
    dict(slug="secret-you-cant-take-back", title="The Secret You Can't Take Back, and the Rule That's All Me",
         date="Sat, 14 Jun 2026 10:00:00 -0400",
         src=os.path.expanduser("~/projects/eds-rules/demo/podcast/ep92.wav"),
         desc="The rule-quality series: never hardcode a secret against a persona-specific rule."),
]

e = html.escape


def font(sz, bold=True):
    p = ARIAL % (" Bold" if bold else "")
    return ImageFont.truetype(p, sz) if os.path.exists(p) else ImageFont.load_default()


def cover():
    W = 3000
    img = Image.new("RGB", (W, W), (16, 16, 16))
    d = ImageDraw.Draw(img)
    if os.path.exists(OWL):
        owl = Image.open(OWL).convert("RGBA").resize((1500, 1500))
        img.paste(owl, ((W - 1500) // 2, 360), owl)
    def ctr(y, t, f, fill):
        w = d.textlength(t, font=f); d.text(((W - w) / 2, y), t, font=f, fill=fill)
    ctr(2030, "ED'S RULES", font(280), (255, 255, 255))
    ctr(2370, SHOW["subtitle"], font(110, False), (191, 191, 191))
    d.rectangle([0, W - 40, W, W], fill=(238, 0, 0))
    p = os.path.join(OUT, "cover.jpg")
    img.save(p, quality=88)
    print("wrote", p, os.path.getsize(p) // 1024, "KB")


def duration(path):
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries",
        "format=duration", "-of", "default=nokey=1:noprint_wrappers=1", path]).strip())


def hhmmss(s):
    s = int(s); return f"{s//3600:02d}:{s%3600//60:02d}:{s%60:02d}"


def mp3s():
    for ep in EPISODES:
        outp = os.path.join(OUT, ep["slug"] + ".mp3")
        subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
            "-i", ep["src"], "-vn", "-c:a", "libmp3lame", "-b:a", "128k", "-ar", "44100", "-ac", "2",
            "-metadata", f"title={ep['title']}", "-metadata", f"artist={SHOW['author']}",
            "-metadata", f"album={SHOW['title']}", "-metadata", "genre=Podcast", outp], check=True)
        ep["dur"] = duration(outp)
        ep["bytes"] = os.path.getsize(outp)
        print(f"  {ep['slug']}.mp3  {hhmmss(ep['dur'])}  {ep['bytes']//1024//1024}MB")


def feed():
    items = []
    for ep in EPISODES:
        url = REL_BASE + ep["slug"] + ".mp3"
        items.append(f"""    <item>
      <title>{e(ep['title'])}</title>
      <description>{e(ep['desc'])}</description>
      <pubDate>{ep['date']}</pubDate>
      <enclosure url="{url}" length="{ep.get('bytes',0)}" type="audio/mpeg"/>
      <guid isPermaLink="false">edsrules-{ep['slug']}</guid>
      <itunes:duration>{hhmmss(ep.get('dur',0))}</itunes:duration>
      <itunes:explicit>false</itunes:explicit>
    </item>""")
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd" xmlns:content="http://purl.org/rss/1.0/modules/content/">
  <channel>
    <title>{e(SHOW['title'])}</title>
    <link>{e(SHOW['link'])}</link>
    <language>{SHOW['language']}</language>
    <description>{e(SHOW['desc'])}</description>
    <itunes:author>{e(SHOW['author'])}</itunes:author>
    <itunes:subtitle>{e(SHOW['subtitle'])}</itunes:subtitle>
    <itunes:summary>{e(SHOW['desc'])}</itunes:summary>
    <itunes:type>episodic</itunes:type>
    <itunes:explicit>false</itunes:explicit>
    <itunes:image href="{REL_BASE}cover.jpg"/>
    <itunes:category text="{SHOW['category']}"/>
    <itunes:owner>
      <itunes:name>{e(SHOW['author'])}</itunes:name>
      <itunes:email>{SHOW['owner_email']}</itunes:email>
    </itunes:owner>
{chr(10).join(items)}
  </channel>
</rss>
"""
    p = os.path.join(OUT, "feed.xml")
    open(p, "w").write(xml)
    print("wrote", p)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    cover()
    mp3s()
    feed()
    print("done — kit in", OUT)
