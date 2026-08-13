# Rancher_DS_NEW — site & tokens

Static site + design-token exports for the Rancher_DS_NEW design system preview.
Everything here is generated from the Figma variables — the site itself is styled
exclusively by `tokens/tokens.css` (try the theme switcher in the header).

## Contents
- `index.html`, `why.html`, `start.html`, `hood.html`, `faq.html` — the site (no build step)
- `tokens/tokens.css` — 116 colour tokens × 4 themes as CSS custom properties (`data-theme` on `<html>`)
- `tokens/tokens.json` — the same data for build pipelines
- `assets/` — copy `Rancher-DS-Getting-Started.pdf` and `Rancher-DS-Poster-A1.pdf` here from your Downloads before pushing (linked from start.html and faq.html)
- `.nojekyll` — tells GitHub Pages to serve files verbatim

## Publishing on GitHub Pages
1. Push this folder to a repo (root or `/docs`).
2. Settings → Pages → Deploy from a branch → pick your branch + folder.
3. The site appears at `https://<user>.github.io/<repo>/` within a minute or two.

To test privately first: push to a personal repo or fork and enable Pages there;
move to the org repo and flip its Pages source when ready. Note: one repo serves
Pages from exactly one branch at a time.

## Before you publish
- Replace `[your channel here]` in `faq.html` with the real feedback channel.
- The Figma links require viewers to have at least view access to the file.
- Delete `_shell*.py` (build leftovers the sandbox could not remove).
