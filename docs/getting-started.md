# Getting started

## 1. Install

- **Windows** — install from the Microsoft Store *(coming soon)*, or download the `.exe` installer from [Releases](https://github.com/mechya/Designer-Report-Release/releases/latest) and run it.
- **macOS** — download the `.dmg` from [Releases](https://github.com/mechya/Designer-Report-Release/releases/latest), open it and drag **Designer Report** to *Applications*.

No separate Java installation is needed.

## 2. Choose a workspace

On the first start, Designer Report asks for a **workspace folder** — the folder where your reports live. Pick an empty folder (or one that already contains `.jrxml` files) and click **Launch**.

Tick *Use this as the default and do not ask again* to skip this step next time. You can switch later with **File → Switch Workspace…**.

The app creates these folders in the workspace:

| Folder | Contents |
|---|---|
| `fonts/` | Fonts your reports use (see [Fonts](fonts.md)) |
| `images/` | Images placed in reports |
| `data/` | Sample data, e.g. JSON files |
| `build/` | Output of **Compile**: `jasper/` with the compiled reports, and only the fonts and images they need. `build.zip` next to it holds the same content |

## 3. Create a report

1. **File → New** (or right-click the workspace in the Project Explorer → **New Report**).
2. Enter a file name, e.g. `invoice.jrxml`.
3. The report opens with three tabs: **Design**, **Source** and **Preview**.

## 4. Add elements

1. Drag an element from the **Palette** (right side) onto a band — for example **Static Text** into the *Title* band.
2. Select it to edit its text, font, size and position in the **Properties** panel.
3. Move it with the mouse or the arrow fields; hold **Shift** to select several elements, then right-click → **Align**.

## 5. Preview

Click the **Preview** tab (or **Compile** in the toolbar). The report is compiled, filled and shown page by page. Messages appear in the **Console** and **Errors** tabs at the bottom.

To preview with data, open the **Data Source** tab at the bottom, choose a JSON file and click **Detect Fields**.

## 6. Save

**File → Save** (Ctrl+S). A `*` in the tab title means the report has unsaved changes.

## Next

- [User guide](user-guide.md) — everything in detail
- [Subreports](subreports.md) — reports inside reports
- [Fonts](fonts.md) — Japanese fonts and font licensing
