#!/usr/bin/env python3
"""One-time YouTube OAuth bootstrap for the publishing pipeline (F18).

Runs the installed-app OAuth flow against your channel: opens a browser, you
click "Allow", and it saves a refresh token to demo/youtube-token.json (gitignored).
publish-episode.py then uses that token to upload + schedule with no further
prompts. Run this ONCE (re-run only if you revoke access or the token is lost).

Prereqs:
  1. pip install google-auth-oauthlib google-api-python-client
     (Google's official libs — Apache-2.0, pure-Python, ARM-fine.)
  2. In Google Cloud Console (console.cloud.google.com):
       - New project (or pick one).
       - APIs & Services → Library → enable "YouTube Data API v3".
       - APIs & Services → OAuth consent screen → External → add yourself as a
         Test user (so it works before app verification).
       - Credentials → Create Credentials → OAuth client ID → type "Desktop app".
       - Download the JSON, save it as demo/client_secret.json.
  3. Run:  python3 demo/get_youtube_token.py

Secrets: client_secret.json and youtube-token.json are gitignored — never commit them.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CLIENT_SECRET = os.path.join(HERE, "client_secret.json")
TOKEN = os.path.join(HERE, "youtube-token.json")
SCOPES = [
    "https://www.googleapis.com/auth/youtube.upload",  # videos.insert
    "https://www.googleapis.com/auth/youtube",          # thumbnails.set, scheduling
]


def main():
    try:
        from google_auth_oauthlib.flow import InstalledAppFlow
    except ImportError:
        sys.exit("Missing deps. Run:\n"
                 "  pip install google-auth-oauthlib google-api-python-client")
    if not os.path.exists(CLIENT_SECRET):
        sys.exit(f"Missing {CLIENT_SECRET}.\n"
                 "Create an OAuth 'Desktop app' client in Google Cloud Console "
                 "(YouTube Data API v3 enabled) and save the JSON there. "
                 "See this file's header for the full steps.")

    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET, SCOPES)
    creds = flow.run_local_server(port=0)  # opens the browser; you click Allow

    with open(TOKEN, "w") as f:
        f.write(creds.to_json())
    print(f"\nAuthorized. Refresh token saved to {TOKEN}")
    print("You won't need to do this again. publish-episode.py can now upload + schedule.")


if __name__ == "__main__":
    main()
