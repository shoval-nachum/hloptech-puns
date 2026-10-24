# Hloptech Puns

After any change:
1. Edit `src/` (never `index.html` directly), then `python3 build.py`.
2. Republish the Claude artifact from `index.html` to https://claude.ai/artifact/TFySGHnaN8r7KyAPCmD2kB (pass it as `url`).
3. Commit and `git push` — GitHub Pages redeploys https://shoval-nachum.github.io/hloptech-puns/ automatically.

GitHub CLI lives at `tools/gh-extract/gh_2.103.0_macOS_amd64/bin/gh` (not on PATH; `tools/` is git-ignored). Git pushes over HTTPS through it.
Likes: Claude's db inside the artifact, Firebase on GitHub Pages once `src/firebase-config.json` holds the web config (see README).
New jokes go in `src/jokes.json`; give them two hand-picked emojis in `src/emoji.json`.
