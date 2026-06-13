Coding assignment — a competent engineer does this correctly in about 10 minutes.
Produce ALL files in your answer: a filename header line, then the file contents.

Build a minimal URL shortener web service.

Backend — a small HTTP API in Python:
  - POST /shorten   body {"url": "..."}  -> {"code": "...", "short_url": "..."}
  - GET  /{code}    -> 302 redirect to the original URL
  - GET  /health    -> {"status": "ok", "version": "..."}
  Storage may be in-memory.

Frontend:
  - a single index.html with a form that calls POST /shorten and shows the result.

Configuration:
  - host, port, and base URL come from environment variables with sane local
    defaults; the service must run locally with zero setup.

Cloud:
  - a Dockerfile and a deploy.sh to ship it to Google Cloud Run (listen on 8080).

Quality:
  - unit tests for the endpoints, and a README with a copy-pasteable quick start.

Deliver every file needed to run, test, and deploy it.
