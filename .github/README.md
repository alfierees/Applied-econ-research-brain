# Research Brain: AI and the US Labour Market

Alfie Rees & Lorenzo Del Monte · Applied Economics (Dr. Yael Hadass) · Reichman University, 2026-27

This repo **is** our Obsidian vault. A small build script turns it into a website that draws the vault as a growing "brain": one branch per part of the paper, a roadmap of every decision, and a replay of how the project grew.

**Live site:** https://applied-econ-research-brain.vercel.app

## How it works

```
00 Home.md, 01 Admin/ … 09 Visuals/   our notes (what you see in Obsidian)
.brain/      build_brain.py, template.html, deliverables.json, note-dates.json
vercel.json  tells Vercel to run .brain/build_brain.py and publish public/
```

Every push to `main` makes Vercel rebuild the site. Edit a note, sync, and the site updates in about a minute. Folders starting with a dot are hidden in Obsidian, so the vault looks like a normal vault.

## Setup for Lorenzo (once)

1. Clone it somewhere outside iCloud:
   ```bash
   git clone https://github.com/alfierees/applied-econ-research-brain.git
   ```
2. Obsidian → Open folder as vault → pick the cloned folder. Trust the author so Dataview and Excalidraw load.
3. Settings → Community plugins → Browse → **Git** (by Vinzent) → Install → Enable. In its settings:
   - Auto pull on startup: **on**
   - Auto commit-and-sync interval: **10** minutes
   - Pull on sync before push: **on**

Obsidian now pulls the other person's changes when it opens and pushes yours every 10 minutes. To sync straight away: command palette → "Git: Commit-and-sync".

## Adding things

| To add | Do this | Where it shows up |
|---|---|---|
| A paper | New note in `03 Literature/...` from the Paper template | Literature branch |
| A decision | New row at the top of `01 Admin/Decisions Log.md` | Roadmap tab |
| A meeting | Note in `01 Admin/Meetings/` from the Meeting template | Admin branch + Roadmap |
| A result | Note in `07 Analysis & Findings/` from the Finding template | Findings branch + Roadmap |
| A hand-in | Entry in `.brain/deliverables.json` | Deliverables branch + Roadmap |

- Link notes with `[[Note name]]`: every link becomes a line in the brain.
- New notes get `created:` from the templates, so the replay knows when they appeared.
- `status: done | in-progress | not-started | out-of-scope` gives a node a coloured ring.

**From a browser:** on the site, open a note → "Edit on GitHub", or open a branch → "+ New note in this branch".

## Run it locally

```bash
python3 .brain/build_brain.py && open public/index.html
```
