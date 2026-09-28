#!/usr/bin/env python3
"""Checks the templates and writes templates/index.json, the catalog Designer Report reads.

    python templates/build_index.py           check, then write index.json
    python templates/build_index.py --check   check only (for pull requests)

Layout (one folder per template, one folder per version; older versions stay):

    templates/<id>/meta.json
    templates/<id>/<version>/template.jrxml
    templates/<id>/<version>/thumbnail.png     (optional)
    templates/<id>/<version>/version.json      (optional: {"updated": "...", "changes": {"ja": "...", "en": "..."}})

Only the Python standard library is used.
"""
import hashlib
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CATEGORIES = {"billing", "delivery", "list", "hr", "other"}
ID = re.compile(r"^[a-z0-9][a-z0-9-]*$")
VERSION = re.compile(r"^\d+\.\d+\.\d+$")
MAX_JRXML = 2 * 1024 * 1024
MAX_THUMBNAIL = 512 * 1024
# Report expressions are Java run by the app. A template has no business doing any of this;
# a match fails the check so a person looks at it.
FORBIDDEN = re.compile(
    r"Runtime|ProcessBuilder|System\s*\.\s*(exit|getenv|setProperty)|Class\s*\.\s*forName|getClassLoader"
    r"|java\s*\.\s*(io|nio|net|lang\s*\.\s*reflect)|javax\s*\.\s*script|Thread\b|\.invoke\s*\("
)


def version_key(v):
    return tuple(int(x) for x in v.split("."))


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def lang_map(value):
    if isinstance(value, str):
        return {"ja": value}
    return {k: v for k, v in (value or {}).items() if isinstance(v, str) and v.strip()}


def check_jrxml(path, errors):
    rel = path.relative_to(ROOT).as_posix()
    if path.stat().st_size > MAX_JRXML:
        errors.append(f"{rel}: larger than 2 MB")
        return
    text = path.read_text(encoding="utf-8")
    try:
        root = ET.fromstring(text.encode("utf-8"))
    except ET.ParseError as e:
        errors.append(f"{rel}: not valid XML ({e})")
        return
    if not root.tag.endswith("jasperReport"):
        errors.append(f"{rel}: the root element must be <jasperReport>")
    for m in re.finditer(r"<(expression|printWhenExpression|[a-zA-Z]*Expression)[^>]*>(.*?)</\1>", text, re.S):
        found = FORBIDDEN.search(m.group(2))
        if found:
            errors.append(f"{rel}: expression uses '{found.group(0)}', which templates may not use")
    if re.search(r'"[A-Za-z]:[\\/]|"/(Users|home)/', text):
        errors.append(f"{rel}: contains an absolute file path; use paths like images/logo.png")


def build():
    errors = []
    templates = []
    for folder in sorted(p for p in ROOT.iterdir() if p.is_dir() and not p.name.startswith((".", "_"))):
        tid = folder.name
        if not ID.match(tid):
            errors.append(f"{tid}: folder names use lower-case letters, digits and '-'")
            continue
        meta_path = folder / "meta.json"
        if not meta_path.is_file():
            errors.append(f"{tid}: meta.json is missing")
            continue
        try:
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            errors.append(f"{tid}/meta.json: {e}")
            continue
        title = lang_map(meta.get("title"))
        if not title:
            errors.append(f"{tid}/meta.json: needs a title (\"ja\" and/or \"en\")")
        category = meta.get("category", "other")
        if category not in CATEGORIES:
            errors.append(f"{tid}/meta.json: category must be one of {sorted(CATEGORIES)}")

        versions = []
        for vdir in folder.iterdir():
            if not vdir.is_dir():
                continue
            if not VERSION.match(vdir.name):
                errors.append(f"{tid}/{vdir.name}: version folders are named like 1.0.0")
                continue
            jrxml = vdir / "template.jrxml"
            if not jrxml.is_file():
                errors.append(f"{tid}/{vdir.name}: template.jrxml is missing")
                continue
            check_jrxml(jrxml, errors)
            entry = {
                "version": vdir.name,
                "file": jrxml.relative_to(ROOT).as_posix(),
                "sha256": sha256(jrxml),
            }
            thumb = vdir / "thumbnail.png"
            if thumb.is_file():
                if thumb.stat().st_size > MAX_THUMBNAIL:
                    errors.append(f"{tid}/{vdir.name}/thumbnail.png: larger than 512 KB")
                entry["thumbnail"] = thumb.relative_to(ROOT).as_posix()
                entry["thumbnailSha256"] = sha256(thumb)
            vmeta_path = vdir / "version.json"
            if vmeta_path.is_file():
                vmeta = json.loads(vmeta_path.read_text(encoding="utf-8"))
                if vmeta.get("updated"):
                    entry["updated"] = vmeta["updated"]
                changes = lang_map(vmeta.get("changes"))
                if changes:
                    entry["changes"] = changes
            versions.append(entry)
        if not versions:
            errors.append(f"{tid}: no version folder with a template.jrxml")
            continue
        versions.sort(key=lambda v: version_key(v["version"]), reverse=True)

        item = {"id": tid, "title": title, "category": category,
                "tags": [t for t in meta.get("tags", []) if isinstance(t, str)]}
        description = lang_map(meta.get("description"))
        if description:
            item["description"] = description
        if meta.get("minAppVersion"):
            item["minAppVersion"] = meta["minAppVersion"]
        item["versions"] = versions
        templates.append(item)
    return {"format": 1, "templates": templates}, errors


def main():
    index, errors = build()
    for e in errors:
        print("ERROR:", e)
    if errors:
        sys.exit(1)
    count = sum(len(t["versions"]) for t in index["templates"])
    if "--check" in sys.argv:
        print(f"OK: {len(index['templates'])} templates, {count} versions")
        return
    (ROOT / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote index.json: {len(index['templates'])} templates, {count} versions")


if __name__ == "__main__":
    main()
