# Changelog

All notable changes to Designer Report are listed here. Versions follow `MAJOR.MINOR.PATCH`.

## [Unreleased]

### Added
- **Project Explorer tabs — Files / Reports.** The Reports tab shows every report with its subreports nested; missing and circular references are marked.
- **Subreport actions** (right-click in the Reports tab): New Subreport, Attach Existing, Show in main report, Delete. Deleting a subreport removes its boxes from every report that uses it; **Ctrl+Z** restores everything, and deleted files go to the Recycle Bin / Trash.
- **Fix Subreport Paths** (right-click the workspace root) rewrites absolute subreport paths to relative ones.
- Preview sets `SUBREPORT_DIR` to the report's folder automatically.
- **Outline:** multi-selection with Ctrl/Shift+click; right-click opens the same menu as the design canvas. Delete, Bring to Front and Send to Back act on all selected elements.
- **Manage Fonts:** font names in the list, a Font Info panel (name, family, version, copyright, license) with a copy button, and a picker for fonts inside collections (.ttc).
- Icons in all menus and context menus; Collapse All / Expand All toggle in the Project Explorer.
- Help menu: Documentation, Report an Issue, Donate, About Designer Report; Check for Updates uses GitHub Releases.

### Fixed
- Subreports now render their content in the design view again.
- Elements inside the Detail band are listed in the Outline.
- Frames, lists and unknown elements (e.g. tables) are no longer removed when a report is edited after reopening.
- Crosstabs and lists now compile with JasperReports 7.
- Subreport parameters no longer break compilation after a design edit.
- Dark theme for all dialogs (Preferences, Manage Fonts, confirmations, input dialogs).
- Only one Data Source tab is shown.

## [1.1.8]

- Last release before this changelog.
