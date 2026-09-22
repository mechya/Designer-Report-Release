# User guide

## The window

| Area | Purpose |
|---|---|
| **Project Explorer** (top left) | Files of the workspace. Two tabs: **Files** (folders as on disk) and **Reports** (each report with its subreports). |
| **Outline** (bottom left) | Structure of the open report: styles, parameters, fields, variables, bands and their elements. |
| **Editor** (center) | One tab per open file, each with **Design**, **Source** and **Preview**. |
| **Palette** (top right) | Elements to drag onto the report. |
| **Properties** (bottom right) | Settings of the selected element, or of the page when the report itself is selected. |
| **Report State** (bottom) | **Console**, **Errors**, **Statistics** and **Data Source**. |

## Project Explorer

- **Files** tab — the workspace as it is on disk.
- **Reports** tab — every report, with the subreports it uses nested underneath. Missing subreport files are shown as *(not found)*, reports that include themselves as *(circular)*. Hover a subreport to see which reports use it.
- Toolbar: **Collapse All / Expand All** and **Refresh**.
- Right-click a report for **New Subreport…**, **Attach Existing Subreport…**, **Rename**, **Delete**, **Copy Path** and **Show in Explorer / Finder**. See [Subreports](subreports.md).

## Designing

- **Add** — drag an element from the **Palette** onto a band.
- **Select** — click an element; **Shift+click** adds to the selection. In the **Outline**, **Ctrl+click** and **Shift+click** select several elements.
- **Move / resize** — drag the element or its handles; elements snap to the grid.
- **Right-click** (on the page or in the Outline): **Cut**, **Copy**, **Paste**, **Delete**, **Select All**, **Bring to Front**, **Send to Back**, **Align** (left, center, right, top, middle, bottom, distribute, same width/height), **Show/Hide Grid**, **Properties**.
- **Undo / Redo** — Ctrl+Z / Ctrl+Y.
- **Zoom** — Ctrl + mouse wheel, pinch on a trackpad, or the zoom box above the palette.
- **Bands** — right-click a band in the Outline to hide or show it (a hidden band has height 0 in the report).
- **Notes** — the *Note* element is a design-only sticky note; it is saved next to the report (`.notes.json`) and never printed.
- **Connectors** — hold **Alt** over an element to show its anchor points and draw design-only connector lines between elements.

## Elements

| Element | Notes |
|---|---|
| Static Text | Fixed text. |
| Text Field | An expression, e.g. `$F{name}`. The default `$F{field}` needs a field of that name. |
| Image | Choose a file; it is copied to the workspace `images/` folder. |
| Line, Rectangle, Ellipse | Shapes with pen width, style and color. |
| Frame | Groups elements; elements inside a frame move with it. |
| Page Break | Starts a new page. |
| Bar/QR Code | Code128, Code39, EAN-13, QR Code, PDF417, Data Matrix and more. |
| Subreport | Another report inside this one — see [Subreports](subreports.md). |
| Chart | Type, title, legend, category / value / series expressions. |
| Crosstab | Row groups, column groups and measures. Bucket values must not be empty (null). |
| List | Repeats its content for each record of a dataset. A new list gets its own empty dataset. |
| Page Number, Total Pages, Page X of Y, Current Date, Time, Percentage | Ready-made text fields. |

## Source

The **Source** tab shows the JRXML with syntax highlighting. Changes in the design view are applied to the source, and vice versa.

- **Ctrl+F** — find
- **Ctrl+Shift+F** — format

## Preview

The **Preview** tab compiles and fills the report and shows the pages. Use **Refresh Preview** after changes, and the page buttons to move between pages. Compile errors are listed in the **Errors** tab.

Preview sets `SUBREPORT_DIR` to the report's folder automatically, so subreports with relative paths work.

## Data sources (JSON)

1. Open the **Data Source** tab at the bottom.
2. Choose a JSON file and, if needed, a query path (the array of records).
3. Click **Detect Fields** — the fields are added to the report.
4. Preview shows the report filled with the JSON data.

The settings are saved per report (`.json-config` next to the report).

## Compile (build)

**Compile** in the toolbar builds the whole workspace into a `build/` folder that you can copy
anywhere — a server, another computer — and use as it is. It is written fresh on every build, so
reports you deleted or renamed never linger in it. Previewing a report does not touch `build/`.

`build.zip` is written next to the folder with exactly the same content, for sending it on or
copying it to a server.

| In `build/` | |
|---|---|
| `jasper/` | the compiled reports — what your application loads, in the same folder structure as the workspace |
| `fonts/` | **only** the fonts the reports actually use, with `jasper-fonts.xml` and the font licenses |
| `images/` | only the images the reports actually use |
| `jasperreports_extension.properties` | tells JasperReports where the fonts are |
| `README.txt` | what the folder contains and how to fill a report from Java |

No `.jrxml` sources are shipped. A report written in Designer Report compiles its subreports from
source while it is filled, so the build rewrites each of those references to the compiled `.jasper`
next to it and says how many it changed:

```
5 subreport reference(s) now point at the compiled .jasper
```

Your workspace `.jrxml` files are untouched — only the copies inside the build are rewritten. If a
reference cannot be rewritten (its target was not built, or the expression is not the generated
form), that one report's source is shipped alongside so filling still works, and the console says so.

Set `SUBREPORT_DIR` to the folder of the report being filled — `build/jasper/` for a report at the
top of it.

Reports whose file name still starts with *untitled* are treated as drafts and left out, unless
another report uses them as a subreport. The console says which ones were skipped and why:

```
Skipped untitled.jrxml - draft ("untitled" file name, not used by any report)
```

Give a draft a real name to have it built.

**Clean** removes `build/` and `build.zip`.

## Fonts

**Tools → Manage Fonts** shows the fonts of the workspace with a preview and details. See [Fonts](fonts.md).

## Preferences

**Window → Preferences**: theme (Light, Dark, Auto) and language (English, 日本語).

## Help menu

| Item | |
|---|---|
| Documentation | Opens this documentation. |
| Report an Issue | Opens the issue form on GitHub. |
| Donate | Supports development via Buy Me a Coffee. |
| Check for Updates… | Checks GitHub for a newer version (installer versions; the Store updates its version itself). |
| About Designer Report | Version, copyright and licenses. |

## Keyboard shortcuts

| Shortcut | Action |
|---|---|
| Ctrl+S | Save |
| Ctrl+Shift+S | Save As |
| Ctrl+Z / Ctrl+Y | Undo / Redo |
| Ctrl+C / Ctrl+X / Ctrl+V | Copy / Cut / Paste element |
| Delete | Delete selected element(s) |
| Ctrl+F | Find in Source |
| Ctrl+Shift+F | Format Source |
| Ctrl + mouse wheel | Zoom |
| Esc | Cancel the current action |

On macOS use **⌘** instead of Ctrl.
