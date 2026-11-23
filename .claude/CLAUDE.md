# CLAUDE.md

Research Brain for Alfie Rees & Lorenzo Del Monte's Applied Economics paper (Reichman, Dr. Yael Hadass): did generative AI reduce employment in AI-exposed US occupations, especially for young workers, 2020-2025?

## Layout
- The repo root **is** the Obsidian vault (`00 Home.md`, `01 Admin/` … `09 Visuals/`, `Templates/`, `.obsidian/`). Both authors edit it in Obsidian with the Obsidian Git plugin and push to `main`. Alfie's copy lives in iCloud with its git directory in `.git.nosync` (a `.git` file points to it) so iCloud doesn't sync git internals.
- `.brain/build_brain.py` Python 3 standard library only. Reads the notes + `.brain/*.json`, injects JSON into `.brain/template.html` at `/*__DATA__*/null`, writes `public/index.html`.
- `.brain/template.html` the whole front end: vanilla JS, a hand-rolled force layout on `<canvas>`, a small Markdown renderer, three side tabs (Branches, Roadmap, Note) and a time scrubber. No npm.
- `.brain/deliverables.json` hand-ins (`folder`, `file`, `title`, `date`, optional `note`). `.brain/note-dates.json` original creation dates for notes that predate the repo; new notes use `created:` frontmatter or git history.
- Dot-folders are hidden in Obsidian; keep tooling in them so the vault stays clean. README lives in `.github/README.md`.
- Deploy: Vercel project `applied-econ-research-brain` (team `alfierees-projects`), builds on push to `main` via `vercel.json`. `public/` is gitignored.

## Commands
- Build: `python3 .brain/build_brain.py`
- Preview: open `public/index.html`

## Conventions
- Top-level note folders map to branches in `SECTIONS` in `build_brain.py`. A new top-level folder needs an entry there (label, paper role, colour).
- Timeline events come from: `01 Admin/Decisions Log.md` table rows, notes with `type: meeting` + `date`, `type: assignment` + `due`, `type: finding`, the History table in `02 Question & Scope/Research Question.md`, and `.brain/deliverables.json`.
- Dates parse as `YYYY-MM-DD`, `23 Nov 2026`, `Nov 2026`.
- Writing style for notes and UI copy: plain, concise, British spelling, no em dashes.
- Keep the site dependency-free and a single page; never add non-note files at the vault's top level except `vercel.json` and `.gitignore`.
