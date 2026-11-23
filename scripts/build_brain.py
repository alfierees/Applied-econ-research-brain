#!/usr/bin/env python3
"""Build the Research Brain site from the Obsidian vault.

    python3 scripts/build_brain.py

Reads vault/ and data/, writes public/index.html. Vercel runs this on every
push to main, so editing a note and pushing is all it takes to update the site.
"""
import datetime
import json
import os
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VAULT = ROOT / "vault"
DATA_DIR = ROOT / "data"
TEMPLATE = ROOT / "site" / "template.html"
OUT_DIR = ROOT / "public"

REPO = "{}/{}".format(
    os.environ.get("VERCEL_GIT_REPO_OWNER", "alfierees"),
    os.environ.get("VERCEL_GIT_REPO_SLUG", "applied-econ-research-brain"),
)
BRANCH = os.environ.get("VERCEL_GIT_COMMIT_REF", "main")

SKIP_DIRS = {".obsidian", "Templates", ".trash"}

# Vault folder -> (branch label, the part of the paper it feeds, colour)
SECTIONS = {
    "01 Admin":                 ("Admin",        "Deadlines, meetings, decisions", "#9aa5b1"),
    "02 Question & Scope":      ("Question",     "Title and Introduction",         "#f2b84b"),
    "03 Literature":            ("Literature",   "Section 2: Literature survey",   "#6fa8ff"),
    "04 Sectors & Occupations": ("Occupations",  "Treatment and control groups",   "#c792ea"),
    "05 Data":                  ("Data",         "Section 3: Data",                "#4fd1c5"),
    "06 Methodology":           ("Methodology",  "Section 3: Methodology",         "#ff8a65"),
    "07 Analysis & Findings":   ("Findings",     "Results",                        "#7ee081"),
    "08 Writing":               ("Writing",      "Drafts and outline",             "#f78fb3"),
    "09 Visuals":               ("Visuals",      "Roadmap and progress tree",      "#b0bec5"),
    "Deliverables":             ("Deliverables", "What we handed in",              "#ffd166"),
}

WIKI = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")
TODAY = datetime.date.today().isoformat()


def load_json(name, default):
    p = DATA_DIR / name
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else default


def parse_frontmatter(text):
    fm = {}
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            for line in text[3:end].splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    fm[k.strip()] = v.strip().strip('"')
            text = text[end + 4:].lstrip("\n")
    return fm, text


def parse_date(s):
    s = (s or "").strip().replace("*", "").replace("~", "")
    s = re.sub(r",.*$", "", s)  # "10 Nov 2026, 13:00" -> "10 Nov 2026"
    for fmt in ("%Y-%m-%d", "%d %b %Y", "%d %B %Y", "%b %Y", "%B %Y"):
        try:
            return datetime.datetime.strptime(s, fmt).date().isoformat()
        except ValueError:
            pass
    return None


def git_dates(rel):
    """(first, last) commit dates for a vault file, or (None, None) without git history."""
    try:
        out = subprocess.run(
            ["git", "log", "--follow", "--format=%as", "--", str(Path("vault") / rel)],
            cwd=ROOT, capture_output=True, text=True, timeout=10,
        ).stdout.split()
        return (out[-1], out[0]) if out else (None, None)
    except Exception:
        return (None, None)


def table_rows(body):
    for line in body.splitlines():
        line = line.strip()
        if line.startswith("|") and not re.match(r"^\|[\s:\-|]+\|$", line):
            yield [c.strip() for c in line.strip("|").split("|")]


