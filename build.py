#!/usr/bin/env python3
"""Builds index.html (one self-contained page) from src/.

    python3 build.py

The same index.html is what GitHub Pages serves and what gets published as the Claude artifact.
"""
import base64, json, pathlib

ROOT = pathlib.Path(__file__).parent
SRC = ROOT / 'src'


def block(id_, text):
    return f'<script id="{id_}" type="application/json">{text}</script>\n'


def main():
    jokes = (SRC / 'jokes.json').read_text().strip()
    json.loads(jokes)  # fail loudly on a broken edit
    photos = {k: 'data:image/jpeg;base64,' + base64.b64encode((ROOT / 'avatars' / f'{name}.jpg').read_bytes()).decode()
              for k, name in (('s', 'shoval'), ('a', 'amiram'), ('d', 'david'))}
    emoji = json.loads((SRC / 'emoji.json').read_text())
    firebase = json.loads((SRC / 'firebase-config.json').read_text())
    page = ''.join([
        (SRC / 'head.html').read_text(),
        block('data', jokes),
        block('avatars', json.dumps(photos)),
        block('emoji', json.dumps(emoji, ensure_ascii=False, separators=(',', ':'))),
        block('firebase-config', json.dumps(firebase)),
        (SRC / 'app.html').read_text(),
    ])
    (ROOT / 'index.html').write_text(page)
    missing = [r[0] for r in json.loads(jokes) if r[0] not in emoji]
    print(f'index.html: {len(page):,} bytes, {len(json.loads(jokes))} jokes'
          + (f', {len(missing)} without hand-picked emoji' if missing else ''))


if __name__ == '__main__':
    main()
