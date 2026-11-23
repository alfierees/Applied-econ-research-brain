# Research Brain: AI and the US Labour Market

Alfie Rees & Lorenzo Del Monte · Applied Economics (Dr. Yael Hadass) · Reichman University, 2026-27

Our research paper's Obsidian vault, plus a website that draws it as a growing "brain": one branch per part of the paper, a roadmap of every decision, and a replay of how the project grew.

**Live site:** https://applied-econ-research-brain.vercel.app

## How it works

```
vault/        the Obsidian vault (all our notes)  ← you edit this
data/         deliverables.json (hand-ins) and note-dates.json (original note dates)
site/         template.html (the page design)
scripts/      build_brain.py (turns vault/ into public/index.html)
```

Every push to `main` makes Vercel run `python3 scripts/build_brain.py` and publish the result. Edit a note, push, and the site updates in about a minute.

## Setup (once each)

1. **Clone** the repo somewhere outside iCloud (iCloud can corrupt Git repos):
   ```bash
   cd ~/code
   git clone https://github.com/alfierees/applied-econ-research-brain.git
   ```
2. **Open the vault in Obsidian:** Open folder as vault → choose `applied-econ-research-brain/vault`. Trust the author when asked, so Dataview and Excalidraw load.
3. **Install Obsidian Git:** Settings → Community plugins → Browse → "Git" (by Vinzent) → Install → Enable. Then in its settings:
   - Auto pull on startup: **on**
   - Auto commit-and-sync interval: **10** minutes
   - Pull on sync before push: **on**

That's it. Obsidian now pulls the other person's changes when it opens and pushes yours every 10 minutes. To push straight away: command palette → "Git: Commit-and-sync".

## Adding things

| To add | Do this | Where it shows up |
|---|---|---|
| A paper | New note in `03 Literature/...` from the Paper template | Literature branch |
| A decision | New row at the top of `01 Admin/Decisions Log.md` (`| 23 Nov 2026 | Decision | Why | Who |`) | Roadmap tab |
| A meeting | Note in `01 Admin/Meetings/` from the Meeting template (`date:` in frontmatter) | Admin branch + Roadmap |
| A result | Note in `07 Analysis & Findings/` from the Finding template | Findings branch + Roadmap |
| A hand-in | Entry in `data/deliverables.json` | Deliverables branch + Roadmap |

- Link notes with `[[Note name]]`: every link becomes a line in the brain.
- Put `created: YYYY-MM-DD` in the frontmatter of new notes (the templates do it) so the replay knows when the note appeared.
- `status: done | in-progress | not-started | out-of-scope` gives the node a coloured ring.

**Quick fix from a browser:** on the site, open a note → "Edit on GitHub". On a branch → "+ New note in this branch".

## Run it locally

```bash
python3 scripts/build_brain.py && open public/index.html
```

No dependencies beyond Python 3.
