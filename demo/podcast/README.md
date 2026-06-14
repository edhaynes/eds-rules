# Ed's 100 Rules — podcast episodes 92–101

Ten episode scripts for the "best rule × worst rule" series format (see
`../SERIES_episode-map.md`). Each pairs a top-scoring rule with a bottom-scoring
one (scores from `quality/grades.csv`); the contrast is the hook.

Audio is generated **locally and privately** — the voicelab VibeVoice clone of
Eddie's voice (reference `voicelab/reference/eddie-wagontrail3-clean.wav`, 20
diffusion steps). No cloud, no third party; `.wav` files stay out of the repo
(gitignored — large, regenerable from the scripts).

| Ep | Good rule (score) | Bad rule (score) |
|----|---|---|
| 92 | #2 Never hardcode a secret (82.0) | #18 Linda searches wide (30.0) |
| 93 | #20 Zero hardcoded values (74.0) | #13 Five roles, human is final (33.5) |
| 94 | #51 Hooks before first commit (73.5) | #14 Claudius plans deep (37.5) |
| 95 | #9 Fail fast (72.5) | #42 Both arches, flag no-ARM (39.5) |
| 96 | #3 Distrust every external input (72.0) | #83 Structured logs past a script (40.0) |
| 97 | #4 Destruction needs a human (71.5) | #90 Cleanup sweep after release (41.5) |
| 98 | #59 Gitignore keys from day one (71.0) | #95 Plans carry a live Status (42.5) |
| 99 | #84 Pin it and lock it (67.5) | #33 One non-trivial class per file (42.5) |
| 100 | #22 Validate config at startup (66.5) | #15 Jason sprints sized for 90% (43.5) |
| 101 | #46 Pre-deploy gates never off (66.5) | #96 ADRs are immutable (44.0) |

Thumbnails: `bard-marketing/tools/episode_thumbnail.py` (brand palette + owl).

## Regenerate audio
```
for n in 92 93 94 95 96 97 98 99 100 101; do
  cd ~/projects/voicelab && COMFY_DIR="$PWD/comfyui" comfyui/.venv/bin/python \
    scripts/narrate.py --voice reference/eddie-wagontrail3-clean.wav \
    --text-file /tmp/ep${n}-spoken.txt --out ~/projects/eds-rules/demo/podcast/ep${n}.wav
done
```
