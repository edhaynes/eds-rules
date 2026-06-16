#!/usr/bin/env python3
"""Upload an assembled "Ed's 100 Rules" episode to YouTube — private by default,
or scheduled to auto-publish at a given local time (the 3pm cadence).

Auth: youtube-token.json (from get_youtube_token.py) — it embeds the client_id/
secret + refresh token, so this refreshes silently.

Usage:
  python3 publish-episode.py --ep 92                 # upload PRIVATE (safe; review on YT)
  python3 publish-episode.py --ep 92 --at 15:00      # schedule today/next 15:00 local
  python3 publish-episode.py --ep 92 --video podcast/ep92.mp4 --thumb ...

Metadata (title / good-vs-bad description / tags) is read from podcast/ep<N>.md.
Requires: google-api-python-client, google-auth (already installed).
"""
import argparse
import datetime
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TOKEN = os.path.join(HERE, "youtube-token.json")
THUMBS = os.path.expanduser("~/projects/bard-marketing/thumbnails")
SCOPES = ["https://www.googleapis.com/auth/youtube.upload",
          "https://www.googleapis.com/auth/youtube"]
CATEGORY_TECH = "28"  # Science & Technology


def creds():
    from google.oauth2.credentials import Credentials
    from google.auth.transport.requests import Request
    if not os.path.exists(TOKEN):
        sys.exit(f"No {TOKEN}. Run get_youtube_token.py first.")
    c = Credentials.from_authorized_user_file(TOKEN, SCOPES)
    if not c.valid:
        c.refresh(Request())
    return c


def metadata(ep):
    md = os.path.join(HERE, "podcast", f"ep{ep}.md")
    title_line = good = bad = ""
    for line in open(md, encoding="utf-8"):
        if line.startswith("# Episode") and not title_line:
            title_line = line.split("—", 1)[-1].strip().strip('"')
        if line.startswith("- GOOD:"):
            good = line.split(":", 1)[1].strip()
        if line.startswith("- BAD:"):
            bad = line.split(":", 1)[1].strip()
    title = f"Ed's 100 Rules · Ep {ep} — {title_line}"[:100]
    desc = (
        f"Episode {ep} of Ed's 100 Rules — the rule-quality series. Each episode "
        f"pairs the best-scoring rule with the worst, graded on a real rubric.\n\n"
        f"GOOD — {good}\nBAD  — {bad}\n\n"
        f"100 Rules for Programming my Software (the Red Hat way). "
        f"github.com/edhaynes/eds-rules"
    )
    tags = ["software engineering", "AI coding", "coding rules", "Red Hat",
            "Ed's 100 Rules", f"episode {ep}"]
    return title, desc, tags


def next_local(hhmm):
    """Next future datetime at HH:MM local, as RFC3339 UTC."""
    h, m = map(int, hhmm.split(":"))
    now = datetime.datetime.now().astimezone()
    target = now.replace(hour=h, minute=m, second=0, microsecond=0)
    if target <= now:
        target += datetime.timedelta(days=1)
    return target.astimezone(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main():
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaFileUpload

    ap = argparse.ArgumentParser()
    ap.add_argument("--ep", required=True)
    ap.add_argument("--video")
    ap.add_argument("--thumb")
    ap.add_argument("--at", help="local HH:MM to auto-publish; omit = stay private")
    ap.add_argument("--public", action="store_true", help="publish public immediately")
    ap.add_argument("--title", help="override title (e.g. interview episodes)")
    ap.add_argument("--description", help="override description")
    ap.add_argument("--tags", help="override tags, comma-separated")
    a = ap.parse_args()
    video = a.video or os.path.join(HERE, "podcast", f"ep{a.ep}.mp4")
    if not os.path.exists(video):
        sys.exit(f"No video at {video}")
    thumb = a.thumb or os.path.join(THUMBS, f"ep{a.ep}.png")
    title, desc, tags = metadata(a.ep)
    if a.title:
        title = a.title[:100]
    if a.description:
        desc = a.description
    if a.tags:
        tags = [t.strip() for t in a.tags.split(",") if t.strip()]

    status = {"privacyStatus": "private", "selfDeclaredMadeForKids": False}
    if a.at:
        status["publishAt"] = next_local(a.at)  # private until then, auto-public at publishAt
    elif a.public:
        status["privacyStatus"] = "public"

    yt = build("youtube", "v3", credentials=creds())
    print(f"Uploading: {title}")
    req = yt.videos().insert(
        part="snippet,status",
        body={"snippet": {"title": title, "description": desc, "tags": tags,
                          "categoryId": CATEGORY_TECH},
              "status": status},
        media_body=MediaFileUpload(video, chunksize=-1, resumable=True))
    resp = None
    while resp is None:
        _, resp = req.next_chunk()
    vid = resp["id"]
    print(f"  video id: {vid}  ->  https://youtu.be/{vid}")

    if os.path.exists(thumb):
        yt.thumbnails().set(videoId=vid, media_body=MediaFileUpload(thumb)).execute()
        print(f"  thumbnail set: {os.path.basename(thumb)}")
    else:
        print(f"  (no thumbnail at {thumb} — skipped)")

    if a.at:
        print(f"  scheduled to auto-publish at {status['publishAt']} (UTC)")
    elif a.public:
        print("  status: PUBLIC (live now)")
    else:
        print("  status: PRIVATE (review on YouTube, then schedule or publish)")


if __name__ == "__main__":
    main()
