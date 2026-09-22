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

### Changed
- **Build output is portable and smaller.** `build/` now holds the compiled reports *and* their `.jrxml` sources in the workspace's folder structure, only the fonts and images the reports actually use (with the font licenses and a matching `jasper-fonts.xml`), and a `README.txt` explaining how to fill a report from Java. The folder can be copied to a server and used as it is.
- `build.zip` is written next to `build/` with the same content; **Clean** removes both.
- `build/` is emptied before every build, so deleted or renamed reports no longer linger in the output.
- Reports still named *untitled…* are skipped unless another report uses them as a subreport; the console says which ones were skipped and why.
- **Compile** writes the build output; previewing a report no longer does, which makes Preview faster.

### Fixed
- Fonts are found regardless of the system language: font families are read from the font files themselves, so a build on an English system no longer ends up with no fonts.
- Subreports now render their content in the design view again.
- Elements inside the Detail band are listed in the Outline.
- Frames, lists and unknown elements (e.g. tables) are no longer removed when a report is edited after reopening.
- Crosstabs and lists now compile with JasperReports 7.
- Subreport parameters no longer break compilation after a design edit.
- Dark theme for all dialogs (Preferences, Manage Fonts, confirmations, input dialogs).
- Only one Data Source tab is shown.

## [1.1.8]

- Last release before this changelog.