def main():
    note_dates = load_json("note-dates.json", {})
    deliverables = load_json("deliverables.json", [])
    nodes, links, events = [], [], []
    by_name = {}

    nodes.append({"id": "root", "kind": "root", "title": "AI and the US Labour Market", "section": None, "body": ""})
    for folder, (label, role, colour) in SECTIONS.items():
        nodes.append({"id": "hub:" + folder, "kind": "hub", "title": label, "role": role,
                      "section": folder, "colour": colour, "body": ""})
        links.append({"source": "root", "target": "hub:" + folder, "kind": "branch"})

    for p in sorted(VAULT.rglob("*.md")):
        rel = p.relative_to(VAULT)
        if any(part in SKIP_DIRS for part in rel.parts) or p.name.endswith(".excalidraw.md"):
            continue
        fm, body = parse_frontmatter(p.read_text(encoding="utf-8"))
        top = rel.parts[0] if len(rel.parts) > 1 else None
        name = p.stem
        nid = "note:" + str(rel)
        g_first, g_last = git_dates(rel)
        date = (parse_date(fm.get("created")) or parse_date(fm.get("date"))
                or note_dates.get(str(rel)) or g_first or TODAY)
        node = {
            "id": nid, "kind": "note", "title": name, "path": str(rel),
            "section": top if top in SECTIONS else None,
            "sub": rel.parts[1] if len(rel.parts) > 2 else None,
            "type": fm.get("type"), "status": fm.get("status"),
            "date": date, "updated": g_last or note_dates.get(str(rel)) or date,
            "body": body,
        }
        nodes.append(node)
        by_name[name.lower()] = nid
        parent = "hub:" + node["section"] if node["section"] else "root"
        links.append({"source": parent, "target": nid, "kind": "branch"})

        if fm.get("type") == "meeting" and fm.get("date"):
            events.append({"date": parse_date(fm["date"]), "kind": "Meeting", "text": name, "node": nid})
        if fm.get("type") == "assignment" and fm.get("due"):
            events.append({"date": parse_date(fm["due"]), "kind": "Deliverable",
                           "text": f"{name} ({fm.get('status', '')})", "node": nid})
        if fm.get("type") == "finding":
            events.append({"date": date, "kind": "Finding", "text": name, "node": nid})
        if name == "Decisions Log":
            for cells in table_rows(body):
                if len(cells) >= 2 and parse_date(cells[0]):
                    events.append({"date": parse_date(cells[0]), "kind": "Decision",
                                   "text": cells[1].replace("**", ""),
                                   "why": cells[2] if len(cells) > 2 else "", "node": nid})
        if name == "Research Question":
            for cells in table_rows(body):
                if len(cells) == 2 and parse_date(cells[0]):
                    events.append({"date": parse_date(cells[0]), "kind": "Question", "text": cells[1], "node": nid})

    for d in deliverables:
        nid = "file:" + d["folder"] + "/" + d["file"]
        nodes.append({"id": nid, "kind": "file", "title": d["title"], "path": d["folder"] + "/" + d["file"],
                      "section": "Deliverables", "date": d["date"], "updated": d["date"],
                      "body": f"**{d['folder'].replace('_', ' ')}** file: `{d['file']}`\n\nSaved {d['date']}."
                              + (f"\n\n{d['note']}" if d.get("note") else "")})
        links.append({"source": "hub:Deliverables", "target": nid, "kind": "branch"})
        events.append({"date": d["date"], "kind": "Deliverable", "text": d["title"], "node": nid})

    seen = set()
    for n in nodes:
        if n["kind"] != "note":
            continue
        out = []
        for m in WIKI.finditer(n["body"]):
            target = m.group(1).strip()
            if target.endswith(".excalidraw"):
                target = target[: -len(".excalidraw")]
            tid = by_name.get(target.lower())
            if tid and tid != n["id"]:
                out.append(tid)
                key = tuple(sorted((n["id"], tid)))
                if key not in seen:
                    seen.add(key)
                    links.append({"source": n["id"], "target": tid, "kind": "wiki"})
        n["out"] = sorted(set(out))

    events = sorted((e for e in events if e["date"]), key=lambda e: e["date"])
    data = {
        "built": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        "repo": REPO, "branch": BRANCH,
        "sections": {k: {"label": v[0], "role": v[1], "colour": v[2]} for k, v in SECTIONS.items()},
        "nodes": nodes, "links": links, "events": events,
    }
    blob = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    OUT_DIR.mkdir(exist_ok=True)
    (OUT_DIR / "index.html").write_text(TEMPLATE.read_text(encoding="utf-8").replace("/*__DATA__*/null", blob), encoding="utf-8")
    print(f"Built public/index.html: {sum(1 for n in nodes if n['kind'] in ('note', 'file'))} notes/files, "
          f"{len(links)} links, {len(events)} timeline events")


if __name__ == "__main__":
    main()
