# Hloptech Puns

The group's puns as a little Instagram-style app: stories by topic, a shuffled feed, a searchable archive and shared likes.

## How it's built

`python3 build.py` turns `src/` into one self-contained `index.html`.

| File | What it holds |
| --- | --- |
| `src/jokes.json` | every joke: `[id, date, time, author (s/a/d), group laughs, pun, explanation]` |
| `src/emoji.json` | two hand-picked emojis per joke id (new jokes fall back to keyword rules) |
| `src/firebase-config.json` | the Firebase web config for shared likes (`{}` = likes off) |
| `src/head.html`, `src/app.html` | styles, markup and app code |
| `avatars/` | the three profile photos (embedded into the page at build time) |
| `icon-*.png`, `manifest.webmanifest` | the home-screen icon |
| `firestore.rules` | Firestore security rules for the likes |

Hosting: GitHub Pages serves `index.html` from the `main` branch, so every push goes live within a minute or two.

## One-time setup

### 1. GitHub
1. Install the GitHub command line tool: download the macOS installer from https://cli.github.com and run it.
2. In Terminal run `gh auth login` and follow the prompts (GitHub.com → HTTPS → log in with a web browser).
3. Tell Claude it's done. Claude creates the public repository `hloptech-puns`, pushes the site and turns on GitHub Pages.
   The site will be at `https://<your-username>.github.io/hloptech-puns/`.

### 2. Firebase (shared likes)
1. Go to https://console.firebase.google.com → **Add project** → name it (this one is `hloptegram`) (Google Analytics: off).
2. **Build → Authentication → Get started → Sign-in method → Anonymous → Enable.**
3. **Build → Firestore Database → Create database** → any location → start in **production mode**.
   Then open the **Rules** tab, paste the contents of `firestore.rules`, and **Publish**.
4. **Project settings (⚙️) → Your apps → Web (`</>`)** → register an app called `puns` (no hosting).
   Copy the `firebaseConfig = { ... }` object it shows and send it to Claude.
   (These values identify the project; they're meant to be public. The rules above are what protect the data.)
5. **Authentication → Settings → Authorized domains → Add domain**: `<your-username>.github.io`.

## Updating
Ask Claude for a change in this folder. It edits `src/`, runs `python3 build.py`, commits and pushes; GitHub Pages redeploys automatically.
