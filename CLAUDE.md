# CLAUDE.md

Research Brain for Alfie Rees & Lorenzo Del Monte's Applied Economics paper (Reichman, Dr. Yael Hadass): did generative AI reduce employment in AI-exposed US occupations, especially for young workers, 2020-2025?

## Layout
- `vault/` Obsidian vault. Source of truth for all content. Both authors edit it in Obsidian (Obsidian Git plugin) and push to `main`.
- `scripts/build_brain.py` Python 3 standard library only. Reads `vault/` + `data/`, injects JSON into `site/template.html` at `/*__DATA__*/null`, writes `public/index.html`.
- `site/template.html` the whole front end: vanilla JS, a hand-rolled force layout on `<canvas>`, a small Markdown renderer, three side tabs (Branches, Roadmap, Note) and a time scrubber. No build step, no npm.
- `data/deliverables.json` hand-ins (`folder`, `file`, `title`, `date`, optional `note`). `data/note-dates.json` original creation dates for notes imported from iCloud (path → date); new notes use `created:` frontmatter or git history instead.
- Deploy: Vercel project `applied-econ-research-brain` (team `alfierees-projects`), builds on push to `main` using `vercel.json`. `public/` is gitignored.

## Commands
- Build: `python3 scripts/build_brain.py`
- Preview: open `public/index.html`

## Conventions
- Vault top-level folders map to branches in `SECTIONS` in `build_brain.py`. A new top-level folder needs an entry there (label, paper role, colour).
- Timeline events come from: `01 Admin/Decisions Log.md` table rows, notes with `type: meeting` + `date`, `type: assignment` + `due`, `type: finding`, the History table in `02 Question & Scope/Research Question.md`, and `data/deliverables.json`.
- Dates parse as `YYYY-MM-DD`, `23 Nov 2026`, `Nov 2026`.
- Writing style for notes and UI copy: plain, concise, British spelling, no em dashes.
- Keep the site dependency-free and a single page; the vault must stay a normal Obsidian vault (don't rename folders without updating `SECTIONS`).
