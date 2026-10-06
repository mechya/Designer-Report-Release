# Changelog

All notable changes to Designer Report are listed here. Versions follow `MAJOR.MINOR.PATCH`.

## [1.5.0] - 2026-10-05

### Added
- **Find and Change** (Edit menu, and the design's right-click menu). Lists the elements of the open report, and optionally its subreports, by type, text or expression, name and font size — frames' contents included. The list filters and sorts like a spreadsheet and copies to Excel. Change the font, size, style and alignment of text, colors and size of any element, lines and borders, and image scaling for every ticked element at once; each report changes in one undo step.
- **Select on canvas.** The elements ticked in Find and Change are selected on the design and in the Outline as you tick them; clicking a row scrolls the design to it.
- **Element names.** Give an element a name (its JRXML `key`) in Properties; the Outline shows it and Find and Change searches it.
- **A color for each element type.** Text, fields, images, lines, shapes, frames, subreports, barcodes, lists, charts, crosstabs, page breaks and notes each have their own selection color on the design; page number, date, time, percentage and "page X of Y" fields have theirs too. The palette icons, the Outline icons and Find and Change use the same colors.
- A loading tab appears at once when a report is opened from the Project Explorer.

### Changed
- A page break shows that it is selected (it used to show nothing).

### Fixed
- Folding or unfolding a node in the Outline cleared the selection on the design.
- With two monitors at different scaling, the window kept the other monitor's size when moved back.

## [1.4.0] - 2026-09-30

### Added
- **PDF viewer.** PDFs in the workspace (test results, exports) open in a Studio tab: all pages, zoom, page buttons, and **Open in PDF app**. The file is not locked while open, and the tab shows the new PDF after a test runs again.
- **Template test: Full page and Next page.** Two new cases fill the first page exactly, and one row more so the report runs onto a second page, to check page breaks. The number of rows is found automatically.
- **Project Explorer:** folders can be deleted (for example old `test-results`), files have **Open**, and double-clicking a file the Studio can't show opens it in its Windows app.

### Changed
- The **Test** button always opens the test wizard on its first page, filled in with the last settings. **Tools → Test Settings** and the button's dropdown are gone.
- JSON files: the Table / Source tabs look like the report editor's, so the open one is clear.

### Fixed
- The source view marked valid JRXML as an error ("No matching opening tag") when a line held several tags, such as `<element …><expression>…</expression></element>`.
- Opening a JSON file with rows crashed the outline.
- Hindi, Nepali and other scripts where one letter is several characters were cut mid-letter in the "just fits", "too long" and "short" tests; AI text with broken vowel signs is no longer used.
- Folder **Copy Path** and **Show in Explorer** used the workspace instead of the folder.

## [1.3.0] - 2026-09-28

### Added
- **New Report wizard.** File → New (and the toolbar and Project Explorer) now asks how to start: **Blank** (paper size and orientation), **Template** or **Create with AI**. Templates and AI drafts open in an editor with a live preview of the first page; nothing is saved until **Create** or **Create and Test**.
- **Create with AI.** Describe the report and the offline AI helper drafts a layout — title, fields at the top, table columns with sums, notes. Ask for changes in plain words ("remove the number, add a year and a month column", "remove the logo"); every request is kept in a history with Undo. The app lays out the page itself, so the JRXML is always valid.
- **Templates.** Six built-in templates (invoice, quotation, delivery note, purchase order, receipt, customer list) with labels in Japanese, English and other languages; **My Templates** from a folder of your own (by default the workspace `templates/`, or a shared folder); and an optional **online library** in this repository, off until you switch it on. Search in any language and filter by source.
- **Template versions.** A template can have several versions; the newest is offered and older ones stay selectable with what changed. Reports remember the template and version they came from.
- **File → Save as Template…** saves the open report as a template with a picture of its first page; saving again under the same name adds a new version.
- **Template test** (Tools → Test Template, Ctrl+Shift+T): fills the report with sample data in four cases (empty, short, just fits, too long) in the languages you choose, saves a PDF of each, and lists cut-off text, shrinking fonts, growing boxes, "null" printed for empty fields and page counts. Picture fields get sample pictures.
- **AI helper** (optional, offline): a free model (Google Gemma 3 or Meta Llama 3.2) downloaded once, used for realistic test text and for drafting templates. **Tools → AI Helper…** shows which models are installed and in use, switches between them, and deletes them to free space.
- Placeholder logos: a drawn stand-in saved as `images/logo.png`, replaced with **Replace…** in Properties; **Build** warns while one is still in use.

### Changed
- Build skips the templates folder.
- Deleting an image element keeps the picture file when another report still uses it.

### Fixed
- Pictures from the workspace `images/` folder failed to preview and test on Windows (the path was written with backslashes into a Java string).
- A `.ttf` that is really a font collection (a `.ttc` copied to a `.ttf` name, such as `BIZ-UDGOTHICR.TTF`) no longer breaks PDF export: a real single font of the family is preferred, and a collection is embedded from the `.ttc` beside it. Test errors name the font file and what to do.
- The Japanese input (IME) candidate box opens under the cursor on scaled displays.
- `run.bat` found Maven's Unix script instead of `mvn.cmd` and failed to start the app.

## [1.2.3] - 2026-09-25

### Fixed
- The main window no longer opens with its title bar above the screen on displays with 125–150 % scaling: its size is capped to the screen, and it opens centred or maximized.

## [1.2.2] - 2026-09-25

### Removed
- **Check for Updates.** The Microsoft Store version crashed at startup because of it; the Store installs updates itself.

## [1.2.1] - 2026-09-24

### Fixed
- With Windows *Controlled folder access* on, the app explains that the workspace folder in Documents is blocked, and offers Windows Security or another folder, instead of failing to start.

## [1.2.0] - 2026-09-23

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
- **Build output is portable and smaller.** `build/` now holds the compiled reports in `jasper/`, keeping the workspace's folder structure, plus only the fonts and images the reports actually use (with the font licenses and a matching `jasper-fonts.xml`) and a `README.txt` explaining how to fill a report from Java. The folder can be copied to a server and used as it is.
- **No sources in the build.** Subreport references are rewritten to point at the compiled `.jasper` beside them, so nothing is compiled while a report is filled — faster, and no `.jrxml` has to be deployed. References that cannot be rewritten keep their source, and the console says which.
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
